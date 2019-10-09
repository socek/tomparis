from tomparis.model import Model
from tomparis.fields import BoolField, ModelField, IntField

from .capabilities import Capabilities
from .se_linux_options import SELinuxOptions


class SecurityContext(Model):
    allow_privilege_escalation = BoolField(name="allowPrivilegeEscalation")
    capabilities = ModelField(Capabilities)
    privileged = BoolField()
    read_only_root_filesystem = BoolField(name="readOnlyRootFilesystem")
    run_as_group = IntField(name="runAsGroup")
    run_as_non_root = BoolField(name="runAsNonRoot")
    run_as_user = IntField(name="runAsUser")
    se_linux_options = ModelField(SELinuxOptions, name="seLinuxOptions")
