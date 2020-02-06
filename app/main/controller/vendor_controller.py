from flask import request
from flask_restx import Resource
from ..marshall.dto import VendorDto
from ..service.vendor_service import save_new_vendor, get_all_vendors, get_all_vendors_within_radius, get_a_vendor, update_vendor
api = VendorDto.api
addvendor = VendorDto.addvendor
vendor = VendorDto.vendor


@api.route('/')
class VendorList(Resource):
    @api.doc('list_of_registered_vendors',params={'longitude': 'Provide longitude','latitude':'Provide latitude','radius':'Provide radius'})
    @api.marshal_list_with(vendor, envelope='data')
    def get(self):
        """List all registered vendors"""
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        radius = request.args.get('radius')
        if longitude and latitude and radius:
            return get_all_vendors_within_radius('POINT({} {})'.format(longitude,latitude),radius)
        return get_all_vendors()

    @api.expect(addvendor, validate=True)
    @api.marshal_with(vendor)
    @api.doc('create a new vendor')
    def post(self):
        """Creates a new Vendor """
        data = request.json
        print(data)
        return save_new_vendor(data=data)


@api.route('/<vendor_id>')
@api.param('vendor_id', 'The Vendor identifier')
@api.response(404, 'Vendor not found.')
class Vendor(Resource):
    @api.doc('get a vendor')
    @api.marshal_with(vendor)
    def get(self, vendor_id):
        """get a vendor given its identifier"""
        vendor = get_a_vendor(vendor_id)
        if not vendor:
            api.abort(404)
        else:
            return vendor

    @api.expect(addvendor, validate=True)
    @api.marshal_with(vendor)
    @api.doc('update a new vendor')
    def put(self,vendor_id):
        """Updates a new Vendor """
        data = request.json
        vendor = update_vendor(data=data,id=vendor_id)
        if not vendor:
            api.abort(404)
        else:
            return vendor


