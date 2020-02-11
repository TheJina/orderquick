from flask import request
from flask_restx import Resource
from app.main import redis_client

from ..marshall.dto import FCMTokenDto

api = FCMTokenDto.api
fcm_token=FCMTokenDto.fcm_token

@api.route('/<fuid_id>')
@api.param('fuid_id', 'The FCM_token identifier')
class FCMToken(Resource):
    @api.doc('Set FCM Token')
    @api.expect(fcm_token, validate=True)
    def post(self,fuid_id):
        """Set  FCM Token"""
        data = request.json
        print(data['token'])
        redis_client.set(fuid_id,data['token'])
        return { 'message': 'Token Created' } , 200 

    @api.doc('Get FCM Token')
    def get(self,fuid_id):
        """Get FCM Token"""
        print(redis_client.get(fuid_id))
        return { 'token': redis_client.get(fuid_id).decode('utf-8')} , 200
