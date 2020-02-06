from .. import db
from sqlalchemy.sql import func

class ProductItem(db.Model):
    """ Product Model for storing product related details """
    __tablename__ = "product_item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(512),default=None)
    price = db.Column(db.Float,default=0.0,nullable=False)
    available = db.Column(db.Boolean,default=True)
    created_at = db.Column(db.DateTime,server_default=func.now())
    updated_at = db.Column(db.DateTime,server_default=None,onupdate=func.now())
    vendor_id = db.Column(db.Integer,db.ForeignKey("vendor.id"))
    product_order_items = db.relationship("OrderItem",back_populates="product_item")


    def __repr__(self):
        return "<ProductItem '{}'>".format(self.name)