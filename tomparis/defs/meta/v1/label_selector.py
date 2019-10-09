from tomparis.model import Model, Field

from .label_selector_requirement import LabelSelectorRequirement


class LabelSelector(Model):
    match_expressions = Field(LabelSelectorRequirement, name="matchExpressions")
    match_labels = Field(dict, name="matchLabels")
