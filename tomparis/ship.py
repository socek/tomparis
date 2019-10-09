from __future__ import annotations
import collections

from tomparis.objects import KubernetesObject
from tomparis.yamlrepresenter import tp_representer
from yaml import add_representer, dump, safe_load


def deep_update_dict(orig_dict, new_dict):
    for key, val in new_dict.items():
        if isinstance(val, collections.Mapping):
            tmp = deep_update_dict(orig_dict.get(key, {}), val)
            orig_dict[key] = tmp
        elif isinstance(val, list):
            orig_dict[key] = orig_dict.get(key, []) + val
        else:
            orig_dict[key] = new_dict[key]
    return orig_dict


class Shipment:
    def __init__(self):
        self.settings = {}
        self.kobjects = []
        self.shipments = []

    def add_kobject(self, kobject: KubernetesObject):
        kobject.set_shipment(self)
        self.kobjects.append(kobject)

    def add_shipment(self, shipment: Shipment):
        self.shipments.append(shipment)

    def read_settings(self, filename: str):
        data = safe_load(open(filename))
        deep_update_dict(self.settings, data)

    def generate(self):
        add_representer(dict, tp_representer)
        for kobject in self.kobjects:
            data = kobject.serialize()
            print("---")
            print(dump(data))
