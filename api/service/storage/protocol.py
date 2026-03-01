from abc import ABC, abstractmethod
from api.schemas.media import MediaUploadResult

class StorageProtocol(ABC):
    @abstractmethod
    async def upload(self, file: str) -> MediaUploadResult: ...

    @abstractmethod
    async def delete(self, file_id: str) -> bool: ...

    @abstractmethod
    async def get_url(self) -> str: ...
