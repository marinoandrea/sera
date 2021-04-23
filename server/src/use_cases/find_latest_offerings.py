from typing import Callable, List, Tuple

from src.entities import Offering, OfferingAudio, User

from .utils import check_permission


def build_find_latest_offerings(
    retrieve_latest_offerings: Callable[[], List[Offering]],
    retrieve_offering_audios_by_id: Callable[[List[str]], List[OfferingAudio]],
    retrieve_users_by_id: Callable[[List[str]], List[User]],
) -> Callable[[str], Tuple[List[Offering], List[OfferingAudio], List[User]]]:

    # NOTE(andrea): check_permission decorator expects
    # an auth token as the 1st argument.
    # This is way we return a Callable[[str], List[Offering]].
    @check_permission(login_only=True)
    def find_latest_offerings() -> Tuple[
            List[Offering], List[OfferingAudio], List[User]
    ]:
        offerings = retrieve_latest_offerings()
        audios = retrieve_offering_audios_by_id(
            list(map(lambda o: o.id, offerings)))
        users = retrieve_users_by_id(
            list(map(lambda o: o.user_account_id, offerings)))
        return offerings, audios, users

    return find_latest_offerings  # type: ignore
