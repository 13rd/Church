from pathlib import Path
from typing import BinaryIO

import aiofiles

from api.service.storage.protocol import StorageProtocol


class LocalStorage(StorageProtocol):
    def __init__(self, upload_dir: str):
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    async def save(self, file: BinaryIO, filename: str) -> str:
        file_path = self.upload_dir / filename
        async with aiofiles.open(file_path, mode="wb") as f:
            content = await file.read()
            await f.write(content)

        return f"/media/{filename}"

    async def delete(self, path: str):
        file_path = self.upload_dir / path.lstrip("/")
        if file_path.exists():
            file_path.unlink()

