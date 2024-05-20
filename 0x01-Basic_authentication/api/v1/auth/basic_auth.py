#!/usr/bin/env python3
"""
6. Basic auth
"""
from flask import request
from typing import List, TypeVar, Optional
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    6. Basic auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> Optional[str]:
        """"  6. Basic auth """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
