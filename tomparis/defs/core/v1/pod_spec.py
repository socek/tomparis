from tomparis.defs.core.v1.security_context import SecurityContext
from tomparis.fields import (
    BoolField,
    DictField,
    EnumField,
    IntField,
    ListField,
    ModelField,
    StringField,
)
from tomparis.model import Model

from . import Container


class Affinity(Model):
    pass
    # TODO: Affinity class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#affinity-v1-core


class PodDNSConfig(Model):
    pass
    # TODO: PodDNSConfig class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#poddnsconfig-v1-core


class HostAlias(Model):
    pass
    # TODO: HostAlias class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#hostalias-v1-core


class LocalObjectReference(Model):
    pass
    # TODO: LocalObjectReference class ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#localobjectreference-v1-core


class Toleration(Model):
    pass
    # TODO: Toleration class; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#toleration-v1-core


class Volume(Model):
    pass
    # TODO: Volume class; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#volume-v1-core


class PodReadlinessGate(Model):
    pass
    # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.11/#podreadinessgate-v1-core


class PodSpec(Model):
    active_deadline_seconds = IntField(name="activeDeadlineSeconds")
    affinity = ModelField(Affinity)
    automount_service_account_token = BoolField(name="automountServiceAccountToken")
    containers = ListField(Container)
    dns_config = ModelField(PodDNSConfig, "dnsConfig")
    dns_policy = EnumField(
        ["ClusterFirst", "ClusterFirstWithHostNet", "ClusterFirst", "Default", "None"],
        name="dnsPolicy",
    )
    host_aliases = ListField(HostAlias, "hostAliases")
    host_ipc = BoolField(name="hostIPC")
    host_network = BoolField(name="hostNetwork")
    host_pid = BoolField(name="hostPID")
    hostname = StringField()
    image_pull_secrets = ListField(LocalObjectReference, "imagePullSecrets")
    init_containers = ListField(Container, "initContainers")
    node_name = StringField(name="nodeName")
    node_selector = DictField(name="nodeSelector")
    priority = IntField()
    priority_class_name = StringField(name="priorityClassName")
    readiness_gates = ListField(PodReadlinessGate, name="readinessGates")
    restart_policy = EnumField(["Always", "OnFailure", "Never"], name="restartPolicy")
    scheduler_name = StringField(name="schedulerName")
    security_context = ModelField(SecurityContext, "securityContext")
    service_account_name = StringField(name="serviceAccountName")
    share_process_namespace = BoolField(name="shareProcessNamespace")
    subdomain = StringField()
    termination_grace_period_seconds = IntField(name="terminationGracePeriodSeconds")
    tolerations = ListField(Toleration, "tolerations")
    volumes = ListField(Volume)
