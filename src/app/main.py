from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .api import users, orders, uploads
from .core.logger import logger
from .core.monitor import alert_critical
from .core import db as core_db  # ✅ importando o módulo inteiro

app = FastAPI(title="RobustFastAPI")

# registrando routers
app.include_router(users.router)
app.include_router(orders.router)
app.include_router(uploads.router)

# eventos de lifecycle: startup / shutdown
@app.on_event("startup")
async def on_startup():
    core_db.connect()  # ✅ acessando via módulo
    logger.info("Application startup complete")

@app.on_event("shutdown")
async def on_shutdown():
    core_db.close()  # ✅ acessando via módulo
    logger.info("Application shutdown complete")

# handler global para exceções não tratadas
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception", exc_info=True, extra={"path": request.url.path})
    try:
        alert_critical(exc, {"path": str(request.url), "method": request.method})
    except Exception:
        logger.exception("Failed to send alert in exception handler")
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})

# health check
@app.get("/health")
async def health():
    try:
        if core_db.db is None:  # ✅ agora acessa o db atualizado
            return {"status": "ok", "db": "not configured"}
        try:
            await core_db.db.command("ping")
            return {"status": "ok", "db": "connected"}
        except Exception as e:
            logger.warning("Health check: DB ping failed", exc_info=True)
            return JSONResponse(status_code=503, content={"status": "degraded", "db_error": str(e)})
    except Exception as e:
        logger.warning("Health check degraded", exc_info=True)
        return JSONResponse(status_code=503, content={"status": "degraded", "error": str(e)})
