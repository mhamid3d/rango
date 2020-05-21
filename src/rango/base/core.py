import mongoengine as me
from requests import get
from rango import schemas
import os


class RangoHandler(object):
    _DATABASE = 'jinx'
    _PORT = os.getenv('MONGO_PORT')
    _THIS_EXT_IP = str(get("https://api.ipify.org").text)
    _MONGO_EXT_IP = os.getenv('MONGO_EXT_IP')
    _MONGO_INT_IP = os.getenv('MONGO_INT_IP')

    if _THIS_EXT_IP == _MONGO_EXT_IP:
        _HOST = _MONGO_INT_IP
    else:
        _HOST = _MONGO_EXT_IP

    def __init__(self):
        me.connect(db=self._DATABASE, host=self._HOST, port=self._PORT)

    def job(self, **kwargs):
        return schemas.Job.objects(**kwargs)

    def stem(self, **kwargs):
        return schemas.Stem.objects(**kwargs)

    def twig(self, **kwargs):
        return schemas.Twig.objects(**kwargs)

    def stalk(self, **kwargs):
        return schemas.Stalk.objects(**kwargs)

    def leaf(self, **kwargs):
        return schemas.Leaf.objects(**kwargs)

    def seed(self, **kwargs):
        return schemas.Seed.objects(**kwargs)
