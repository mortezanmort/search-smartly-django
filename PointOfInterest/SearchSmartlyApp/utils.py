from typing import Dict, List, Optional

def extract_ratings(poi_dict: Dict[str, str]) -> Optional[List[float]]:
    """
    Extract ratings from the given dictionary.

    Args:
        poi_dict (Dict[str, str]): Dictionary containing PointOfInterest data.

    Returns:
        Optional[List[float]]: List of extracted ratings, or None if not present.
    """
    ratings = None

    if 'ratings' in poi_dict:

        ratings = poi_dict['ratings']
    elif 'poi_ratings' in poi_dict:

        ratings = poi_dict['poi_ratings'].strip("{}").split(',')
    elif 'pratings' in poi_dict:

        ratings = poi_dict['pratings'].split(',')

    ratings = [float(rating) for rating in ratings] if ratings else None

    return ratings


def get_internal_id(poi_dict: Dict[str, str]) -> str:
    """
    Get the internal ID from the given dictionary.

    Args:
        poi_dict (Dict[str, str]): Dictionary containing PointOfInterest data.

    Returns:
        str: Internal ID.
    """
    return poi_dict.get('poi_id', poi_dict.get('id', poi_dict.get('pid', '')))

def get_name(poi_dict: Dict[str, str]) -> str:
    """
    Get the name from the given dictionary.

    Args:
        poi_dict (Dict[str, str]): Dictionary containing PointOfInterest data.

    Returns:
        str: Name.
    """
    return poi_dict.get('poi_name', poi_dict.get('name', poi_dict.get('pname', '')))

def get_latitude(poi_dict: Dict[str, str]) -> Optional[str]:
    """
    Get the latitude from the given dictionary.

    Args:
        poi_dict (Dict[str, str]): Dictionary containing PointOfInterest data.

    Returns:
        Optional[str]: Latitude, or None if not present.
    """
    return poi_dict.get('poi_latitude', poi_dict.get('coordinates', {}).get('latitude', poi_dict.get('platitude')))

def get_longitude(poi_dict: Dict[str, str]) -> Optional[str]:
    """
    Get the longitude from the given dictionary.

    Args:
        poi_dict (Dict[str, str]): Dictionary containing PointOfInterest data.

    Returns:
        Optional[str]: Longitude, or None if not present.
    """
    return poi_dict.get('poi_longitude', poi_dict.get('coordinates', {}).get('longitude', poi_dict.get('plongitude')))

def get_category(poi_dict: Dict[str, str]) -> str:
    """
    Get the category from the given dictionary.

    Args:
        poi_dict (Dict[str, str]): Dictionary containing PointOfInterest data.

    Returns:
        str: Category.
    """
    return poi_dict.get('poi_category', poi_dict.get('category', poi_dict.get('pcategory', '')))
