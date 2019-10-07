from tomparis.config import Config, Field
from tomparis.meta import Metadata
from tomparis.objects import KubernetesObject
from tomparis.selector import LabelSelector
from tomparis.container import SecurityContext


class PodSpec(Config):
    active_deadline_seconds = Field(name="activeDeadlineSeconds")
    affinity = Field(dict)  # TODO: Affinity class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#affinity-v1-core
    automount_service_account_token = Field(name="automountServiceAccountToken")
    containers = Field(list)
    dns_config = Field(dict, "dnsConfig")  # TODO: PodDNSConfig class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#poddnsconfig-v1-core
    dns_policy = Field(name="dnsPolicy")
    host_aliases = Field(list, "hostAliases")  # TODO: HostAlias class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#hostalias-v1-core
    host_ipc = Field(name="hostIPC")
    host_network = Field(name="hostNetwork")
    host_pid = Field(name="hostPID")
    hostname = Field()
    image_pull_secrets = Field(list, "imagePullSecrets")  # TODO: LocalObjectReference  class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#localobjectreference-v1-core
    init_containers = Field(list, "initContainers")
    node_name = Field(name="nodeName")
    node_selector = Field(dict, "nodeSelector")
    priority = Field()
    priority_class_name = Field(name="priorityClassName")
    restart_policy = Field(name="restartPolicy")
    scheduler_name = Field(name="schedulerName")
    security_context = Field(SecurityContext, "securityContext")
    service_account = Field(name="serviceAccount")
    service_account_name = Field(name="serviceAccountName")
    share_process_namespace = Field(name="shareProcessNamespace")
    subdomain = Field()
    termination_grace_period_seconds = Field(name="terminationGracePeriodSeconds")
    tolerations = Field(list, "tolerations")  # TODO: Toleration class; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#toleration-v1-core
    volumes = Field(list)  # TODO: Volume class; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#volume-v1-core


class PodTemplateSpec(Config):
    metadata = Field(Metadata)
    spec = Field(PodSpec)


class DeploymentSpec(Config):
    min_ready_seconds = Field(name="minReadySeconds")
    paused = Field()
    progress_deadline_seconds = Field(name="progressDeadlineSeconds")
    replicas = Field()
    revision_history_limit = Field(name="revisionHistoryLimit")
    selector = Field(LabelSelector)
    strategy = Field(dict)
    template = Field(PodTemplateSpec)


class Deployment(KubernetesObject):
    api_version = "apps/v1"
    kind = "Deployment"

    spec = Field(DeploymentSpec)
    status = Field(dict)

    def add_container(self, container):
        self.spec.template.spec.containers.append(container)

    def add_init_container(self, container):
        self.spec.template.spec.initContainers.append(container)
