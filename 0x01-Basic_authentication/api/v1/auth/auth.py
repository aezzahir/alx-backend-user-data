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
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        path = path.rstrip('/')
        for excluded_path in excluded_paths:
            excluded_path = excluded_path.rstrip('/')
            if path == excluded_path:
                return False
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """request will be the Flask request object"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None - request will be the Flask request object"""
        return None
