from time import time

import src.data_access.database.user as UserRepository
from src.plugins import auth_manager

from .permissions import build_check_permission

check_permission = build_check_permission(
    UserRepository.retrieve_user_by_id,
    auth_manager
)


def get_cursor():
    return time() * 1000


__all__ = [
    'check_permission'
]
