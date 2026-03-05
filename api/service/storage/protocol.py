from abc import ABC, abstractmethod
from typing import BinaryIO

class StorageProtocol(ABC):
    @abstractmethod
    async def save(self, file: BinaryIO, filename: str) -> str:
        """
        Save media and return filepath/url to file

        """

    @abstractmethod
    async def delete(self, path: str) -> None: ...
    #
    # @abstractmethod
    # async def get_url(self, file_id: str) -> str: ...
