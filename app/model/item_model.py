from pydantic import BaseModel

class ItemModel(BaseModel):
    id: int
    name: str
