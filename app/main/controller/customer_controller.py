from flask import request
from flask_restx import Resource

from ..marshall.dto import CustomerDto
from ..service.customer_service import save_new_customer, get_all_customers, get_a_customer, update_customer, delete_a_customer

api = CustomerDto.api
addcustomer = CustomerDto.addcustomer
customer = CustomerDto.customer


@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_registered_customers')
    @api.marshal_list_with(customer, envelope='data')
    def get(self):
        """List all registered customers"""
        return get_all_customers()

    @api.expect(addcustomer, validate=True)
    @api.marshal_with(customer)
    @api.doc('create a new customer')
    def post(self):
        """Creates a new Customer """
        data = request.json
        print(data)
        return save_new_customer(data=data)



@api.route('/<customer_id>')
@api.param('customer_id', 'The Customer identifier')
@api.response(404, 'Customer not found.')
class Customer(Resource):
    @api.doc('get a customer')
    @api.marshal_with(customer)
    def get(self, customer_id):
        """get a customer given its identifier"""
        customer = get_a_customer(customer_id)
        if not customer:
            api.abort(404)
        else:
            return customer

    @api.expect(addcustomer, validate=True)
    @api.marshal_with(customer)
    @api.doc('update a new customer')
    def put(self,customer_id):
        """Updates a new Customer """
        data = request.json
        customer = update_customer(data=data,id=customer_id)
        if not customer:
            api.abort(404)
        else:
            return customer
    
    @api.marshal_with(customer)
    @api.doc('delete a new customer')
    def delete(self,customer_id):
        """Deletes a new Customer """
        customer = delete_a_customer(id=customer_id)
        if not customer:
            api.abort(404)
        else:
            return customer


