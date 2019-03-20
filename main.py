from app import db, Config, create_app
from app.models import User, Post, Message, Notification, Task

application = create_app(config_class=Config)


@application.shell_context_processor
def make_shell_context():
    return {
        'db': db, 'User': User, 'Post': Post,
        'Message': Message, 'Notification': Notification.id,
        'Task': Task}
