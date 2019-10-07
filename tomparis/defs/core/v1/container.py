from tomparis.config import Config, Field

from .container_port import ContainerPort
from .env_var import EnvVar
from .resource_requirements import ResourceRequirements
from .security_context import SecurityContext
from .volume_mount import VolumeMount


class Container(Config):
    args = Field()
    command = Field(list)
    env = Field(list)  # EnvVar
    env_from = Field(list, "envFrom")  # EnvVarSource
    image = Field()
    image_pull_policy = Field(name="imagePullPolicy")
    lifecycle = Field(
        dict
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#lifecycle-v1-core
    liveness_probe = Field(
        dict, name="livenessProbe"
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#probe-v1-core
    name = Field()
    ports = Field(list)  # ContainerPort
    readiness_probe = Field(
        dict, name="readinessProbe"
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#probe-v1-core
    resources = Field(ResourceRequirements)
    security_context = Field(SecurityContext, "securityContext")
    stdin = Field()
    stdin_once = Field(name="stdinOnce")
    termination_message_path = Field(name="terminationMessagePath")
    termination_message_policy = Field(name="terminationMessagePolicy")
    tty = Field()
    volume_devices = Field(
        list, name="volumeDevices"
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#volumedevice-v1-core
    volume_mounts = Field(list, "volumeMounts")
    working_dir = Field(name="workingDir")

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
