from tomparis.defs.core.v1 import PodSpec
from tomparis.defs.meta.v1 import LabelSelector, ObjectMeta
from tomparis.fields import BoolField, IntField, ModelField
from tomparis.model import Model


class PodTemplateSpec(Model):
    metadata = ModelField(ObjectMeta)
    spec = ModelField(PodSpec)


class DeploymentStrategy(Model):
    pass
    # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#deploymentstrategy-v1-apps


class DeploymentSpec(Model):
    min_ready_seconds = IntField(name="minReadySeconds")
    paused = BoolField()
    progress_deadline_seconds = IntField(name="progressDeadlineSeconds")
    replicas = IntField()
    revision_history_limit = IntField(name="revisionHistoryLimit")
    selector = ModelField(LabelSelector)
    strategy = ModelField(DeploymentStrategy)
    template = ModelField(PodTemplateSpec)
