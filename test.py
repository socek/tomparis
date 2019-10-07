from tomparis.configmap import ConfigMap
from tomparis.container import Container
from tomparis.deployment import Deployment
from tomparis.service import Service
from tomparis.ship import Shipment


class MyConfig(ConfigMap):
    def prepare(self):
        self.metadata.name = "NaMe"
        self.metadata.namespace = "namespace"
        self.metadata.labels["elo"] = 10
        self.data["ELO"] = self.settings["elo"]["super"]


class MyService(Service):
    def prepare(self):
        self.metadata.name = "NaMe Service"
        self.metadata.labels["thisis"] = "service"
        self.spec.add_port(80, 80, name="UPS")
        self.spec.selector["termos"] = "howmelksow"
        self.spec.type = "ClusterIP"


class MyContainer(Container):
    def prepare(self):
        self.name = "backend"
        self.image_pull_policy = "IfNotPresent"
        self.add_port("http", 80, "TCP")
        self.add_env_from("configMapRef", "database")
        self.add_env("HELLO", 10)
        self.add_env("ME", "heLpe")

        self.resources.limits.cpu = 1
        self.resources.limits.memory = 2
        self.resources.requests.cpu = 3
        self.resources.requests.memory = 4

        self.command = ["/bin/bash", "-c"]
        self.args = ["some", "args"]

        self.add_volume_mount("MyName", "/path")


class MyDeployment(Deployment):
    def prepare(self):
        self.add_container(MyContainer())


shipment = Shipment()
shipment.read_settings("values.yaml")


shipment.add_kobject(MyConfig())
shipment.add_kobject(MyService())
shipment.add_kobject(MyDeployment())
shipment.generate()
