from time import time

from src.data_access.database.user import retrieve_user_by_id
from src.plugins import auth_manager

from .permissions import build_check_permission

check_permission = build_check_permission(
    retrieve_user_by_id, auth_manager)


def get_cursor():
    return time() * 1000


__all__ = [
    'check_permission'
]
