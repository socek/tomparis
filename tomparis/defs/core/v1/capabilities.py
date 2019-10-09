from tomparis.model import Model
from tomparis.fields import ListField


class Capabilities(Model):
    add = ListField(str)
    drop = ListField(str)
