class UserNotExist(Exception):
    """
    The user does it exist
    """

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        return 'The user not exist, please check for errors again'


class USER_PASSWORD_ERROR(Exception):
    """
    The user or password does it error
    """

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        return 'The user or password error'


class ZIP_ERROR(Exception):

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        return 'zip error'
