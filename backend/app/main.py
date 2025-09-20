from fastapi import FastAPI

app = FastAPI()


@app.get("/shipment")
def get_shipment():
    return {"content": "sch40 pvc", "status": "in transit"}
