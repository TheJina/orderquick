from .. import db
from sqlalchemy.sql import func

class Order(db.Model):
    """ Order Model for storing order related details """
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(16),default="CREATE",nullable=False)
    created_at = db.Column(db.DateTime,server_default=func.now())
    updated_at = db.Column(db.DateTime,server_default=None,onupdate=func.now())
    customer_id = db.Column(db.Integer,db.ForeignKey("customer.id"))
    vendor_id = db.Column(db.Integer,db.ForeignKey("vendor.id"))
    customer = db.relationship("Customer",back_populates="customer_orders")
    vendor = db.relationship("Vendor",back_populates="vendor_orders")
    order_items = db.relationship("OrderItem",back_populates="order")



    def __repr__(self):
        return "<Order '{}'>".format(self.name)