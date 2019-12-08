from tomparis.fields import BoolField
from tomparis.fields import ListField
from tomparis.fields import ModelField
from tomparis.fields import StringField
from tomparis.model import Model

from .container_port import ContainerPort
from .env_var import EnvVar
from .env_var_source import EnvVarSource
from .resource_requirements import ResourceRequirements
from .security_context import SecurityContext
from .volume_mount import VolumeMount


class Lifecycle(Model):
    pass
    # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#lifecycle-v1-core


class Probe(Model):
    pass
    # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#probe-v1-core


class VolumeDevices(Model):
    pass
    # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#volumedevice-v1-core


class Container(Model):
    args = ListField(str)
    command = ListField(str)
    env = ListField(EnvVar)
    env_from = ListField(EnvVarSource, "envFrom")
    image = StringField()
    image_pull_policy = StringField(name="imagePullPolicy")
    lifecycle = ModelField(Lifecycle)
    liveness_probe = ModelField(Probe, name="livenessProbe")
    name = StringField()
    ports = ListField(ContainerPort)  #
    readiness_probe = ModelField(Probe, name="readinessProbe")
    resources = ModelField(ResourceRequirements)
    security_context = ModelField(SecurityContext, "securityContext")
    stdin = BoolField()
    stdin_once = BoolField(name="stdinOnce")
    termination_message_path = StringField(name="terminationMessagePath")
    termination_message_policy = StringField(name="terminationMessagePolicy")
    tty = BoolField()
    volume_devices = ListField(VolumeDevices, name="volumeDevices")
    volume_mounts = ListField(VolumeMount, "volumeMounts")
    working_dir = StringField(name="workingDir")

    def add_port(
        self, name: str = None, container_port: int = None, protocol: str = None
    ):
        port = ContainerPort()
        port.name = name
        port.container_port = container_port
        port.protocol = protocol
        self.ports.append(port)

    def add_env_from(self, typename: str, name: str):
        self.env_from.append({typename: {"name": name}})

    def add_env(self, name: str, value: str):
        env = EnvVar()
        env.name = name
        env.value = value
        self.env.append(env)

    def add_volume_mount(self, name: str, mount_path: str):
        volume = VolumeMount()
        volume.name = name
        volume.mount_path = mount_path
        self.volume_mounts.append(volume)

    def set_image(self, repository: str, registry: str = None, tag: str = None):
        if (repository or repository != "docker.io") and tag:
            self.image = f"{registry}/{repository}:{tag}"
        elif repository or repository != "docker.io":
            self.image = f"{registry}/{repository}"
        elif tag:
            self.image = f"{repository}:tag"
        else:
            raise RuntimeError("This should not happen ever!")
