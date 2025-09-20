from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from typing import Any


app = FastAPI()

shipments = {
    1016789: {"weight": 75, "content": "a foiter", "status": "delivered"},
    7337: {"weight": 1.75, "content": "jackets", "status": "in transit"},
    987778: {"weight": 2375, "content": "propeller", "status": "delayed"},
    10078: {"weight": 2.25, "content": "air", "status": "delivered"},
    987111: {"weight": 0.5, "content": "screws", "status": "delivered"},
    234567: {"weight": 15.2, "content": "motor", "status": "in transit"},
    445566: {"weight": 8.75, "content": "cables", "status": "delayed"},
    778899: {"weight": 120.0, "content": "steel beams", "status": "delivered"},
    334455: {"weight": 3.25, "content": "electronics", "status": "in transit"},
    667788: {"weight": 45.5, "content": "plastic parts", "status": "delayed"},
    112233: {"weight": 0.25, "content": "bolts", "status": "delivered"},
}


@app.get("/shipment")
def get_shipment(id: int) -> dict[str, Any]:
    if id in shipments:
        return shipments[id]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given id does not exist"
        )


@app.post("/shipment")
def submit_shipment(content: str, weight: float) -> dict[str, int]:
    if weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Maximum weight limit is 25kg",
        )

    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {"content": content, "weight": weight, "status": "placed"}
    return {"id": new_id}


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API")
