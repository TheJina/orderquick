from app.main import db
from app.main.model.customer import Customer
from sqlalchemy import or_


def save_new_customer(data):
    customer = Customer.query.filter(or_(Customer.fuid_email==id,Customer.fuid_phone==id)).first()
    if not customer:
        new_customer = Customer(
            name=data['name'],
            fuid_email=data['fuid_email'],
            fuid_phone = data['fuid_phone'],
            contact=data['contact'],
            address=data['address'],
            longitude=data['longitude'],
            latitude=data['latitude'],
            url=data['url'],
            geo = 'POINT({} {})'.format(data['longitude'],data['latitude']),
            location=data['location']
        )
        save_changes(new_customer)
        return new_customer
    else:
        response_object = {
            'status': 'fail',
            'message': 'Customer already exists. Please Log in.',
        }
        return response_object, 409

def update_customer(data,id):
    customer = Customer.query.filter(or_(Customer.fuid_email==id,Customer.fuid_phone==id)).first()
    if customer:
        customer.name=data['name'],
        customer.contact=data['contact'],
        customer.address=data['address'],
        customer.longitude=data['longitude'],
        customer.latitude=data['latitude'],
        customer.url=data['url'],
        customer.geo = 'POINT({} {})'.format(data['longitude'],data['latitude']),
        customer.location = data['location']
        update_changes()
        return customer


def get_all_customers():
    return Customer.query.all()

def delete_a_customer(id):
    data = Customer.query.filter_by(id=id).first()
    delete_changes(data)
    return data

def get_a_customer(id):
    response = Customer.query.filter(or_(Customer.fuid_email==id,Customer.fuid_phone==id)).first()
    return response

def update_changes():
    db.session.commit()

def delete_changes(data):
    db.session.delete(data)
    db.session.commit()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
