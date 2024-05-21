#!/usr/bin/env python3
"""
6. Basic auth
"""
from flask import request
from typing import List, TypeVar, Optional
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """8. Basic - Base64 decode"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
