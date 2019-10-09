from tomparis.model import Model, Field


class DeploymentStatus(Model):
    available_replicas = Field(name="availableReplicas")
    collision_count = Field(name="collisionCount")
    conditions = Field(
        list
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#deploymentcondition-v1-apps
    observed_generation = Field(name="observedGeneration")
    ready_replicas = Field(name="readyReplicas")
    replicas = Field()
    unavailable_replicas = Field()
    updated_replicas = Field()
