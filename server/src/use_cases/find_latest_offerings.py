from typing import Callable, List, Tuple

from src.entities import Offering, OfferingAudio
from src.use_cases.utils import check_permission


def build_find_latest_offerings(
    retrieve_latest_offerings: Callable[
        [], Tuple[List[Offering], List[OfferingAudio]]]
) -> Callable[[str], Tuple[List[Offering], List[OfferingAudio]]]:

    # NOTE(andrea): check_permission decorator expects
    # an auth token as the 1st argument.
    # This is way we return a Callable[[str], List[Offering]].
    @ check_permission(login_only=True)
    def find_latest_offerings() -> Tuple[List[Offering], List[OfferingAudio]]:
        return retrieve_latest_offerings()

    return find_latest_offerings  # type: ignore
