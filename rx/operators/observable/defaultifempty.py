from rx.core import AnonymousObservable, ObservableBase


def default_if_empty(source, default_value=None) -> ObservableBase:
    """Returns the elements of the specified sequence or the specified
    value in a singleton sequence if the sequence is empty.

    Examples:
        >>> res = obs = xs.default_if_empty()
        >>> obs = xs.default_if_empty(False)

    Args:
        default_value: The value to return if the sequence is empty. If
        not provided, this defaults to None.

    Returns:
        An observable sequence that contains the specified default value
        if the source is empty otherwise, the elements of the source.
    """

    def subscribe(observer, scheduler=None):
        found = [False]

        def on_next(x):
            found[0] = True
            observer.on_next(x)

        def on_completed():
            if not found[0]:
                observer.on_next(default_value)
            observer.on_completed()

        return source.subscribe_(on_next, observer.on_error, on_completed, scheduler)
    return AnonymousObservable(subscribe)
