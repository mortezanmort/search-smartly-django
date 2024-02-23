from typing import Dict
from celery import shared_task
from .utils import extract_ratings, get_category, get_internal_id, get_latitude, get_longitude, get_name
from SearchSmartlyApp.models import PointOfInterest
import uuid

@shared_task
def create_poi_from_dict_task(poi_dict: Dict[str, str]) -> None:
    """
    Task to create a PointOfInterest instance from a dictionary.

    Args:
        poi_dict (Dict[str, str]): Dictionary containing PointOfInterest data.
    """
    ratings = extract_ratings(poi_dict)
    internal_id = get_internal_id(poi_dict)
    external_id = str(uuid.uuid4())
    description = poi_dict.get('description')

    PointOfInterest.objects.create(
        internal_id=internal_id,
        name=get_name(poi_dict),
        latitude=get_latitude(poi_dict),
        longitude=get_longitude(poi_dict),
        external_id=external_id,
        category=get_category(poi_dict),
        ratings=ratings,
        description=description
    )
