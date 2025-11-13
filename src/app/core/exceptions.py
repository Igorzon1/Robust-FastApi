from fastapi import HTTPException

class ExternalServiceError(HTTPException):
    def __init__(self, detail="External service error", status_code=502):
        super().__init__(status_code=status_code, detail=detail)
