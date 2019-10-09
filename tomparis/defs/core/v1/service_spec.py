from tomparis.model import Model, Field

from .service_port import ServicePort


class ServiceSpec(Model):
    cluster_ip = Field(name="clusterIP")
    external_ips = Field(list, name="externalIPs")
    external_name = Field(name="externalName")
    external_traffic_policy = Field(name="externalTrafficPolicy")
    health_check_node_port = Field(name="healthCheckNodePort")
    load_balancer_ip = Field(name="loadBalancerIP")
    load_balancer_source_ranges = Field(list, name="loadBalancerSourceRanges")
    ports = Field(list)  # ServicePort
    publish_not_ready_addresses = Field(name="publishNotReadyAddresses")
    selector = Field(dict)
    session_affinity = Field(name="sessionAffinity")
    session_affinity_config = Field(
        dict, name="sessionAffinityConfig"
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#sessionaffinityconfig-v1-core
    type = Field()

    def add_port(self, port, target_port, protocol=None, name=None):
        service_port = ServicePort()
        service_port.port = port
        service_port.target_port = target_port
        service_port.protocol = protocol
        service_port.name = name
        self.ports.append(service_port)
