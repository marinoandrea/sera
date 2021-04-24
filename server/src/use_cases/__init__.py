import src.data_access.database.offering as OfferingRepository
import src.data_access.database.user as UserRepository
from src.plugins import auth_manager, file_manager, password_manager

from .authenticate_phone_number import build_authenticate_phone_number
from .find_latest_offerings import build_find_latest_offerings
from .find_offering_audios import build_find_offering_audios
from .find_offerings import build_find_offerings
from .login import build_login
from .make_search_audio import build_make_search_audio
from .register_user import build_register_user
from .upload_offering import build_upload_offering

authenticate_phone_number = build_authenticate_phone_number(
    UserRepository.retrieve_user_by_phone_number,
    auth_manager
)

find_latest_offerings = build_find_latest_offerings(
    OfferingRepository.retrieve_latest_offerings,
    OfferingRepository.retrieve_offering_audios_by_id,
    UserRepository.retrieve_users_by_id
)

make_search_audio = build_make_search_audio(
    OfferingRepository.retrieve_offering_audios  # type: ignore
)

upload_offering = build_upload_offering(
    OfferingRepository.create_offering,
    OfferingRepository.create_offering_audio,
    UserRepository.retrieve_user_by_phone_number,
    file_manager
)

find_offerings = build_find_offerings(
    OfferingRepository.retrieve_offerings,  # type: ignore
    UserRepository.retrieve_users_by_id
)

login = build_login(
    UserRepository.retrieve_user_by_email,
    password_manager,
    auth_manager
)

register_user = build_register_user(
    UserRepository.create_user,
    password_manager,
    auth_manager
)


find_offering_audios = build_find_offering_audios(
    OfferingRepository.retrieve_offering_audios  # type: ignore
)
