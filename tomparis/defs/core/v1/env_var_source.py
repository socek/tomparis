from tomparis.fields import ModelField
from tomparis.model import Model


class ConfigMapKeyRef(Model):
    pass
    # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#configmapkeyselector-v1-core


class FieldRef(Model):
    pass
    # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#objectfieldselector-v1-core


class FesourceFieldRef(Model):
    pass
    # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#resourcefieldselector-v1-core


class SecretKeyRef(Model):
    pass
    # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#secretkeyselector-v1-core


class EnvVarSource(Model):
    config_map_key_ref = ModelField(ConfigMapKeyRef, name="configMapKeyRef")
    field_ref = ModelField(FieldRef, name="fieldRef")
    resource_field_ref = ModelField(FesourceFieldRef, name="resourceFieldRef")
    secret_key_ref = ModelField(SecretKeyRef, name="secretKeyRef")
