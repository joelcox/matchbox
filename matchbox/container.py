

class Container(object):
    """Inversion of control container that injects dependencies through
    typehints.
    """

    _dependency_map = {}

    def resolve(self, class_name):
        """Receives a class for which the appropriate dependencies are resolves
        which are injected in the instance and returned to the caller.
        """

        dependencies = self._dependency_map.get(class_name)

        # Return an instance of the class if there are no dependencies at all
        if (dependencies is None):
            return class_name()

        resolved_dependencies = []

        # Resolve each dependency recursively
        for dependency in dependencies:
            resolved_dependencies.append(self.resolve(dependency))

        return class_name(*resolved_dependencies)

    def map(self, class_name, dependencies):
        """Maps the dependencies to a class.
        """
        self._dependency_map[class_name] = dependencies

