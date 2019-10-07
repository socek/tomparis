from tomparis.config import Config, Field
from tomparis.defs.meta.v1 import LabelSelector, ObjectMeta
from tomparis.defs.core.v1 import PodSpec


class PodTemplateSpec(Config):
    metadata = Field(ObjectMeta)
    spec = Field(PodSpec)


class DeploymentSpec(Config):
    min_ready_seconds = Field(name="minReadySeconds")
    paused = Field()
    progress_deadline_seconds = Field(name="progressDeadlineSeconds")
    replicas = Field()
    revision_history_limit = Field(name="revisionHistoryLimit")
    selector = Field(LabelSelector)
    strategy = Field(
        dict
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#deploymentstrategy-v1-apps
    template = Field(PodTemplateSpec)
