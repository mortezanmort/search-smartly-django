from django.core.management.base import BaseCommand
from SearchSmartlyApp.models import PointOfInterest

class Command(BaseCommand):
    help = 'Clear all Point of Interest data from the database'

    def handle(self, *args, **options):
        """
        Handle command execution.

        Args:
            *args: Additional arguments.
            **options: Additional options.

        Raises:
            Exception: If there is an error during the data clearing process.
        """
        try:
            self.clear_poi_data()
            self.stdout.write(self.style.SUCCESS('Successfully cleared all Point of Interest data.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error clearing Point of Interest data: {str(e)}"))

    def clear_poi_data(self) -> None:
        """
        Clear all Point of Interest data from the database.

        Raises:
            Exception: If there is an error during the data clearing process.
        """
        PointOfInterest.objects.all().delete()
