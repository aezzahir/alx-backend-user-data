#!/usr/bin/env python3
"""
1. Empty session
"""
from flask import request
from typing import List, TypeVar, Optional, Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64
from uuid import uuid4


class SessionAuth(Auth):
    """SessionAuth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session"""

        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return (None)
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
