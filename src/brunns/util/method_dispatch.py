from functools import update_wrapper

try:
    from functools import singledispatch
except ImportError:
    from singledispatch import singledispatch


def methoddispatch(func):
    """From https://stackoverflow.com/a/24602374"""
    dispatcher = singledispatch(func)

    def wrapper(*args, **kw):
        return dispatcher.dispatch(args[1].__class__)(*args, **kw)

    wrapper.register = dispatcher.register
    update_wrapper(wrapper, func)
    return wrapper
