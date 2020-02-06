from .. import db
from sqlalchemy.sql import func
from geoalchemy2 import Geometry

class Customer(db.Model):
    """ Customer Model for storing user related details """
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fuid_email = db.Column(db.String(36),nullable=False,unique=True)
    fuid_phone = db.Column(db.String(36),nullable=False,unique=True)
    name = db.Column(db.String(50))
    contact = db.Column(db.String(50),unique=True)
    address = db.Column(db.String(256))
    registered_on = db.Column(db.DateTime,server_default=func.now())
    updated_on = db.Column(db.DateTime,server_default=None,onupdate=func.now())
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    location = db.Column(db.String(256))
    url = db.Column(db.String(1024),default="https://cdn.hasselblad.com/hasselblad-com/6cb604081ef3086569319ddb5adcae66298a28c5_x1d-ii-sample-01-web.jpg?auto=format&q=97")
    geo = db.Column(Geometry(geometry_type="POINT"))
    customer_orders=db.relationship("Order",back_populates="customer")

    def __repr__(self):
        return "<User '{}'>".format(self.name)