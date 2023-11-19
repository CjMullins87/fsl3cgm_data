"""Various exceptions to handle cases unique to this implementation"""


class FSL3Exception(Exception):
    """Base exception class"""

    pass


class CredsNotFound(FSL3Exception):
    """Raised when local creds aren't found or readable."""

    # NOTE: I expect an `fsl3_credentials.json` file in the parent directory
    # of the package
    pass


class TokenExpired(FSL3Exception):
    """Raised when it is determined that the current token is expired."""

    pass
