import csv
import json
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from ...tasks import create_poi_from_dict_task

class Command(BaseCommand):
    help = 'Import Point of Interest data from files'

    def add_arguments(self, parser):
        parser.add_argument('files', nargs='+', type=str, help='List of files to import')

    def handle(self, *args, **options):
        for file_path in options['files']:
            try:
                self.import_file(file_path)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error importing file {file_path}: {str(e)}"))

    def import_file(self, file_path: str) -> None:
        """
        Import data from a file and create PointOfInterest instances asynchronously.

        Args:
            file_path (str): The path to the file.

        Raises:
            Exception: If there is an error during the import process.
        """
        if file_path.endswith('.csv'):
            self.import_csv(file_path)
        elif file_path.endswith('.json'):
            self.import_json(file_path)
        elif file_path.endswith('.xml'):
            self.import_xml(file_path)
        else:
            self.stdout.write(self.style.ERROR(f"Unsupported file type: {file_path}"))

    def import_csv(self, file_path: str) -> None:
        """
        Import data from a CSV file and create PointOfInterest instances asynchronously.

        Args:
            file_path (str): The path to the CSV file.
        """
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                create_poi_from_dict_task.delay(row)

    def import_json(self, file_path: str) -> None:
        """
        Import data from a JSON file and create PointOfInterest instances asynchronously.

        Args:
            file_path (str): The path to the JSON file.
        """
        with open(file_path, 'r') as file:
            data = json.load(file)
            for entry in data:
                create_poi_from_dict_task.delay(entry)

    def import_xml(self, file_path: str) -> None:
        """
        Import data from an XML file and create PointOfInterest instances asynchronously.

        Args:
            file_path (str): The path to the XML file.
        """
        tree = ET.parse(file_path)
        root = tree.getroot()
        for element in root:
            entry = {child.tag: child.text for child in element}
            create_poi_from_dict_task.delay(entry)
