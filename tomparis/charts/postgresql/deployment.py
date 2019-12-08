from tomparis.defs.apps.v1 import Deployment
from tomparis.defs.core.v1 import Container


class PsqlContainer(Container):
    def prepare(self):
        super().prepare()
        registry = self.settings["image"]["registry"]
        repository = self.settings["image"]["repository"]
        tag = self.settings["image"]["tag"]

        self.name = "psql-container"
        self.image = f"{registry}/{repository}:{tag}"
        self.image_pull_policy = self.settings["image"]["pullPolicy"]

        self.add_env("POSTGRESQL_PASSWORD", "simplepass")


class PsqlDeployment(Deployment):
    def __init__(self):
        super().__init__("psql-deployment")

    def prepare(self):
        super().prepare()
        self.add_container(PsqlContainer())
        self.spec.selector.match_labels["name"] = self._name
        self.spec.template.metadata.labels["name"] = self._name
