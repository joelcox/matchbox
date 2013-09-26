

class Container(object):
    """Inversion of control container that injects dependencies through
    typehints.
    """

    def resolve(self, className):
        """Receives a class for which the appropriate dependencies are resolves
        which are injected in the instance and returned to the caller.
        """
        return className()