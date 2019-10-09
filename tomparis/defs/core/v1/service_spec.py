from tomparis.fields import (
    BoolField,
    DictField,
    IntField,
    ListField,
    ModelField,
    StringField,
)
from tomparis.model import Model

from .service_port import ServicePort


class SessionAffinityConfig(Model):
    pass
    # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.11/#sessionaffinityconfig-v1-core


class ServiceSpec(Model):
    cluster_ip = StringField(name="clusterIP")
    external_ips = ListField(str, name="externalIPs")
    external_name = StringField(name="externalName")
    external_traffic_policy = StringField(name="externalTrafficPolicy")
    health_check_node_port = IntField(name="healthCheckNodePort")
    load_balancer_ip = StringField(name="loadBalancerIP")
    load_balancer_source_ranges = ListField(str, name="loadBalancerSourceRanges")
    ports = ListField(ServicePort)
    publish_not_ready_addresses = BoolField(name="publishNotReadyAddresses")
    selector = DictField()
    session_affinity = StringField(name="sessionAffinity")
    session_affinity_config = ModelField(
        SessionAffinityConfig, name="sessionAffinityConfig"
    )
    type = StringField()

    def add_port(
        self, port: int, target_port: int, protocol: str = None, name: str = None
    ):
        service_port = ServicePort()
        service_port.port = port
        service_port.target_port = target_port
        service_port.protocol = protocol
        service_port.name = name
        self.ports.append(service_port)
