"""Connects to FreeStyle's LibreLinkUp API and fetches data"""

import requests

from fsl3cgm.creds import Creds


class FreeStyleAPI:
    def __init__(self, creds: Creds = None):
        """Basic connection components"""
        # Android headers, because we're using the Android API for access
        # NOTE: the versions change often enough, so we'll need a way to rotate
        # these in the event of a non-response
        self.base_url = "https://api.libreview.io/"
        self.creds = creds
        self.headers = {
            "authorization": f"Bearer {self.creds.token}",
            "accept-encoding": "gzip",
            "cache-control": "no-cache",
            "connection": "Keep-Alive",
            "content-type": "application/json",
            "product": "llu.android",
            "version": "4.7.0",
        }

    def _call_api(self, method: str, endpoint: str, json: str = None):
        """Establishes protocol for calling the API"""

        url = f"{self.base_url}/{endpoint}"
        args = (method, url)
        kwargs = {"headers": self.headers, "json": json}

        try:
            resp = None
            resp = requests.request(*args, **kwargs)
            resp.raise_for_status()

        except requests.HTTPError:
            # We don't have a lot of documentation to reference for what
            # the possible HTTP errors are, or any limitations on frequency
            raise

        return resp.json()

    def get_auth_token(self, return_token=False):
        """Use this to get an auth token for the attached creds object.

        This will automatically update the attached creds object, but passing
        return_token = True will return the token and its expiration date
        as a tuple

        Args:
            return_token (bool, optional): If True, return token data. Defaults to False.

        Returns:
            Tuple: (token, expiration_date)
        """
        # This endpoint is used to retrieve an auth token.
        # in experimentation it continued to return the same data, even
        # if a header containing "authentication" information was passed
        endpoint = "llu/auth/login"
        json = {"email": self.creds.user_email, "password": self.creds.password}

        resp = self._call_api("post", endpoint, json)

        # the data should live here
        token = resp["data"]["authTicket"]["token"]
        expiry = resp["data"]["authTicket"]["expires"]

        # update the creds object
        self.creds.token = token
        self.creds.token_expires = expiry

        if return_token:
            return (token, expiry)

    def get_patient_id(self, return_id=False):
        """Uses the auth information to fetch a patient ID for the attached creds.

        This call does return some glucose data in the JSON, but the graphdata
        API we intend to call has a full eight hours or so worth, so we can
        make fewer calls and get more data

        Args:
            return_id (bool, optional): If True, return the patient ID. Defaults to False.

        Returns:
            str: patient_id
        """
        # make the call
        endpoint = "llu/connections"
        resp = self._call_api("get", endpoint)

        # Extract and write
        _id = resp["data"][0]["patientId"]
        self.creds.patient_id = _id

        if return_id:
            return _id

    def get_graph_data(self):
        """Retrieve's the patient's graph data, this has about 8 hours of history.

        Returns:
            dict: the graphData json structure
        """
        endpoint = f"llu/connections/{self.creds.patient_id}/graph"
        resp = self._call_api("get", endpoint)

        # graphdata lives here:
        graphdata = resp["data"]["graphData"]

        # graphdata is shaped like this:
        # [
        # {
        # "FactoryTimestamp": "5/21/2022 1:39:50 AM",
        # "Timestamp": "5/21/2022 3:39:50 AM",
        # "type": 0,
        # "ValueInMgPerDl": 117,
        # "MeasurementColor": 1,
        # "GlucoseUnits": 1,
        # "Value": 117,
        # "isHigh": False,
        # "isLow": False
        # },
        # ]

        return graphdata
