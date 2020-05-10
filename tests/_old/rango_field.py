from rango.base import rango_fops


class RangoField(object):
    def __init__(self, handler=None, entity=None, field=None):
        self.handler = handler
        self.entity = entity
        self.field = field

    def __eq__(self, value):
        return rango_fops.RangoEqOp(entity_name=None, field_name=None, value=None)
        return [str(self.entity.name), str(self.field), value]