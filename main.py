from contextlib import contextmanager
from config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from data.data import fake_roles, fake_users
from models.models import Roles, Users


engine = sa.create_engine(
    f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
    echo=True,
)

DBSession = sessionmaker(engine)


@contextmanager
def session_scope():
    """Provides a transactional scope around a series of operations."""
    session = DBSession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


if __name__ == '__main__':
    with session_scope() as s:
        all_users = s.query(Users.id).filter(Users.username.like('user%')).order_by(Users.id.desc())
        all_users = all_users.add_columns(Users.username, Users.email, Users.password)
        for current_user in all_users:
            print(current_user)