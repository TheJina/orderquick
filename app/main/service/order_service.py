from app.main import db
from app.main.model.order import Order
from app.main.model.customer import Customer
from app.main.model.vendor import Vendor
from sqlalchemy import desc
from app.main import redis_client
from pyfcm import FCMNotification
import os
push_service = FCMNotification(api_key=os.environ['FIREBASE_API_KEY'])

def save_new_order(data):
    new_order = Order(
        status=data['status'],
        customer_id = data['customer_id'],
        vendor_id=data['vendor_id'],
    )
    save_changes(new_order)
    vendor_data = Vendor.query.filter_by(id=data['vendor_id']).first()
    registration_id=redis_client.get(vendor_data.fuid_phone)
    if registration_id is None:
        registration_id=redis_client.get(vendor_data.fuid_email)
    message_title = "Order No. "+ str(new_order.id)
    message_body = "Hi, You have a new Order"
    push_service.notify_single_device(registration_id=registration_id.decode('utf-8'), message_title=message_title, message_body=message_body)

    return new_order
    

def update_order(data,id):
    order = Order.query.filter_by(id=id).first()
    if order:
        order.status=data['status']
        order.customer_id = data['customer_id']
        order.vendor_id=data['vendor_id']
        update_changes()
        customer_data = Customer.query.filter_by(id=data['customer_id']).first()
        registration_id=redis_client.get(customer_data.fuid_phone)
        if registration_id is None:
            registration_id=redis_client.get(customer_data.fuid_email)
        message_title = "Order No. "+id
        message_body = "Hi, Your Order is  "+data['status']
        push_service.notify_single_device(registration_id=registration_id.decode('utf-8'), message_title=message_title, message_body=message_body)

        return order

def get_all_orders():
    return Order.query.all()

def get_all_vendor_orders(vendor_id):
    return Order.query.filter_by(vendor_id=vendor_id).order_by(desc(Order.created_at)).all()

def get_all_customer_orders(customer_id):
    return Order.query.filter_by(customer_id=customer_id).order_by(desc(Order.created_at)).all()

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
