# src/app/api/uploads.py
from fastapi import APIRouter, UploadFile, File, HTTPException, status
import aiofiles
import os
import logging

router = APIRouter(prefix="/upload", tags=["Uploads"])
log = logging.getLogger("robust.uploads")

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...)):
    """
    Faz upload de um arquivo e salva localmente.
    """
    try:
        filepath = os.path.join(UPLOAD_DIR, file.filename)
        async with aiofiles.open(filepath, "wb") as f:
            content = await file.read()
            await f.write(content)
        log.info("File uploaded", extra={"filename": file.filename})
        return {"status": "uploaded", "filename": file.filename}
    except Exception as e:
        log.exception("File upload failed", exc_info=True)
        raise HTTPException(status_code=500, detail="File upload failed")
