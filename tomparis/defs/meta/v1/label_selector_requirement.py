from tomparis.fields import ListField, StringField
from tomparis.model import Model


class LabelSelectorRequirement(Model):
    key = StringField()
    operator = StringField()
    values = ListField(str)
