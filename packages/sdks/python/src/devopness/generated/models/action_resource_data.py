"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import Union

from .application_relation import ApplicationRelation, ApplicationRelationPlain
from .credential_relation import CredentialRelation, CredentialRelationPlain
from .cron_job_relation import CronJobRelation, CronJobRelationPlain
from .daemon_relation import DaemonRelation, DaemonRelationPlain
from .network_relation import NetworkRelation, NetworkRelationPlain
from .network_rule_relation import NetworkRuleRelation, NetworkRuleRelationPlain
from .server_relation import ServerRelation, ServerRelationPlain
from .service_relation import ServiceRelation, ServiceRelationPlain
from .ssh_key_relation import SshKeyRelation, SshKeyRelationPlain
from .ssl_certificate_relation import (
    SslCertificateRelation,
    SslCertificateRelationPlain,
)
from .subnet_relation import SubnetRelation, SubnetRelationPlain
from .virtual_host_relation import VirtualHostRelation, VirtualHostRelationPlain

#: AnyOf Type
#: The resource data of type specified on `resource.type`
ActionResourceData = Union[
    ApplicationRelation,
    CredentialRelation,
    CronJobRelation,
    DaemonRelation,
    NetworkRelation,
    NetworkRuleRelation,
    ServerRelation,
    ServiceRelation,
    SshKeyRelation,
    SslCertificateRelation,
    SubnetRelation,
    VirtualHostRelation,
]

#: The plain version of ActionResourceData
ActionResourceDataPlain = Union[
    ApplicationRelationPlain,
    CredentialRelationPlain,
    CronJobRelationPlain,
    DaemonRelationPlain,
    NetworkRelationPlain,
    NetworkRuleRelationPlain,
    ServerRelationPlain,
    ServiceRelationPlain,
    SshKeyRelationPlain,
    SslCertificateRelationPlain,
    SubnetRelationPlain,
    VirtualHostRelationPlain,
]
