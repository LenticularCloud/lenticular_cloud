import argparse
from .model import db, User
from .app import create_app
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_migrate import upgrade
from pathlib import Path
from flask import Flask

import logging
import os


def entry_point() -> None:
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    parser = argparse.ArgumentParser(description='lenticular_cloud cli')
    subparsers = parser.add_subparsers()

    parser_user = subparsers.add_parser('user')
    parser_user.set_defaults(func=cli_user)

    parser_signup = subparsers.add_parser('signup')
    parser_signup.add_argument('--signup_id', type=str)
    parser_signup.set_defaults(func=cli_signup)

    parser_run = subparsers.add_parser('run')
    parser_run.set_defaults(func=cli_run)

    parser_db_upgrade = subparsers.add_parser('db_upgrade')
    parser_db_upgrade.set_defaults(func=cli_db_upgrade)

    '''
    parser_upcoming = subparsers.add_parser('upcoming')
    parser_upcoming.set_defaults(func=cli_upcoming)
    parser_upcoming.add_argument('-a', '--all', help='shows all single order`', nargs='?', default=False, const=True,
                                 type=bool,
                                 required=False)
    parser_upcoming.add_argument('-n', '--no-import', dest='noimport', help='do not a automatic import', nargs='?',
                                 default=False, type=bool, required=False)
    parser_upcoming.add_argument('-F', '--format', help='format can be `d`|`m`|`y`', default='d', required=False)

    # parser_select.add_argument('-F', '--format', help='format can be `d`|`m`|`y`', default='d', required=False)
    # parser_select.add_argument('-f', '--from', help='from date in the format `yyyy-mm-dd`', required=False)
    # parser_select.add_argument('-t', '--to', help='to date in the format `yyyy-mm-dd`', required=False)
    '''
    args = parser.parse_args()
    if 'func' not in args:
        parser.print_help()
        return
    app = create_app()
    if args.func == cli_run:
        cli_run(app,args)
        return
    with app.app_context():
        args.func(args)


def cli_user(args) -> None:
    for user in User.query.all():
        print(f'{user.id} - Enabled: {user.enabled} - Name:`{user.username}`')
    pass

def cli_signup(args) -> None:

    if args.signup_id is not None:
        user = User.query.get(args.signup_id)
        if user == None:
            print("user not found")
            return
        user.enabled = True

        db.session.commit()
    else:
        # list
        print('disabled users:')
        for user in User.query.filter_by(enabled=False).all():
            print(f'<Signup id={user.id}, username={user.username}>')


def cli_run(app: Flask, args) -> None:
    print("running in debug mode")
    logging.basicConfig(level=logging.DEBUG)
    #app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1)
    app.run(debug=True, host='127.0.0.1', port=5000)


def cli_db_upgrade(args) -> None:
    app = create_app()
    migration_dir = Path(app.root_path) / 'migrations'
    upgrade( str(migration_dir) )


if __name__ == "__main__":
    entry_point()

