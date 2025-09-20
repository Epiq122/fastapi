from typing import Any, Callable

routes: dict[str, Callable[[Any], Any]] = {}


def route(path: str):
    def register_route(func):
        routes[path] = func

    return register_route


@route("/shipment")
def get_shipment():
    return "Shipment<1001, in transit>"
