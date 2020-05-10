import pymongo as pm
from pymongo.collection import Collection as MongoCollection
from rango.base.rango_field import RangoField


class RangoEntity(MongoCollection):
    def __init__(self, handler=None, name=None):
        super(RangoEntity, self).__init__(database=handler, name=name)
        self.handler = handler

    def __getitem__(self, item):
        return RangoField(handler=self.handler, entity=self, field=item)

    def one(self, filter):
        msch = {}
        for c in filter.criteria:
            msch[c[1]] = c[2]

        return self.find_one(msch)