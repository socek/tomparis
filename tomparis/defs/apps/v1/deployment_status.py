from tomparis.model import Model
from tomparis.fields import IntField, ListField


class DeploymentCondition(Model):
    pass
    # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#deploymentcondition-v1-apps


class DeploymentStatus(Model):
    available_replicas = IntField(name="availableReplicas")
    collision_count = IntField(name="collisionCount")
    conditions = ListField(DeploymentCondition)
    observed_generation = IntField(name="observedGeneration")
    ready_replicas = IntField(name="readyReplicas")
    replicas = IntField()
    unavailable_replicas = IntField()
    updated_replicas = IntField()
