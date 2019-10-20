from tomparis.defs.apps.v1 import Deployment
from tomparis.defs.core.v1 import ConfigMap, Container, Service
from tomparis.chart import Chart


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


chart = Chart()
chart.read_settings("values.yaml")


chart.add_kobject(MyConfig())
chart.add_kobject(MyService())
chart.add_kobject(MyDeployment())
chart.generate()
