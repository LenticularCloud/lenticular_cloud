import argparse
from .model import db, User, UserSignUp
from .app import create_app
from werkzeug.middleware.proxy_fix import ProxyFix

import logging
import os


def entry_point():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    parser = argparse.ArgumentParser(description='lenticular_cloud cli')
    subparsers = parser.add_subparsers()

    parser_user = subparsers.add_parser('user')
    parser_user.set_defaults(func=cli_user)

    parser_signup = subparsers.add_parser('signup')
    parser_signup.add_argument('--signup_id', type=int)
    parser_signup.set_defaults(func=cli_signup)

    parser_run = subparsers.add_parser('run')
    parser_run.set_defaults(func=cli_run)

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


def cli_user(args):
    print(User.query.all())
    pass

def cli_signup(args):
    
    print(args.signup_id)
    if args.signup_id is not None:
        user_data = UserSignUp.query.get(args.signup_id)
        user = User.new(user_data)

        db.session.add(user)
        db.session.delete(user_data)
        db.session.commit()
    else:
        # list
        print(UserSignUp.query.all())


def cli_run(app, args):
    logging.basicConfig(level=logging.DEBUG)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1)
    app.run(debug=True, host='127.0.0.1', port=5000)

if __name__ == "__main__":
    entry_point()

