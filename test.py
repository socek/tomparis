from test2 import MySecondChart
from tomparis.chart import Chart
from tomparis.charts.postgresql.chart import PostgreSQLChart
from tomparis.defs.apps.v1 import Deployment
from tomparis.defs.core.v1 import ConfigMap
from tomparis.defs.core.v1 import Container
from tomparis.defs.core.v1 import Secret
from tomparis.defs.core.v1 import Service


class MySecret(Secret):
    def prepare(self):
        super().prepare()
        self.data["doom"] = "sdsadwq"
        self.data["patrol"] = "xsew"


class MyConfig(ConfigMap):
    def prepare(self):
        super().prepare()
        self.metadata.labels["hello"] = "me"
        self.data["elo"] = "CC"
        self.data["my"] = "config"


class MyService(Service):
    def prepare(self):
        super().prepare()
        self.metadata.name = "name-service"
        self.metadata.labels["thisis"] = "service"
        self.spec.add_port(80, 80, name="ups")
        self.spec.selector["termos"] = "howmelksow"
        self.spec.type = "ClusterIP"


class MyContainer(Container):
    def prepare(self):
        super().prepare()
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
        super().prepare()
        self.add_container(MyContainer())
        self.spec.selector.match_labels["name"] = "myname"


class MyChart(Chart):
    def prepare_requirements(self):
        super().prepare_requirements()
        # self.add_chart(MySecondChart("mysecond"))
        self.add_chart(PostgreSQLChart("psql"))

    def prepare_settings(self):
        super().prepare_settings()
        self.read_settings("values.yaml")

        # self.update_subchart("mysecond", self.settings["mysecond"])

    # def prepare_chart(self):
    #     super().prepare_chart()
    #     self.add_kobject(MySecret("MySecret"))
    #     self.add_kobject(MyConfig("MyConfig"))
        # self.add_kobject(MyService())
        # self.add_kobject(MyDeployment())


chart = MyChart("mychart")
chart.printall()
