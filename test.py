from db.base import Base
from db.session import engine
from db.models import *
from db.session import SessionLocal
from db.repositories import UserRepository

session = SessionLocal()
user_repository = UserRepository(session)


def create_tables():
    Base.metadata.create_all(bind=engine)


def create_user():
    user = user_repository.create_user(
        first_name="Vali5", username="vali8", last_name="Aliyev5"
    )


def get_users():
    users = user_repository.get_all_users()

    for user in users:
        print(user.user_id, user.username)


def get_user():
    user = user_repository.get_one_user(3)
    print(user)


def get_active_users():
    users = user_repository.get_active_users()
    print(users)


def delete_user():
    user_repository.delete_user(5)


def update_user():
    user_repository.update_user(
        6,
        "TEST",
    )


# create_tables()
# create_user()
# get_users()
# get_user()
# get_active_users()
# delete_user()
update_user()
