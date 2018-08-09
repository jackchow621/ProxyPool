class ResourceDepletionException(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('The proxy source is exhausted')


class PoolEmptyException(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('The proxy pool is empty')
