"""Utilities for fetching/maintaining fsl_credentials.json"""

import datetime
import json

from fsl3cgm import ROOT_DIR
from fsl3cgm.exceptions import TokenExpired, CredsNotFound


class Creds:
    def __init__(
        self,
        user_email: str = None,
        password: str = None,
        patient_id: str = None,
        token: str = None,
        token_expires: str = None,
    ):
        """Houses user auth information.

        Args:
            user_email (str, optional): LibreLinkUp Email. Defaults to None.
            password (str, optional): LibreLinkUp Password. Defaults to None.
            patient_id (str, optional): LibreLinkUp PatientID. Defaults to None.
            token (str, optional): LibreLinkUp API token. Defaults to None.
            token_expires (str, optional): API token expiration time. Defaults to None.
        """
        self.user_email = user_email
        self.password = password
        self.patient_id = patient_id
        self.token = token
        self.token_expires = token_expires

    def read_fsl3_credentials_json(self):
        """Reads the local credentials info into object"""
        # We should have a creds file saved at the top of the directory
        try:
            credsfile = open(ROOT_DIR / "fsl3_credentials.json", "r")
            data = json.load(credsfile)

            self.user_email = data["user_info"]["user_email"]
            self.password = data["user_info"]["password"]
            self.patient_id = data["user_info"]["patient_id"]
            self.token = data["auth"]["token"]
            self.token_expires = data["auth"]["expires"]

        except FileNotFoundError:
            raise CredsNotFound(
                "Couldn't load local creds. "
                "Are they formatted and in the parent directory?"
            )

    def check_if_token_expired(self):
        """Reads the expiry date"""

        if datetime.now() < self.token_expires:
            pass
        else:
            raise TokenExpired("Your included token has expired.")
