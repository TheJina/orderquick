from .. import db
from sqlalchemy.sql import func

class OrderItem(db.Model):
    """ OrderItem Model for storing order_itemrelated details """
    __tablename__ = "order_item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer,db.ForeignKey("order.id"))
    product_item_id = db.Column(db.Integer,db.ForeignKey("product_item.id"))
    quantity = db.Column(db.Integer,server_default="0")
    created_at = db.Column(db.DateTime,server_default=func.now())
    updated_at = db.Column(db.DateTime,server_default=None,onupdate=func.now())
    order = db.relationship("Order",back_populates="order_items")
    product_item = db.relationship("ProductItem",back_populates="product_order_items")



    def __repr__(self):
        return "<OrderItem '{}'>".format(self.id)