from flask import session
from typing import Optional, TypedDict

__sessionUserKey = 'user'


class User(TypedDict):
    userId: str
    userName: str
    email: str
    roles: list[str]
    idToken: str


def createUserSession(userId: str, userName: str, email: str, roles: list[str] = [], idToken=""):
    user: User = {
        "userId": userId,
        "userName": userName,
        "email": email,
        "roles": roles,
        "idToken": idToken
    }
    session[__sessionUserKey] = user


def clearUserSession():
    session.pop(__sessionUserKey, None)


def getUserFromSession() -> Optional[User]:
    if not __sessionUserKey in session:
        return None
    return session[__sessionUserKey]
