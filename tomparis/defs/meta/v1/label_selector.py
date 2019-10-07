from tomparis.config import Config, Field

from .label_selector_requirement import LabelSelectorRequirement


class LabelSelector(Config):
    match_expressions = Field(LabelSelectorRequirement, name="matchExpressions")
    match_labels = Field(dict, name="matchLabels")
