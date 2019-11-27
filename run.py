from platform import platform

class Config(object):
    DEBUT = True
    DEVELOPMENT = True
    SECRET_KEY = "1hbd87sbwjV6stB#dj79726$!"
    THREADS_PER_PAGE = 2
    CSRF_ENABLED = True
    # CSRF_SESSION_KEY = "1hbd87sbwjV6stB#dj79726$!"
    # DB_HOST = 'local.database'


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    # DB_HOST = 'production.database'


platform.config.from_object(Config())
platform.run(debug=True)
