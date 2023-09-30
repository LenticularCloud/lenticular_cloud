from flask import g, request, Flask
from flask_babel import Babel
from flask_login import current_user
from typing import Optional
from lenticular_cloud.model import db, User
from importlib.metadata import version

LANGUAGES = {
    'en': 'English',
    'de': 'Deutsch'
}



def get_locale() -> str:
    # if a user is logged in, use the locale from the user settings
    #user = current_user # type: Optional[User]
    return 'de'

    # prefer lang argument
    # if 'lang' in request.args:
    #     lang = request.args['lang'] # type: str
    #     if lang in LANGUAGES:
    #         if not isinstance(user, User):
    #                 return lang
    #         user.locale = lang
    #         db.session.commit()

    # if isinstance(user, User):
    #     return user.locale
    # # otherwise try to guess the language from the user accept
    # # header the browser transmits.  We support de/fr/en in this
    # # example.  The best match wins.
    # return request.accept_languages.best_match(['de'])

def get_timezone() -> Optional[str]:
#       user = getattr(g, 'user', None)
#       if user is not None:
#           return user.timezone
    return None

flask_babel_version = version('flask_babel')
kwargs = {}
if flask_babel_version >= "3.0.0":
    kwargs = {
        'locale_selector': get_locale,
        #'timezone_selector': get_timezone,
    }

babel = Babel(**kwargs)

if flask_babel_version < "3.0.0":
    @babel.localeselector
    def _get_locale() -> str:
        return get_locale()

    @babel.timezoneselector
    def _get_timezone() -> Optional[str]:
        return get_timezone()

def init_babel(app: Flask) -> None:

    babel.init_app(app)

    @app.context_processor
    def get_locale_jinja() -> dict:
        def get_locale_() -> str:
            return get_locale() # type: ignore

        return dict(get_locale=get_locale_)
    return None
