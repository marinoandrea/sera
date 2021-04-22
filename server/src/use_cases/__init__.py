import src.data_access.database.offering as OfferingRepository
import src.data_access.database.user as UserRepository
from src.plugins import auth_manager

from .authenticate_phone_number import build_authenticate_phone_number
from .find_latest_offerings import build_find_latest_offerings
from .make_search_audio import build_make_search_audio
from .upload_offering import build_upload_offering
from .find_offerings import build_find_offerings


authenticate_phone_number = build_authenticate_phone_number(
    UserRepository.retrieve_user_by_phone_number,
    auth_manager
)

find_latest_offerings = build_find_latest_offerings(
    OfferingRepository.retrieve_latest_offerings
)

make_search_audio = build_make_search_audio(
    OfferingRepository.retrieve_offering_audios  # type: ignore
)

upload_offering = build_upload_offering(
    OfferingRepository.create_offering,
    UserRepository.retrieve_user_by_phone_number
)

find_offerings = build_find_offerings(
    OfferingRepository.retrieve_offerings
)
