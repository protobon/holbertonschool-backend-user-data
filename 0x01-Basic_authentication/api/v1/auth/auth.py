#!/usr/bin/env python3
"""Authentication"""

from flask import request
from typing import List, TypeVar


class Auth():
    """Class for user authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if the path requested requires authorization
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        for excl_path in excluded_paths:
            if path == excl_path or\
               (path in excl_path and len(path) == len(excl_path) - 1):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Checks if the request header has an Authorization key
        """
        if request is None:
            return None
        if request.headers.get('Authorization'):
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ TO-DO implementation
        """
        return None