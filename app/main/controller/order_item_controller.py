from flask import request
from flask_restx import Resource
from ..marshall.dto import OrderItemDto
from ..service.order_item_service import save_bulk_order_item , get_all_order_order_items

api = OrderItemDto.api
order_item = OrderItemDto.order_item



@api.route('/<order_id>')
class OrderList(Resource):
    @api.doc('list_of_order_items filtered by order_id')
    @api.marshal_list_with(order_item, envelope='data')
    def get(self,order_id):
        """List all registered order items"""
        result = get_all_order_order_items(order_id)
        return result





