import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def user_get_friends(userId, limit=None, offset=None):  # noqa: E501
    """Get user&#39;s friends

    Get all the friends of a given user # noqa: E501

    :param userId: 
    :type userId: int
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    :rtype: List[User]
    """
    return 'do some magic!'
