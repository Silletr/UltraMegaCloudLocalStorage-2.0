import asyncpg
from pydantic import BaseModel


class File(BaseModel):
    file_name: str
    file_ext: str  # Will be used in future for sorting
    file_id: int
    file_size: int  # In MB
    file_hash: str


class FileChunks(BaseModel):
    file_id: int
    chunk_index: int
    chunk_hash: int
    chunk_size: int
