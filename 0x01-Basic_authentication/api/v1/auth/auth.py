#!/usr/bin/env python3
"""
3.Authentication Class
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    3.Authentication Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """that returns"""
        return False

    def authorization_header(self, request=None) -> str:
        """request will be the Flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None - request will be the Flask request object"""
        return None
