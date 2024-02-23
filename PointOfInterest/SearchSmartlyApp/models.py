from django.db import models

class PointOfInterest(models.Model):
    """
    Model representing a Point of Interest (POI).

    Attributes:
        internal_id (str): The internal ID of the POI.
        name (str): The name of the POI.
        latitude (float): The latitude of the POI.
        longitude (float): The longitude of the POI.
        category (str): The category of the POI.
        ratings (list): A list containing the ratings of the POI.
        description (str, optional): A description of the POI (nullable).
        external_id (str, optional): The external ID of the POI (unique and nullable).
    """

    internal_id = models.CharField(max_length=255, verbose_name="Internal ID")
    name = models.CharField(max_length=255, verbose_name="Name")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")
    category = models.CharField(max_length=255, verbose_name="Category")
    ratings = models.JSONField(verbose_name="Ratings")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    external_id = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name="External ID")

    def __str__(self):
        """
        Return a human-readable string representation of the POI.

        Returns:
            str: The name of the POI.
        """
        return self.name
