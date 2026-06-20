import asyncpg
from pydantic import BaseModel
from fastapi import FastAPI


class File(BaseModel):
    file_id: int
    file_size: int  # In MB
    file_hash: str
    file_name: str
    file_ext: str  # Will be used in future for sorting


#  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


class FileChunks(BaseModel):
    file_id: int
    chunk_index: int
    chunk_hash: str
    chunk_size: int  # PostgreSQL analogue: BIGINT


#  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


client = FastAPI()


@client.get(path="/files-list")
def get_files_list():
    return {"hello": "here's empty for now"}
