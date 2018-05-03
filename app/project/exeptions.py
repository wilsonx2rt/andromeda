from rest_framework.exceptions import APIException


class LikeDoesNotExist(APIException):
    status_code = 400
    default_detail = 'Like does not exist'
    default_code = 'bad_request'
