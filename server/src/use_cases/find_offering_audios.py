from typing import Callable, List

from src.entities import OfferingAudio


def build_find_offering_audios(
    retrieve_offering_audios: Callable[[dict], List[OfferingAudio]]
) -> Callable[[str, str, str, float, float], List[OfferingAudio]]:

    def find_offering_audios(
        lang: str,
        category: str,
        subcategory: str,
        min_quantity: float = 0.0,
        max_quantity: float = 9999.0
    ) -> List[OfferingAudio]:
        audios = retrieve_offering_audios({
            'lang': lang,
            'category': category,
            'subcategory': subcategory,
            'min_quantity': min_quantity,
            'max_quantity': max_quantity
        })
        return audios

    return find_offering_audios
