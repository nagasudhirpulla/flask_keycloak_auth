import functools
from flask import redirect, url_for, request, abort
from src.security.user import getUserFromSession


def login_required(_func=None, *, roles=[]):
    def decorator_login_required(func):
        """Make sure user is logged in before proceeding"""
        @functools.wraps(func)
        def wrapper_login_required(*args, **kwargs):
            user = getUserFromSession()
            if user == None:
                return redirect(url_for("oauth.login", next=request.url))
            # check user roles
            isRolesPresent = True if len(roles) == 0 else all(
                [rl in user["roles"] for rl in roles])
            if not isRolesPresent:
                return abort(401)
            return func(*args, **kwargs)
        return wrapper_login_required

    if _func is None:
        return decorator_login_required
    else:
        return decorator_login_required(_func)
