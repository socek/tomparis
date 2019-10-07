from uuid import uuid4

from tomparis.config import Config, Field


class StatusCause(Config):
    field = Field()
    message = Field()
    reason = Field()


class StatusDetails(Config):
    causes = Field(list)
    group = Field()
    kind = Field()
    name = Field()
    retry_after_seconds = Field(name="retryAfterSeconds")
    uid = Field()


class ListMeta(Config):
    continue_ = Field(name="continue")
    resource_version = Field(name="resourceVersion")


class Status(Config):
    api_version = Field(name="apiVersion")
    code = Field()
    details = Field(StatusDetails)
    kind = Field()
    message = Field()
    metadata = Field()
    reason = Field()
    status = Field()


class Initializer(Config):
    name = Field(ListMeta)


class Initializers(Config):
    pending = Field(list)
    result = Field(Status)


class OwnerReference(Config):
    api_version = Field(name="apiVersion")
    block_owner_deletion = Field(name="blockOwnerDeletion")
    controller = Field()
    kind = Field()
    name = Field()
    uid = Field()


class Metadata(Config):
    annotations = Field(dict)
    cluster_name = Field(name="clusterName")
    creation_timestamp = Field(name="creationTimestamp")
    deletion_grace_period_seconds = Field(name="deletionGracePeriodSeconds")
    deletion_timestamp = Field(name="deletionTimestamp")
    finalizers = Field(list)
    generate_name = Field(name="generateName")
    generation = Field(name="generation")
    initializers = Field(Initializers)
    labels = Field(dict)
    name = Field()
    namespace = Field()
    owner_references = Field(list, name="ownerReferences")  # OwnerReference
    resource_version = Field()
    self_link = Field(name="selfLink")
    uid = Field()

    def _get_uid(self, value):
        if value:
            return value
        elif self.shipment.settings["core"]["autogenerate_uid"]:
            return uuid4().hex
