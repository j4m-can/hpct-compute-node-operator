#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Head node operator.
"""

import logging

from ops.main import main

from hpctlib.ops.charm.node import NodeCharm
from hpctlib.interface.relation import interface_registry


logger = logging.getLogger(__name__)


class HpctComputeNodeCharm(NodeCharm):
    """Operator for cluster compute node."""

    def __init__(self, *args):
        super().__init__(*args)

        self.interfaces = {
            "ldap-client-ready": interface_registry.load(
                "relation-subordinate-ready", self, "ldap-client-ready"
            ),
            "slurm-client-ready": interface_registry.load(
                "relation-subordinate-ready", self, "slurm-client-ready"
            ),
        }

        self.setup_subordinate_relations_and_syncs(["ldap-client-ready", "slurm-client-ready"])


if __name__ == "__main__":
    main(HpctComputeNodeCharm)
