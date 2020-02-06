from app.main import db
from app.main.model.product_item import ProductItem


def save_new_product_item(data):
    new_product_item = ProductItem(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        available=data['available'],
        vendor_id=data['vendor_id'],
    )
    save_changes(new_product_item)
    return new_product_item
    

def update_product_item(data,id):
    product_item = ProductItem.query.filter_by(id=id).first()
    if product_item:
        product_item.name=data['name'],
        product_item.description=data['description'],
        product_item.price=data['price'],
        product_item.available=data['available'],
        product_item.vendor_id=data['vendor_id'],
        update_changes()
        return product_item

def delete_a_product_item(id):
    product_item= ProductItem.query.filter_by(id=id).first()
    if product_item:
        delete_changes(product_item)
    return product_item



def get_all_product_items():
    return ProductItem.query.all()

def get_all_vendor_product_items(vendor_id):
    return ProductItem.query.filter_by(vendor_id=vendor_id).all()

def get_a_product_item(id):
    return ProductItem.query.filter_by(id=id).first()

def update_changes():
    db.session.commit()

def delete_changes(data):
    db.session.delete(data)
    db.session.commit()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
