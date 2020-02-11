from app.main import db
from app.main.model.order_item import OrderItem
from app.main.model.product_item import ProductItem
from app.main.model.vendor import Vendor
from app.main.model.order import Order
from app.main.service.order_service import get_all_customer_orders
from sqlalchemy import desc


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

def get_all_order_order_items(customer_id):          
    response = [dict(
            orderId=o.id,
            vendorId=v.id,
            vendorName=v.name,
            orderedAt=o.created_at,
            orderStatus=o.status,
            totalPrice=0,
            items=[ dict(itemName=p.product_item.name,
                         itemQty=p.quantity,
                         itemDesc=p.product_item.desc,
                         itemPrice=p.product_item.price
                         ) for p in o.order_items])
                               for o , v in db.session.query(Order,Vendor).filter(Order.vendor_id == Vendor.id , Order.customer_id == customer_id).order_by(desc(Order.created_at)).all() ]
    
    
    return response

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