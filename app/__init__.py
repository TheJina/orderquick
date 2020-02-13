
from flask_restx import Api
from flask import Blueprint

from .main.controller.customer_controller import api as customer_ns
from .main.controller.vendor_controller import api as vendor_ns
from .main.controller.product_item_controller import api as product_ns
from .main.controller.order_controller import api as order_ns
from .main.controller.order_item_controller import api as order_item_ns
from .main.controller.fcm_token_controller import api as fcm_token_ns
from .main.controller.image_controller import api as image_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='ORDER QUICK',
          version='1.0',
          description='a order quick service'
          )

api.add_namespace(customer_ns, path='/customer')
api.add_namespace(vendor_ns,path='/vendor')
api.add_namespace(product_ns,path='/product')
api.add_namespace(order_ns,path='/order')
api.add_namespace(order_item_ns,path='/order_item')
api.add_namespace(fcm_token_ns,path='/fcm_token')
api.add_namespace(image_ns,path='/image')