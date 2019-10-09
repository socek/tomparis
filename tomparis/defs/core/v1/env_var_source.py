from tomparis.model import Model, Field


class EnvVarSource(Model):
    config_map_key_ref = Field(
        dict, name="configMapKeyRef"
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#configmapkeyselector-v1-core
    field_ref = Field(
        dict, name="fieldRef"
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#objectfieldselector-v1-core
    resource_field_ref = Field(
        dict, name="resourceFieldRef"
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#resourcefieldselector-v1-core
    secret_key_ref = Field(
        dict, name="secretKeyRef"
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#secretkeyselector-v1-core
