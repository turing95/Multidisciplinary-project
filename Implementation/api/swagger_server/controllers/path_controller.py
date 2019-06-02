import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util
from swagger_server.models import Path

from path_recommender import user_predictions as up
from path_recommender.utils import path_to_png


def get_related_paths(pathId, limit=None, offset=None):  # noqa: E501
    """Returns related paths

    Returns a collection of paths related to the given one # noqa: E501

    :param pathId: 
    :type pathId: int
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    :rtype: InlineResponse200
    """


    return 'do some magic!'


def get_suggested_paths(userId, limit=None, offset=None):  # noqa: E501
    """Get suggested paths

    Get a set of suggested paths for the current user # noqa: E501

    :param userId: 
    :type userId: int
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    :rtype: InlineResponse200
    """

    _, predictions=up.recommend(userId)
    
    suggestions=predictions.to_dict(orient='records')

    result = []
    for s in suggestions:
        image_url=path_to_png.plot_path_to_png(timezone = s['time_zone'])

        path = Path(
            path_id = s['pathId'],
            title = s['title'],
            image_url = image_url
        )
        result.append(path)


    return result
