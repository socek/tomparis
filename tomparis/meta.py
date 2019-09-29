from uuid import uuid4

from tomparis.config import Config, Field


class Metadata(Config):
    def __init__(self):
        super().__init__()
        self.name = None
        self.namespace = None
        self.labels = {}
        self.annotations = {}
        self.creation_timestamp = None
        self.resource_version = None
        self.uid = None

    @Field("name")
    def get_name(self):
        return self.name

    @Field("namespace")
    def get_namespace(self):
        return self.namespace

    @Field("labels")
    def get_labels(self):
        return self.labels

    @Field("annotations")
    def get_annotations(self):
        return self.annotations

    @Field("creationTimestamp")
    def get_creation_timestamp(self):
        return self.creation_timestamp

    @Field("resourceVersion")
    def get_resource_version(self):
        return self.resource_version

    @Field("uid")
    def get_uid(self):
        if self.uid:
            return self.uid
        elif self.shipment.settings["core"]["autogenerate_uid"]:
            return uuid4().hex
