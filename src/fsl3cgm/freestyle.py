"""Connects to FreeStyle API components and fetches data"""

import requests
import time


class FreeStyleAPI:
    def __init__(self, user_email: str, password: str):
        """Basic connection components"""
        # Android headers, because we're using the Android API for access
        # NOTE: the versions change often enough, so we'll need a way to rotate
        # these in the event of a non-response
        self.base_url = "https://api.libreview.io/"
        self.headers = {
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
        kwargs = {"header": self.headers, "json": json}

        try:
            resp = None
            resp = requests.request(*args, **kwargs)
            resp.raise_for_status()

        except requests.HTTPError:
            ...
