import src.data_access.database.offering as OfferingRepository
import src.data_access.database.user as UserRepository
from src.plugins import auth_manager

from .authenticate_phone_number import build_authenticate_phone_number
from .find_latest_offerings import build_find_latest_offerings

authenticate_phone_number = build_authenticate_phone_number(
    UserRepository.retrieve_user_by_phone_number,
    auth_manager
)

find_latest_offerings = build_find_latest_offerings(
    OfferingRepository.retrieve_latest_offerings
)
