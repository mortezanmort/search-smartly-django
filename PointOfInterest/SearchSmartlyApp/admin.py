from django.contrib import admin
from .models import PointOfInterest

@admin.register(PointOfInterest)
class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ('internal_id', 'name', 'latitude', 'longitude', 'external_id', 'category', 'ratings_avg')
    search_fields = ('internal_id', 'external_id')
    list_filter = ('category',)


    def ratings_avg(self, obj: PointOfInterest) -> float:
        """
        Calculate and return the average rating for the PointOfInterest.

        Args:
            obj (PointOfInterest): The PointOfInterest instance.

        Returns:
            float: The average rating or 0 if no ratings are available.
        """
        return sum(obj.ratings) / len(obj.ratings) if obj.ratings else 0.0

    ratings_avg.short_description = 'Avg. rating'
