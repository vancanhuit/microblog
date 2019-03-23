from app.models import User, Post
from datetime import datetime, timedelta


def test_connect(database):
    assert database is not None


def test_password_hashing():
    u = User(username='jojo')
    u.set_password('example')
    assert u.check_password('example')
    assert not u.check_password('sample')


def test_avatar():
    u = User(username='john', email='john@example.com')
    u.avatar(128) == ('https://www.gravatar.com/avatar/'
                      'd4c74594d841139328695756648b6bd6'
                      '?s=128&d=identicon')


def test_follow(database):
    u1 = User(username='john', email='john@example.com')
    u2 = User(username='susan', email='susan@example.com')
    database.session.add(u1)
    database.session.add(u2)
    database.session.commit()

    assert u1.followed.count() == 0
    assert u1.followers.count() == 0

    u1.follow(u2)
    assert u1.is_following(u2)
    assert u1.followed.count() == 1
    assert u2.followers.count() == 1

    u1.unfollow(u2)
    assert not u1.is_following(u2)
    assert u1.followed.count() == 0
    assert u2.followers.count() == 0


def test_followed_posts(database):
    u1 = User(username='john', email='john@example.com')
    u2 = User(username='susan', email='susan@example.com')
    u3 = User(username='mary', email='mary@example.com')
    u4 = User(username='david', email='david@example.com')
    database.session.add_all([u1, u2, u3, u4])
    now = datetime.utcnow()
    p1 = Post(body='Post from john', author=u1,
              timestamp=now + timedelta(seconds=1))
    p2 = Post(body='Post from susan', author=u2,
              timestamp=now + timedelta(seconds=4))
    p3 = Post(body='Post from mary', author=u3,
              timestamp=now + timedelta(seconds=3))
    p4 = Post(body='Post from david', author=u4,
              timestamp=now + timedelta(seconds=2))
    database.session.add_all([p1, p2, p3, p4])
    database.session.commit()

    u1.follow(u2)
    u1.follow(u4)
    u2.follow(u3)
    u3.follow(u4)
    database.session.commit()

    f1 = u1.followed_posts().all()
    f2 = u2.followed_posts().all()
    f3 = u3.followed_posts().all()
    f4 = u4.followed_posts().all()
    assert f1 == [p2, p4, p1]
    assert f2 == [p2, p3]
    assert f3 == [p3, p4]
    assert f4 == [p4]
