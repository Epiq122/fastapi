from typing import Any


text: str = "Value"
age: int = 55
temp: float = 22

number: int | float = 12

optional: str | None

optional = "check it"


def root(num: int, float, exp: float | None) -> float:
    return pow(num, 0.5 if exp is None else exp)


# root_35: float = root(35)
# root_35.conjugate
# root_35 = root("melia")
# print(root_35)

digits: list[int] = [1, 2, 3, 4, 5]
table_5: tuple[int, ...] = (5, 10, 15, 20, 25)

city_temp: tuple[str, float | int] = ("city", 10.2)

shipment: dict[str, str | int | float] = {
    "id": 1016789,
    "weight": 1.24,
    "content": "sch 40 pvc",
    "status": "shipped",
}
