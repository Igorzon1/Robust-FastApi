import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_user_success():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/users/", json={"name": "Igor", "email": "igor@example.com"})
        assert resp.status_code == 200 or resp.status_code == 201
        json = resp.json()
        assert json["user"]["email"] == "igor@example.com"

@pytest.mark.asyncio
async def test_create_user_duplicate():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # cria primeiro
        await ac.post("/users/", json={"name": "Igor", "email": "dup@example.com"})
        # tenta criar duplicado
        resp = await ac.post("/users/", json={"name": "Igor 2", "email": "dup@example.com"})
        assert resp.status_code == 409
