#!/usr/bin/env python3
"""
1. Empty session
"""
from flask import request
from typing import List, TypeVar, Optional, Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class SessionAuth(Auth):
    """SessionAuth"""
    pass
