from __future__ import annotations

from collections import Mapping, OrderedDict

from tomparis.objects import KubernetesObject
from tomparis.yamlrepresenter import tp_representer
from yaml import add_representer, dump, safe_load


def deep_update_dict(orig_dict, new_dict):
    for key, val in new_dict.items():
        if isinstance(val, Mapping):
            tmp = deep_update_dict(orig_dict.get(key, {}), val)
            orig_dict[key] = tmp
        elif isinstance(val, list):
            orig_dict[key] = orig_dict.get(key, []) + val
        else:
            orig_dict[key] = new_dict[key]
    return orig_dict


class Chart:
    def __init__(self, name=None):
        self.name = name
        self.settings = {}
        self.kobjects = []
        self.charts = OrderedDict()

    def add_kobject(self, kobject: KubernetesObject):
        kobject.set_chart(self)
        self.kobjects.append(kobject)

    def add_chart(self, chart: Chart):
        self.charts[chart.name] = chart

    def update_settings(self, settings: dict):
        self.settings = deep_update_dict(self.settings, settings)

    def read_settings(self, filename: str):
        data = safe_load(open(filename))
        deep_update_dict(self.settings, data)

    def prepare_requirements(self):
        for chart in self.charts.values():
            chart.prepare_requirements()

    def prepare_settings(self):
        for chart in self.charts.values():
            chart.prepare_settings()

    def prepare_chart(self):
        for chart in self.charts.values():
            chart.prepare_chart()

    def generate(self):
        for chart in self.charts.values():
            yield from chart.generate()

        for kobject in self.kobjects:
            yield kobject.serialize()

    def printall(self):
        self.prepare_requirements()
        self.prepare_settings()
        self.prepare_chart()

        add_representer(dict, tp_representer)

        for kobject in self.generate():
            print("---")
            print(dump(kobject))
