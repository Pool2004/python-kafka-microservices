from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Order(BaseModel):

    item_id: int 
    quantity: int 
    price: float

@app.post("/order")
def create_order(order: Order):
    return {"message": "Order created", "order": order}



@app.get("/")
def service():
    return {"message": "Api is working"}