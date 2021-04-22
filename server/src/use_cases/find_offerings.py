from typing import Callable, List, Tuple

from src.entities import Offering, OfferingAudio


def build_find_offerings(
    retrieve_offerings: Callable[
        [], List[Offering]]
) -> Callable[[str], List[Offering]]:

    def find_offerings() -> List[Offering]:
        return retrieve_offerings()

    return find_offerings
