import inspect


def froze_it(cls):
    def frozensetattr(self, key, value):
        methodname = inspect.stack()[1][3]
        if not hasattr(self, key) and (
            methodname != "__init__" and not methodname.startswith("set_")
        ):
            raise RuntimeError(
                f"Class {cls.__name__} is frozen. Cannot set {key} = {value}"
            )
        else:
            self.__dict__[key] = value

    cls.__setattr__ = frozensetattr
    return cls


class Field:
    def __init__(self, fieldname):
        self.fieldname = fieldname

    def __call__(self, fieldmethod):
        fieldmethod._fieldname = self.fieldname
        return fieldmethod


@froze_it
class Config:
    def __init__(self):
        self.shipment = None

    @property
    def settings(self):
        return self.shipment.settings

    def set_shipment(self, shipment):
        self.shipment = shipment

    def serialize(self, shipment=None):
        if shipment:
            self.set_shipment(shipment)
        self.prepare()
        fields = {}
        for attrname in dir(self):
            try:
                attr = getattr(self, attrname)
                fieldname = getattr(attr, "_fieldname", None)
                if fieldname:
                    fields[fieldname] = attr
            except AttributeError:
                pass

        data = {}
        for name, method in fields.items():
            value = method()
            if isinstance(value, Config):
                value = value.serialize(self.shipment)
            elif isinstance(value, list):
                value = [
                    item.serialize(self.shipment) if isinstance(item, Config) else item
                    for item in value
                ]
            if value or value is False:
                data[name] = value
        return data

    def prepare(self):
        pass
