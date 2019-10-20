from tomparis.chart import Chart
from tomparis.defs.core.v1 import ConfigMap


class MyConfig(ConfigMap):
    def prepare(self):
        self.metadata.name = "name2"
        self.metadata.labels["hello"] = "me"
        self.data["from"] = self.settings["from"]


class MySecondChart(Chart):
    def prepare_settings(self):
        super().prepare_settings()
        self.settings["from"] = "second_chart"

    def prepare_chart(self):
        super().prepare_chart()
        self.add_kobject(MyConfig())
