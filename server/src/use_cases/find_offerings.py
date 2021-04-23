from typing import Callable, List, Tuple

from src.entities import Offering, User

from .utils import check_permission


def build_find_offerings(
    retrieve_offerings: Callable[[dict], List[Offering]],
    retrieve_users_by_id: Callable[[List[str]], List[User]]
) -> Callable[[str, str, str, float, float],
              Tuple[List[User], List[Offering]]]:

    @check_permission(login_only=True)
    def find_offerings(
        category: str,
        subcategory: str,
        min_quantity: float = 0.0,
        max_quantity: float = 9999.0
    ) -> Tuple[List[User], List[Offering]]:
        offerings = retrieve_offerings({
            'category': category,
            'subcategory': subcategory,
            'min_quantity': min_quantity,
            'max_quantity': max_quantity
        })

        users = retrieve_users_by_id(
            list(map(lambda x: x.id, offerings))
        )

        return users, offerings

    return find_offerings  # type: ignore
