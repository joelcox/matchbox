

def hint(*types):

    def decorator(f):
        def newf(*args):

            # Check whether the length of arguments matches the length of types
            if len(args) is not len(types):
                raise TypeError('%s hint decorator expects %s types (%s given)' % (f.__name__, len(args), len(types)))

            # Get all the types of the passed arguments
            arg_types = tuple(map(type, args))

            # Zip up the types of the passed arguments and the types, so we
            # get a list of tuples which contain the actual type and the
            # desired type.
            for index, arg in enumerate(zip(arg_types, types)):

                if arg[1] is not None and arg[0] is not arg[1]:
                    raise TypeError('Argument %s should be %s (got %s)' % (index + 1, arg[1], arg[0]))

            return f(*args)

        newf.__name__ = f.__name__
        return newf

    return decorator