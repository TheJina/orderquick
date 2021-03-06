from flask_restx import Namespace, fields


class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    addcustomer = api.model('addcustomer', {
    'name': fields.String(required=True, description='The customer name '),
    'fuid_email': fields.String(required=True, description='The customer fuid_email '),
    'fuid_phone':fields.String(required=True,description="The customer fuid_phone"),
    'contact': fields.String(required=True, description='The customer contact'),
	'address': fields.String(required=True, description='The customer address'),
    'longitude': fields.Float(required=True,description='The customer longitude'),
    'latitude':fields.Float(required=True,desscription="The customer latitude"),
    'url': fields.String(required=True, description='The vendor url'),
    'location': fields.String(required=True, description='The customer location '),
    })

    customer = api.model('customer', {
    'id':fields.Integer(description="The customer uuid"),
    'name': fields.String(required=True, description='The customer name '),
    'fuid_email': fields.String(required=True, description='The customer fuid_email '),
    'fuid_phone':fields.String(required=True,description="The customer fuid_phone"),
    'contact': fields.String(required=True, description='The customer contact'),
	'address': fields.String(required=True, description='The customer address'),
    'longitude': fields.Float(required=True,description='The customer longitude'),
    'latitude':fields.Float(required=True,desscription="The customer latitude"),
    'url': fields.String(required=True, description='The vendor url'),
    'location': fields.String(required=True, description='The customer location '),
    })

class VendorDto:
    api = Namespace('vendor', description='vendor related operations')
    addvendor = api.model('addvendor', {
    'name': fields.String(required=True, description='The vendor name '),
    'fuid_email': fields.String(required=True, description='The vendor fuid_email '),
    'fuid_phone':fields.String(required=True,description="The vendor fuid_phone"),
    'contact': fields.String(required=True, description='The vendor contact'),
	'address': fields.String(required=True, description='The vendor address'),
    'longitude': fields.Float(required=True,description='The vendor longitude'),
    'latitude':fields.Float(required=True,description="The vendor latitude"),
    'url': fields.String(required=True, description='The vendor url'),
    'desc': fields.String(required=True, description='The vendor desc'),
    'location': fields.String(required=True, description='The vendor location'),
    })

    vendor = api.model('vendor', {
    'id':fields.Integer(description="The vendor uuid"),
    'name': fields.String(required=True, description='The vendor name '),
    'contact': fields.String(required=True, description='The vendor contact'),
	'address': fields.String(required=True, description='The vendor address'),
    'longitude': fields.Float(required=True,description='The vendor longitude'),
    'latitude':fields.Float(required=True,description="The vendor latitude"),
    'url': fields.String(required=True, description='The vendor url'),
    'desc': fields.String(required=True, description='The vendor desc'),
    'location': fields.String(required=True, description='The vendor location'),
    })

class ProductItemDto:
    api = Namespace('product_item', description='product_item related operations')
    addproduct_item = api.model('addproduct_item', {
    'name': fields.String(required=True, description='The product_item name '),
    'desc': fields.String(required=True, description='The product_item description'),
    'price': fields.Float(required=True,description='The product_item price'),
    'url': fields.String(required=True, description='The vendor url'),
    'available': fields.Boolean(required=True,description="The product_item available"),
    'vendorId':fields.Integer(required=True,desscription="The product_item vendor_id"),
    })

    product_item = api.model('product_item', {
    'id':fields.Integer(description="The product_item uuid"),
    'name': fields.String(required=True, description='The product_item name '),
    'desc': fields.String(required=True, description='The product_item description'),
    'price': fields.Float(required=True,description='The product_item price'),
    'url': fields.String(required=True, description='The vendor url'),
    'available': fields.Boolean(required=True,description="The product_item available"),
    'created_at':fields.DateTime(required=True,description="The product_item creation date"),
    'vendorId':fields.Integer(required=True,desscription="The product_item vendor_id"),
    })

class OrderDto:
    api = Namespace('order', description='order related operations')
    addorder = api.model('addorder', {
    'status': fields.String(required=True, description='The order name '),
    'customer_id':fields.Integer(required=True,desscription="The order customer_id"),
    'vendor_id':fields.Integer(required=True,desscription="The order vendor_id"),
    })

    order = api.model('order', {
    'id':fields.Integer(description="The order uuid"),
    'status': fields.String(required=True, description='The order name '),
    'customer_id':fields.Integer(required=True,desscription="The order customer_id"),
    'vendor_id':fields.Integer(required=True,desscription="The order vendor_id"),
    })

    addorder_item = api.model('order', {
    'product_item_id':fields.Integer(required=True,desscription="The order_item product_item_id"),
    'quantity': fields.Integer(required=True, description='The order_item quantity '),
    })


class OrderItemDto:
    api = Namespace('order_item', description='order_item related operations')

    add_order_item = api.model('order_item', {
    'itemName':fields.String(required=True,desscription="The order_item product_item_id"),
    'itemQty': fields.Integer(required=True, description='The order_item quantity '),
    'itemDesc':fields.String(required=True,description="The order_item description"),
    'itemPrice':fields.Integer(required=True,description="The order_item price"),
    })
    
    order_history = api.model('order_history', {
    'orderId':fields.Integer(required=True,description="The order_item order_id"),
    'vendorId':fields.String(required=True,description="The order_item vendor_id"),
    'vendorName':fields.String(required=True,description="The vendor_name"),
    'orderedAt':fields.DateTime(required=True,description="The vendor_name"),
    'orderStatus':fields.String(required=True,description="The order status"),
    'totalPrice':fields.Float(required=True,description="The total price"),
    "items": fields.List(fields.Nested(add_order_item)),  
    })

    vendor_order_history = api.model('vendor_order_history', {
    'orderId':fields.Integer(required=True,description="The order_item order_id"),
    'userId':fields.String(required=True,description="The order_item customer_id"),
    'userName':fields.String(required=True,description="The customer_name"),
    'orderedAt':fields.DateTime(required=True,description="The vendor_name"),
    'orderStatus':fields.String(required=True,description="The order status"),
    'address':fields.String(required=True,description="The customer address"),
    'contact':fields.String(required=True,description="The customer contact"),
    'latitude':fields.Float(required=True),
    'longitude':fields.Float(required=True),
    "items": fields.List(fields.Nested(add_order_item)),  
    })

class FCMTokenDto:
    api = Namespace('fcm_token',description='Fcm token related operations')

    fcm_token = api.model('fcm_token',{
        'token': fields.String(required=True,description="The FCM token")
    })


