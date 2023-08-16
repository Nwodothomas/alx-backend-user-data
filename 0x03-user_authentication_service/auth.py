#!/usr/bin/env python3
"""Authentication Module
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union

def _hash_password(password: str) -> str:
    """Hashes the input password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def _generate_uuid() -> str:
    """Generates a UUID.

    Returns:
        str: The generated UUID as a string.
    """
    id = uuid4()
    return str(id)

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize the Auth instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> Union[None, User]:
        """Registers a new user.

        Args:
            email (str): User's email.
            password (str): User's password.

        Returns:
            Union[None, User]: Newly created User object or None if user already exists.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            # Check if user already exists
            self._db.find_user_by(email=email)
        except NoResultFound:
            # Add user to database
            return self._db.add_user(email, _hash_password(password))
        else:
            # If user already exists, raise an error
            raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Validates user login credentials.

        Args:
            email (str): User's email.
            password (str): User's password.

        Returns:
            bool: True if valid login, False otherwise.
        """
        try:
            # Find the user with the given email
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        # Check validity of password
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """Creates a session for the user.

        Args:
            email (str): User's email.

        Returns:
            str: Session ID.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            user.session_id = _generate_uuid()
            return user.session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """Gets a user from a session ID.

        Args:
            session_id (str): Session ID.

        Returns:
            User: User object or None if session not found.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        else:
            return user

    def destroy_session(self, user_id: str) -> None:
        """Destroys a user's session.

        Args:
            user_id (str): User ID.
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None
        else:
            user.session_id = None
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Generates a reset password token for a user.

        Args:
            email (str): User's email.

        Returns:
            str: Reset password token.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        else:
            user.reset_token = _generate_uuid()
            return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates a user's password using a reset token.

        Args:
            reset_token (str): Reset password token.
            password (str): New password.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        else:
            user.hashed_password = _hash_password(password)
            user.reset_token = None
            return None
