import httpx
import random
import logging
from ..core.config import settings

log = logging.getLogger("robust.payment")

async def charge_card(user_id: str, amount: float):
    """
    Simula o processamento de pagamento com API externa.
    Pode falhar aleatoriamente para testar o tratamento de erros.
    """
    try:
        # simula 20% de chance de falha
        if random.random() < 0.2:
            raise Exception("Simulated payment failure")

        # simula resposta de sucesso
        fake_ref = f"PAY-{random.randint(10000,99999)}"
        log.info("Payment success", extra={"user_id": user_id, "amount": amount})
        return {"success": True, "ref": fake_ref}
    except Exception as e:
        log.warning("Payment API error", exc_info=True)
        return {"success": False, "error": str(e)}
