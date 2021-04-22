from typing import Callable, Optional

from src.entities import Offering, User
from src.errors import ValidationError


def build_upload_offering(
    create_offering: Callable[[Offering], None],
    retrieve_user_by_phone: Callable[[str], Optional[User]]
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
        return offering

    return upload_offering
