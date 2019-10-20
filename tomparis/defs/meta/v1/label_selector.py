from tomparis.fields import DictField, ModelField
from tomparis.model import Model

from .label_selector_requirement import LabelSelectorRequirement


class LabelSelector(Model):
    match_expressions = ModelField(LabelSelectorRequirement, name="matchExpressions")
    match_labels = DictField(name="matchLabels")
