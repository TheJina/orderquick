from app.main import db
from app.main.model.order_item import OrderItem
from app.main.model.product_item import ProductItem

def save_new_order_item(id,data):
    new_order_item = OrderItem(
        order_id = id,
        product_item_id=data['product_item_id'],
        quantity=data['quantity'],
    )
    return new_order_item

def save_bulk_order_item(id,data):
    order_item_list = []
    for i in data:
        order_item_list.append(save_new_order_item(id,i))
    save_bulk_changes(order_item_list)
    return True


def get_all_order_items():
    return OrderItem.query.all()

def get_all_order_order_items(order_id):
    response = db.session.query(OrderItem,ProductItem).filter_by(order_id=order_id).join(ProductItem,ProductItem.id == OrderItem.product_item_id).all()
    def get_tuple(entity_tuple):
        return dict(
            id=entity_tuple.OrderItem.id,
            order_id=entity_tuple.OrderItem.order_id,
            product_item_id=entity_tuple.OrderItem.product_item_id,
            quantity=entity_tuple.OrderItem.quantity,
            name=entity_tuple.ProductItem.name,
            description=entity_tuple.ProductItem.description,
            price=entity_tuple.ProductItem.price,
            available=entity_tuple.ProductItem.available,
            vendor_id=entity_tuple.ProductItem.vendor_id,
        )

   
    return list(map(get_tuple,response))

def get_a_order_item(id):
    return OrderItem.query.filter_by(id=id).first()

def update_changes():
    db.session.commit()

def delete_changes(data):
    db.session.delete(data)
    db.session.commit()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def save_bulk_changes(data):
    db.session.add_all(data)
    db.session.commit()