from flask import request
from flask_restx import Resource
from ..marshall.dto import OrderItemDto
from ..service.order_item_service import save_bulk_order_item , get_all_order_order_items

api = OrderItemDto.api
order_history = OrderItemDto.order_history



@api.route('/<customer_id>')
class OrderList(Resource):
    @api.doc('list_of customer orders history')
    @api.marshal_list_with(order_history, envelope='data')
    def get(self,customer_id):
        """List all registered customer orders"""
        result = get_all_order_order_items(customer_id)
        return result





