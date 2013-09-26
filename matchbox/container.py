

class Container(object):
    """Inversion of control container that injects dependencies through
    typehints.
    """

    _dependency_map = {}

    def resolve(self, class_name):
        """Receives a class for which the appropriate dependencies are resolves
        which are injected in the instance and returned to the caller.
        """
        return class_name()

    def map(self, class_name, dependencies):
        self._dependency_map[class_name] = dependencies

