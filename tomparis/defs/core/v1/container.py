from tomparis.config import Config, Field
from tomparis.fields import BoolField, ListField, ModelField, StringField

from .container_port import ContainerPort
from .env_var import EnvVar
from .env_var_source import EnvVarSource
from .resource_requirements import ResourceRequirements
from .security_context import SecurityContext
from .volume_mount import VolumeMount


class Container(Config):
    args = ListField(str)
    command = ListField(str)
    env = ListField(EnvVar)
    env_from = ListField(EnvVarSource, "envFrom")
    image = StringField()
    image_pull_policy = StringField(name="imagePullPolicy")
    lifecycle = Field(
        dict
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#lifecycle-v1-core
    liveness_probe = Field(
        dict, name="livenessProbe"
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#probe-v1-core
    name = StringField()
    ports = ListField(ContainerPort)  #
    readiness_probe = Field(
        dict, name="readinessProbe"
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#probe-v1-core
    resources = ModelField(ResourceRequirements)
    security_context = ModelField(SecurityContext, "securityContext")
    stdin = BoolField()
    stdin_once = BoolField(name="stdinOnce")
    termination_message_path = StringField(name="terminationMessagePath")
    termination_message_policy = StringField(name="terminationMessagePolicy")
    tty = BoolField()
    volume_devices = ListField(
        dict, name="volumeDevices"
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#volumedevice-v1-core
    volume_mounts = ListField(VolumeMount, "volumeMounts")
    working_dir = StringField(name="workingDir")

    def add_port(self, name=None, container_port=None, protocol=None):
        port = ContainerPort()
        port.name = name
        port.container_port = container_port
        port.protocol = protocol
        self.ports.append(port)

    def add_env_from(self, typename, name):
        self.env_from.append({typename: {"name": name}})

    def add_env(self, name, value):
        env = EnvVar()
        env.name = name
        env.value = value
        self.env.append(env)

    def add_volume_mount(self, name, mount_path):
        volume = VolumeMount()
        volume.name = name
        volume.mount_path = mount_path
        self.volume_mounts.append(volume)
