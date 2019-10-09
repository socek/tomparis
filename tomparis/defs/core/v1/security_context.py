from tomparis.model import Model, Field

from .capabilities import Capabilities
from .se_linux_options import SELinuxOptions


class SecurityContext(Model):
    allow_privilege_escalation = Field(name="allowPrivilegeEscalation")
    capabilities = Field(Capabilities)
    privileged = Field()
    read_only_root_filesystem = Field(name="readOnlyRootFilesystem")
    run_as_group = Field(name="runAsGroup")
    run_as_non_root = Field(name="runAsNonRoot")
    run_as_user = Field(name="runAsUser")
    se_linux_options = Field(SELinuxOptions, name="seLinuxOptions")
