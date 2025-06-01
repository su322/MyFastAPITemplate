from pydantic import BaseModel

class ItemCreateSchema(BaseModel):
    name: str

class ItemReadSchema(BaseModel):
    id: int
    name: str
