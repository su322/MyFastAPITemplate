from fastapi import APIRouter
from app.service import item_service
from app.schemas.item_schema import ItemCreateSchema, ItemReadSchema
from app.common.response import success, error
from typing import List

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
async def get_items_api():
    data = item_service.get_items()
    return success(data=data)

@router.get("/{item_id}")
async def get_item_api(item_id: int):
    item = item_service.get_item(item_id)
    if item:
        return success(data=item)
    return error(code=404, msg="Item not found")

@router.post("/")
async def create_item_api(item: ItemCreateSchema):
    new_item = item_service.create_item(item)
    return success(data=new_item)

@router.put("/{item_id}")
async def update_item_api(item_id: int, item: ItemCreateSchema):
    updated = item_service.update_item(item_id, item)
    if updated:
        return success(data=updated)
    return error(code=404, msg="Item not found")

@router.delete("/{item_id}")
async def delete_item_api(item_id: int):
    deleted = item_service.delete_item(item_id)
    if deleted:
        return success(data=deleted)
    return error(code=404, msg="Item not found")
