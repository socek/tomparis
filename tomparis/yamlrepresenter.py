from yaml import representer

SORTING = [
    "apiVersion",
    "kind",
    "metadata",
    "data",
    "spec",
    "template",
    "name",
    "labels",
    "annotations",
    "selector",
    "replicas",
    "initContainers",
    "containers",
    "image",
    "imagePullPolicy",
    "resources",
    "type",
    "ports",
    "env",
    "envFrom",
    "command",
    "args",
]


def sort_key(key):
    try:
        return SORTING.index(key)
    except ValueError:
        return len(SORTING)


def tp_representer(self, data):
    keys = sorted(data.keys(), key=sort_key)
    items = [(key, data[key]) for key in keys]
    return representer.SafeRepresenter.represent_dict(self, items)
