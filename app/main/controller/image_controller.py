from flask_restx import Resource , Namespace
from flask_uploads import UploadNotAllowed
from flask import send_file, request
import os

from app.main.libs import image_helper

api = Namespace('image', description='Get or upload image')

@api.route('/<vendor_id>/<filename>')
class Image(Resource):
   
    def get(self,vendor_id, filename: str):
        """
        This endpoint returns the requested image if exists. 
        """
        
        folder = f"user_{vendor_id}"
        # check if filename is URL secure
        if not image_helper.is_filename_safe(filename):
            return {"message": "image_illegal_file_name"}, 400
        try:
            # try to send the requested file to the user with status code 200
            return send_file(image_helper.get_path(filename, folder=folder))
        except FileNotFoundError:
            return {"message": "image_not_found"}, 404
