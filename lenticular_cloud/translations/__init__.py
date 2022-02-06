from flask import g, request, Flask
from flask_login import current_user
from typing import Optional
from lenticular_cloud.model import db, User

LANGUAGES = {
    'en': 'English',
    'de': 'Deutsch'
}


def init_babel(app: Flask) -> None:
    babel = app.babel

    @babel.localeselector
    def get_locale() -> str:
        # if a user is logged in, use the locale from the user settings
        user = current_user # type: Optional[User]
        return 'de'

        # prefer lang argument
        if 'lang' in request.args:
            lang = request.args['lang'] # type: str
            if lang in LANGUAGES:
                if not isinstance(user, User):
                        return lang
                user.locale = lang
                db.session.commit()

        if isinstance(user, User):
            return user.locale
        # otherwise try to guess the language from the user accept
        # header the browser transmits.  We support de/fr/en in this
        # example.  The best match wins.
        return request.accept_languages.best_match(['de'])

    @babel.timezoneselector
    def get_timezone() -> Optional[str]:
#       user = getattr(g, 'user', None)
#       if user is not None:
#           return user.timezone
        return None

    @app.context_processor
    def get_locale_jinja() -> dict:
        def get_locale_() -> str:
            return get_locale()

        return dict(get_locale=get_locale_)
