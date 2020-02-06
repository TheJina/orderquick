from flask import request
from flask_restx import Resource
from ..marshall.dto import ProductItemDto
from ..service.product_item_service import save_new_product_item, get_all_product_items, get_all_vendor_product_items, get_a_product_item, update_product_item, delete_a_product_item

api = ProductItemDto.api
addproduct_item = ProductItemDto.addproduct_item
product_item = ProductItemDto.product_item


@api.route('/')
class ProductItemList(Resource):
    @api.doc('list_of_registered_product_items',params={'vendor_id':'Provide Vendor Id'})
    @api.marshal_list_with(product_item, envelope='data')
    def get(self):
        """List all registered product_items"""
        vendor_id = request.args.get('vendor_id')
        if vendor_id:
            return get_all_vendor_product_items(vendor_id)
        return get_all_product_items()

    @api.expect(addproduct_item, validate=True)
    @api.marshal_with(product_item)
    @api.doc('create a new product_item')
    def post(self):
        """Creates a new ProductItem """
        data = request.json
        return save_new_product_item(data=data)


@api.route('/<product_item_id>')
@api.param('product_item_id', 'The ProductItem identifier')
@api.response(404, 'ProductItem not found.')
class ProductItem(Resource):
    @api.doc('get a product_item')
    @api.marshal_with(product_item)
    def get(self, product_item_id):
        """get a product_item given its identifier"""
        product_item = get_a_product_item(product_item_id)
        if not product_item:
            api.abort(404)
        else:
            return product_item

    @api.expect(addproduct_item, validate=True)
    @api.marshal_with(product_item)
    @api.doc('update a new product_item')
    def put(self,product_item_id):
        """Updates a new ProductItem """
        data = request.json
        product_item = update_product_item(data=data,id=product_item_id)
        if not product_item:
            api.abort(404)
        else:
            return product_item

    
    @api.doc('delete a new product_item')
    @api.marshal_with(product_item)
    def delete(self,product_item_id):
        """Deletes a new ProductItem """
        product_item = delete_a_product_item(id=product_item_id)
        if not product_item:
            api.abort(404)
        else:
            return product_item


