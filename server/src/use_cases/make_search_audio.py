import os
import pathlib
from time import time
from typing import Callable, List, Optional

from src.entities import OfferingAudio


def build_make_search_audio(
    retrieve_offerings_audio: Callable[[dict], List[OfferingAudio]]
):

    def make_search_audio(
        lang: str,
        category: str,
        subcategory: str,
        min_quantity: float = 0,
        max_quantity: float = 99999,
    ) -> Optional[str]:
        """
        Returns the path of a temp .wav audio file which contains
        information about offerings determined by the search
        parameters in input.
        """

        offering_audios = retrieve_offerings_audio({
            'lang': lang,
            'category': category,
            'subcategory': subcategory,
            'min_quantity': min_quantity,
            'max_quantity': max_quantity
        })
        if len(offering_audios) == 0:
            return None

        output_path = f'temp_search_{int(time() * 1000)}.wav'
        output_path = str(pathlib.Path(os.getcwd()).joinpath(output_path))

        # use sox to concat offering audios in a single temp file
        sox_string = 'sox -b 16 -c 1 -e signed-integer '
        sox_string += ' '.join(a.path for a in offering_audios)
        sox_string += f' {output_path} rate 8k'

        pathlib.Path(output_path).touch(exist_ok=True)
        os.system(sox_string)

        return output_path

    return make_search_audio
