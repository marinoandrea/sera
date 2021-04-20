from dataclasses import dataclass

from .entity import Entity


@dataclass
class Offering(Entity):
    user_account_id: str
    category: str
    subcategory: str
    quantity_kg: float
    price_per_kg_cfa_cents: int
    audio_asset: str
