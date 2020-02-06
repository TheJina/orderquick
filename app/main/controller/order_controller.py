from flask import request
from flask_restx import Resource
from ..marshall.dto import OrderDto, OrderItemDto
from ..service.order_service import save_new_order, get_all_orders, get_all_vendor_orders,get_all_customer_orders, get_a_order, update_order, delete_a_order
from ..service.order_item_service import save_bulk_order_item

api = OrderDto.api
addorder = OrderDto.addorder
order = OrderDto.order
addorder_item = OrderDto.addorder_item



@api.route('/')
class OrderList(Resource):
    @api.doc('list_of_registered_orders',params={'vendor_id':'Provide Vendor Id','customer_id':'Provide Customer Id'})
    @api.marshal_list_with(order, envelope='data')
    def get(self):
        """List all registered orders"""
        vendor_id = request.args.get('vendor_id')
        customer_id = request.args.get('customer_id')
        if vendor_id:
            return get_all_vendor_orders(vendor_id)
        if customer_id:
            return get_all_customer_orders(customer_id)
        return get_all_orders()

    @api.expect([addorder_item], validate=True)
    @api.doc('create a new order',params={'vendor_id':'Provide Vendor Id','customer_id':'Provide Customer Id','status':'Provide Order Status'})
    def post(self):
        """Creates a new Order """
        order = dict(
            status=request.args.get("status"),
            customer_id=request.args.get("customer_id"),
            vendor_id=request.args.get("vendor_id")
        )
        body = request.json
        order = save_new_order(data=order)
        save_bulk_order_item(id=order.id,data=body)
        return {'message':'Order Created'} , 200




@api.route('/<order_id>')
@api.param('order_id', 'The Order identifier')
@api.response(404, 'Order not found.')
class Order(Resource):
    @api.doc('get a order')
    @api.marshal_with(order)
    def get(self, order_id):
        """get a order given its identifier"""
        order = get_a_order(order_id)
        if not order:
            api.abort(404)
        else:
            return order

    @api.expect(addorder, validate=True)
    @api.marshal_with(order)
    @api.doc('update a new order')
    def put(self,order_id):
        """Updates a new Order """
        data = request.json
        order = update_order(data=data,id=order_id)
        if not order:
            api.abort(404)
        else:
            return order

    
    @api.doc('delete a new order')
    @api.marshal_with(order)
    def delete(self,order_id):
        """Deletes a new Order """
        order = delete_a_order(id=order_id)
        if not order:
            api.abort(404)
        else:
            return order


