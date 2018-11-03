import logging

LOG = logging.getLogger("root")


class Role:
    def __init__(self, name, accesses=None):
        """
        Initializes role.
        :param name: Role name
        :param accesses: List of dicts with accesses
        """
        self.name = name
        self.accesses = accesses if accesses is not None else []
        LOG.info("[Role] Created with name {}".format(name))

    def add_access_to_resource(self, resource):
        """
        Adds access to resource for a role.
        :param resource: function to which access may be granted
        """
        LOG.debug("[Role] Adding access for role {} to resource {}".format(
            self.name, resource.__name__
        ))
        self.accesses.append(resource.__name__)
        LOG.debug("[Role] Access added for role {}".format(self.name))

    def get_accesses(self):
        """
        Returns a list of accesses that a role has.
        :return: list of dicts with access specification
        """
        LOG.debug("[Role] Getting accesses for role {}: {}".format(
            self.name, self.accesses
        ))
        return self.accesses
