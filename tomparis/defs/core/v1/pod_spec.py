from tomparis.config import Config, Field
from tomparis.defs.core.v1.security_context import SecurityContext


class PodSpec(Config):
    active_deadline_seconds = Field(name="activeDeadlineSeconds")
    affinity = Field(
        dict
    )  # TODO: Affinity class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#affinity-v1-core
    automount_service_account_token = Field(name="automountServiceAccountToken")
    containers = Field(list)
    dns_config = Field(
        dict, "dnsConfig"
    )  # TODO: PodDNSConfig class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#poddnsconfig-v1-core
    dns_policy = Field(name="dnsPolicy")
    host_aliases = Field(
        list, "hostAliases"
    )  # TODO: HostAlias class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#hostalias-v1-core
    host_ipc = Field(name="hostIPC")
    host_network = Field(name="hostNetwork")
    host_pid = Field(name="hostPID")
    hostname = Field()
    image_pull_secrets = Field(
        list, "imagePullSecrets"
    )  # TODO: LocalObjectReference  class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#localobjectreference-v1-core
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
    tolerations = Field(
        list, "tolerations"
    )  # TODO: Toleration class; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#toleration-v1-core
    volumes = Field(
        list
    )  # TODO: Volume class; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#volume-v1-core
