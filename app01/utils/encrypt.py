import hashlib
from django.conf import settings

#加盐加密方法
def md5(pa_data):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(pa_data.encode('utf-8'))
    return obj.hexdigest()