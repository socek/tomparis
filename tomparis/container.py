from tomparis.config import Config, Field


class SecurityContext(Config):
    allow_privilege_escalation = Field(name="allowPrivilegeEscalation")
    capabilities = Field(dict)
    privileged = Field()
    read_only_root_filesystem = Field(name="readOnlyRootFilesystem")
    run_as_group = Field(name="runAsGroup")
    run_as_non_root = Field(name="runAsNonRoot")
    run_as_user = Field(name="runAsUser")
    se_linux_options = Field(name="seLinuxOptions")


class VolumeMount(Config):
    name = Field()
    mount_path = Field(name="mountPath")


class ResourceElement(Config):
    cpu = Field()
    memory = Field()


class Resources(Config):
    limits = Field(ResourceElement)
    requests = Field(ResourceElement)


class Env(Config):
    name = Field()
    value = Field()


class ContainerPort(Config):
    name = Field()
    container_port = Field(name="containerPort")
    protocol = Field()


class Container(Config):
    name = Field()
    image = Field()
    image_pull_policy = Field(name="imagePullPolicy")
    ports = Field(list)
    env_from = Field(list, "envFrom")
    env = Field(list)
    resources = Field(Resources)
    command = Field(list)
    args = Field()
    volume_mounts = Field(list, "volumeMounts")
    security_context = Field(SecurityContext, "securityContext")
    lifecycle = Field(dict)
    liveness_probe = Field(dict, name="livenessProbe")
    readiness_probe = Field(dict, name="readinessProbe")
    stdin = Field()
    stdin_once = Field(name="stdinOnce")
    termination_message_path = Field(name="terminationMessagePath")
    termination_message_policy = Field(name="terminationMessagePolicy")
    tty = Field()
    volume_devices = Field(list, name="volumeDevices")
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
        env = Env()
        env.name = name
        env.value = value
        self.env.append(env)

    def add_volume_mount(self, name, mount_path):
        volume = VolumeMount()
        volume.name = name
        volume.mount_path = mount_path
        self.volume_mounts.append(volume)
