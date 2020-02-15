from app.main import db
from app.main.model.vendor import Vendor
from sqlalchemy import func


def save_new_vendor(data):
    vendor = Vendor.query.filter_by(contact=data['contact']).first()
    if not vendor:
        new_vendor = Vendor(
            name=data['name'],
            fuid_email=data['fuid_email'],
            fuid_phone = data['fuid_phone'],
            contact=data['contact'],
            address=data['address'],
            longitude=data['longitude'],
            latitude=data['latitude'],
            geo = 'POINT({} {})'.format(data['longitude'],data['latitude']),
            url=data['url'],
            desc=data['desc'],
            location=data['location'],
        )
        save_changes(new_vendor)
        return new_vendor
    else:
        response_object = {
            'status': 'fail',
            'message': 'Vendor already exists. Please Log in.',
        }
        return response_object, 409

def update_vendor(data,id):
    vendor = Vendor.query.filter_by(id=id).first()
    if vendor:
        vendor.name=data['name']
        vendor.contact=data['contact']
        vendor.address=data['address']
        vendor.longitude=data['longitude']
        vendor.latitude=data['latitude']
        vendor.geo = 'POINT({} {})'.format(data['longitude'],data['latitude'])
        vendor.url=data['url']
        vendor.desc=data['desc']
        vendor.location=data['location']
        update_changes()
        return vendor


def get_all_vendors():
    return Vendor.query.all()

def get_all_vendors_within_radius(geo,radius):
    print(geo)
    return Vendor.query.filter(func.ST_DistanceSphere(Vendor.geo,geo) < radius).all()


def get_a_vendor(id):
    return Vendor.query.filter_by(id=id).first()

def update_changes():
    db.session.commit()

def delete_changes(data):
    db.session.delete(data)
    db.session.commit()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
