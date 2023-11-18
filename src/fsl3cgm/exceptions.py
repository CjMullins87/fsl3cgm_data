"""Various exceptions to handle cases unique to this implementation"""


class FSL3Exception(Exception):
    """Base exception class"""

    pass


class CredsNotFound(FSL3Exception):
    pass
