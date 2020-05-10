from pymongo.database import Database as MongoDatabase
from requests import get
from rango.base.rango_entity import RangoEntity
import pymongo as pm


class RangoHandler(MongoDatabase):
    _THIS_EXT_IP = get("https://api.ipify.org").text
    _MONGO_EXT_IP = "24.200.206.122"
    _MONGO_INT_IP = "127.0.0.1"
    _PORT = 18732

    if _THIS_EXT_IP == _MONGO_EXT_IP:
        _HOST = _MONGO_INT_IP
    else:
        _HOST = _MONGO_EXT_IP

    _CLIENT = pm.MongoClient(host=_HOST, port=_PORT)

    def __init__(self):
        super(RangoHandler, self).__init__(name='jinx', client=self._CLIENT)

    @property
    def facility_entities(self):
        return ['job', 'stem', 'twig', 'stalk', 'leaf', 'seed']

    def is_valid_entity(self, entity):
        entity = str(entity)
        if entity in self.facility_entities:
            return True
        else:
            return False

    def __getitem__(self, name):
        if self.is_valid_entity(name):
            return self.get_entity(name)
        else:
            raise AttributeError(name)

    def get_entity(self, name):
        return RangoEntity(handler=self, name=name)