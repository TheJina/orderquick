from app.main import db
from app.main.model.order import Order


def save_new_order(data):
    new_order = Order(
        status=data['status'],
        customer_id = data['customer_id'],
        vendor_id=data['vendor_id'],
    )
    save_changes(new_order)
    return new_order
    

def update_order(data,id):
    order = Order.query.filter_by(id=id).first()
    if order:
        order.status=data['status'],
        order.customer_id = data['customer_id'],
        order.vendor_id=data['vendor_id'],
        update_changes()
        return order

def get_all_orders():
    return Order.query.all()

def get_all_vendor_orders(vendor_id):
    return Order.query.filter_by(vendor_id=vendor_id).all()

def get_all_customer_orders(customer_id):
    return Order.query.filter_by(customer_id=customer_id).all()

def get_a_order(id):
    return Order.query.filter_by(id=id).first()

def delete_a_order(id):
    order= Order.query.filter_by(id=id).first()
    if order:
        delete_changes(order)
    return order

def update_changes():
    db.session.commit()

def delete_changes(data):
    db.session.delete(data)
    db.session.commit()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
