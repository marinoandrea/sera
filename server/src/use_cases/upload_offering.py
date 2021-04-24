import os
import pathlib
from time import time
from typing import Callable, Optional

from gtts import gTTS
from src.entities import Offering, OfferingAudio, User
from src.errors import ValidationError
from src.plugins.interfaces import FileManager


def build_upload_offering(
    create_offering: Callable[[Offering], None],
    create_offering_audio: Callable[[OfferingAudio], None],
    retrieve_user_by_phone: Callable[[str], Optional[User]],
    file_manager: FileManager
) -> Callable[[str, str, str, float, int], Offering]:

    def upload_offering(
        phone_number: str,
        category: str,
        subcategory: str,
        quantity: float,
        price: int
    ) -> Offering:
        user = retrieve_user_by_phone(phone_number)
        if user is None:
            raise ValidationError("This number is not authorized.")

        offering = Offering(
            user_account_id=user.id,
            category=category,
            subcategory=subcategory,
            quantity_kg=quantity,
            # conversion to cents
            price_per_kg_cfa_cents=int(float(price) * 100)
        )
        create_offering(offering)

        for lang in ['en', 'fr']:
            temp_mp3 = f'temp_{int(time())}.mp3'
            temp_wav = f'temp_{int(time())}.wav'

            audio = gTTS(build_info_string(offering, user, lang), lang=lang)
            audio.save(temp_mp3)

            sox_string = 'sox -b 16 -c 1 -e signed-integer '
            sox_string += temp_mp3
            sox_string += f' {temp_wav} rate 8k'

            pathlib.Path(temp_wav).touch(exist_ok=True)
            os.system(sox_string)
            os.remove(temp_mp3)

            offering_audio = OfferingAudio(
                offering_id=offering.id,
                lang=lang,
                path=file_manager.store_file(temp_wav)
            )
            create_offering_audio(offering_audio)

            os.remove(temp_wav)

        return offering

    def build_info_string(offering: Offering, user: User, lang: str) -> str:
        return {
            'en': build_en_info_string(offering, user),
            'fr': build_fr_info_string(offering, user)
        }[lang]

    def build_en_info_string(offering: Offering, user: User) -> str:
        out = f'The seller: {user.name} '
        out += f'is offering {offering.quantity_kg} kilos '
        out += f'of {offering.category} {offering.subcategory} '
        out += f'for {offering.price_per_kg_cfa_cents} C F A per kilo'
        return out

    def build_fr_info_string(offering: Offering, user: User) -> str:
        out = f'Le vendeur: {user.name} '
        out += f'offre {offering.quantity_kg} kilos '
        out += f'de {offering.category} {offering.subcategory} '
        out += f'pour {offering.price_per_kg_cfa_cents} C F A par kilogramme'
        return out

    return upload_offering
