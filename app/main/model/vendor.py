from .. import db
from sqlalchemy.sql import func
from geoalchemy2.types import Geometry
class Vendor(db.Model):
    """ Vendor Model for storing vendor related details """
    __tablename__ = "vendor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    fuid_email = db.Column(db.String(36),nullable=False,unique=True)
    fuid_phone = db.Column(db.String(36),nullable=False,unique=True)
    contact = db.Column(db.String(50),unique=True,nullable=False)
    address = db.Column(db.String(256))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    geo = db.Column(Geometry(geometry_type="POINT"))
    url = db.Column(db.String(1024),default="https://cdn.hasselblad.com/hasselblad-com/6cb604081ef3086569319ddb5adcae66298a28c5_x1d-ii-sample-01-web.jpg?auto=format&q=97")
    desc = db.Column(db.String(512))
    location = db.Column(db.String(256))
    products = db.relationship('ProductItem',backref="vendor")
    registered_on = db.Column(db.DateTime,server_default=func.now())
    updated_on = db.Column(db.DateTime,server_default=None,onupdate=func.now())
    vendor_orders=db.relationship('Order',back_populates="vendor")

    def __repr__(self):
        return "<Vendor '{}'>".format(self.name)