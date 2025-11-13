# src/app/api/users.py
from fastapi import APIRouter, HTTPException, status
from ..models.schemas import UserCreate
from ..core import db as db_core   # <- importa o módulo, não a variável
import logging

router = APIRouter(prefix="/users", tags=["Users"])
log = logging.getLogger("robust.users")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """
    Cria um novo usuário no banco MongoDB.
    Se o email já existir, retorna 409.
    """
    # pega a instância atual do db no momento da requisição
    db = getattr(db_core, "db", None)
    if db is None:
        log.error("DB not configured")
        raise HTTPException(status_code=500, detail="Database not configured")

    users_coll = db.get_collection("users")

    # checar duplicidade
    exists = await users_coll.find_one({"email": user.email})
    if exists:
        log.warning("Attempt to create duplicate user", extra={"email": user.email})
        raise HTTPException(status_code=409, detail="Email already registered")

    try:
        result = await users_coll.insert_one({"name": user.name, "email": user.email})
        log.info("User created", extra={"email": user.email, "id": str(result.inserted_id)})
        return {
            "status": "created",
            "user": {"id": str(result.inserted_id), "name": user.name, "email": user.email},
        }
    except Exception as e:
        log.exception("Failed to insert user", exc_info=True)
        raise HTTPException(status_code=500, detail="Database insert error")

@router.get("/", status_code=status.HTTP_200_OK)
async def list_users():
    """Lista todos os usuários cadastrados."""
    db = getattr(db_core, "db", None)
    if db is None:
        raise HTTPException(status_code=500, detail="Database not configured")
    users_coll = db.get_collection("users")
    users = await users_coll.find({}, {"_id": 0}).to_list(length=100)
    return {"count": len(users), "users": users}
