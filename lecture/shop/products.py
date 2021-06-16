from dataclasses import dataclass
from typing import Dict, Any, List, Optional


@dataclass
class Product:
    product_id: int
    title: str
    price: float


class Products:
    _data: Dict[int, Dict[str, Any]] = {
        1: {
            'product_id': 1,
            'title': 'Product 1',
            'price': 100.0,
        },
        2: {
            'product_id': 2,
            'title': 'Product 2',
            'price': 50.0,
        },
        3: {
            'product_id': 3,
            'title': 'Product 3',
            'price': 75.0,
        },
        4: {
            'product_id': 4,
            'title': 'Product 4',
            'price': 120.0,
        },
        5: {
            'product_id': 5,
            'title': 'Product 5',
            'price': 15.0,
        },
    }

    def all(self) -> List[Product]:
        return [self._build(attributes=attributes) for _, attributes in self._data.items()]

    def by_id(self, product_id: int) -> Optional[Product]:
        product = self._data.get(product_id, None)
        return self._build(product) if product else None

    def _build(self, attributes: Dict[str, Any]) -> Product:
        return Product(**attributes)
