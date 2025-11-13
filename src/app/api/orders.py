# src/app/api/orders.py
from fastapi import APIRouter, HTTPException, status
from ..models.schemas import OrderCreate
from ..core import db as db_core
from ..services.payment_client import charge_card
import logging

router = APIRouter(prefix="/orders", tags=["Orders"])
log = logging.getLogger("robust.orders")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    """
    Cria um pedido e tenta processar o pagamento via API externa simulada.
    """
    db = getattr(db_core, "db", None)
    if db is None:
        raise HTTPException(status_code=500, detail="Database not configured")

    orders_coll = db.get_collection("orders")

    try:
        # simula chamada de pagamento externo
        payment_response = await charge_card(order.user_id, order.amount)
        if not payment_response.get("success"):
            log.warning("Payment failed", extra={"user_id": order.user_id})
            raise HTTPException(status_code=400, detail="Payment failed")

        # salvar pedido no banco
        doc = {
            "user_id": order.user_id,
            "amount": order.amount,
            "status": "paid",
            "external_ref": payment_response.get("ref"),
        }
        result = await orders_coll.insert_one(doc)
        log.info("Order created", extra={"order_id": str(result.inserted_id)})
        return {"status": "created", "order_id": str(result.inserted_id)}

    except HTTPException:
        raise
    except Exception as e:
        log.exception("Error creating order", exc_info=True)
        raise HTTPException(status_code=500, detail="Error creating order")

@router.get("/", status_code=status.HTTP_200_OK)
async def list_orders():
    db = getattr(db_core, "db", None)
    if db is None:
        raise HTTPException(status_code=500, detail="Database not configured")
    orders_coll = db.get_collection("orders")
    orders = await orders_coll.find({}, {"_id": 0}).to_list(length=100)
    return {"count": len(orders), "orders": orders}
