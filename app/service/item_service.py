from app.model.item_model import ItemModel
from app.schemas.item_schema import ItemCreateSchema

# 用于模拟数据库的内存数据
_fake_db = [
    ItemModel(id=1, name="item1"),
    ItemModel(id=2, name="item2")
]

def get_items():
    return _fake_db

def get_item(item_id: int):
    for item in _fake_db:
        if item.id == item_id:
            return item
    return None

def create_item(item: ItemCreateSchema):
    new_id = max([item.id for item in _fake_db], default=0) + 1
    item_obj = ItemModel(id=new_id, name=item.name)
    _fake_db.append(item_obj)
    return item_obj

def update_item(item_id: int, item: ItemCreateSchema):
    for idx, old_item in enumerate(_fake_db):
        if old_item.id == item_id:
            updated_item = ItemModel(id=item_id, name=item.name)
            _fake_db[idx] = updated_item
            return updated_item
    return None

def delete_item(item_id: int):
    for idx, item in enumerate(_fake_db):
        if item.id == item_id:
            return _fake_db.pop(idx)
    return None
