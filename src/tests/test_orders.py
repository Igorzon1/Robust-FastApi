import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_order_success(monkeypatch):
    async def fake_charge(payload):
        return {"id":"ok"}
    monkeypatch.setattr("app.services.payment_client.charge_card", fake_charge)

    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/orders/", json={"user_id":1, "amount":100.0})
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"
