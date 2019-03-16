from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(config_class)

    db.init_app(application)
    migrate.init_app(application, db)
    login_manager.init_app(application)
    mail.init_app(application)
    bootstrap.init_app(application)
    moment.init_app(application)

    if not application.debug and not application.testing:
        if application.config['MAIL_SERVER']:
            auth = None
            if application.config['MAIL_USERNAME'] or \
                    application.config['MAIL_PASSWORD']:
                auth = (
                    application.config['MAIL_USERNAME'],
                    application.config['MAIL_PASSWORD'])
            secure = None
            if application.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(
                    application.config['MAIL_SERVER'],
                    application.config['MAIL_PORT']),
                fromaddr='no-reply@' + application.config['MAIL_SERVER'],
                toaddrs=application.config['ADMINS'],
                subject='Miroblog Failure', secure=secure,
                credentials=auth
            )
            mail_handler.setLevel(logging.ERROR)
            application.logger.addHandler(mail_handler)

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler(
            'logs/app.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s \
                [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        application.logger.addHandler(file_handler)

        application.logger.setLevel(logging.INFO)
        application.logger.info('Miroblog startup')

    from app.errors import bp as errors_bp
    application.register_blueprint(errors_bp)
    from app.auth import bp as auth_bp
    application.register_blueprint(auth_bp, url_prefix='/auth')
    from app.main import bp as main_bp
    application.register_blueprint(main_bp)

    return application
