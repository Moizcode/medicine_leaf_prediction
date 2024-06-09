from django.core.management.base import BaseCommand
from api.models import Leaf
import json


class Command(BaseCommand):
    help = 'Load a list of leaves from a JSON file into the database'

    def handle(self, *args, **options):
        with open(r'C:\Users\moizb\OneDrive\Desktop\codes\django\djangoproject\medicinal leaf\leafapp\leaf_database.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for leaf in data:
                Leaf.objects.create(
                    hindiName=leaf['hindiName'],
                    sanskritName=leaf['sanskritName'],
                    englishName=leaf['englishName'],
                    latinName=leaf['latinName'],
                    shortDescription=leaf['shortDescription'],
                    longDescription=leaf['longDescription'],
                    medicinalUses=leaf['medicinalUses']
                )
        self.stdout.write(self.style.SUCCESS(
            'Successfully loaded leaf data into database'))
