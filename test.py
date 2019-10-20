from tomparis.chart import Chart
from tomparis.defs.apps.v1 import Deployment
from tomparis.defs.core.v1 import ConfigMap
from tomparis.defs.core.v1 import Container
from tomparis.defs.core.v1 import Service

from test2 import MySecondChart


class MyConfig(ConfigMap):
    def prepare(self):
        self.metadata.name = "name"
        self.metadata.labels["hello"] = "me"
        self.data["elo"] = "CC"
        self.data["my"] = "config"


class MyService(Service):
    def prepare(self):
        self.metadata.name = "name-service"
        self.metadata.labels["thisis"] = "service"
        self.spec.add_port(80, 80, name="ups")
        self.spec.selector["termos"] = "howmelksow"
        self.spec.type = "ClusterIP"


class MyContainer(Container):
    def prepare(self):
        self.name = "backend"
        self.image_pull_policy = "IfNotPresent"
        self.add_port("http", 80, "TCP")
        self.add_env_from("configMapRef", "database")
        self.add_env("HELLO", "10")
        self.add_env("ME", "heLpe")

        self.resources.limits.cpu = "1cpu"
        self.resources.limits.memory = "2MBi"
        self.resources.requests.cpu = "3cpus"
        self.resources.requests.memory = "4MBi"

        self.command = ["/bin/bash", "-c"]
        self.args = ["some", "args"]

        self.add_volume_mount("MyName", "/path")


class MyDeployment(Deployment):
    def prepare(self):
        self.add_container(MyContainer())
        self.spec.selector.match_labels["name"] = "myname"


class MyChart(Chart):
    def prepare_requirements(self):
        super().prepare_requirements()
        self.add_chart(MySecondChart("mysecond"))

    def prepare_settings(self):
        super().prepare_settings()
        self.read_settings("values.yaml")

        self.charts["mysecond"].update_settings(self.settings["second"])

    def prepare_chart(self):
        super().prepare_chart()
        self.add_kobject(MyConfig())
        # self.add_kobject(MyService())
        # self.add_kobject(MyDeployment())


chart = MyChart()
chart.printall()
