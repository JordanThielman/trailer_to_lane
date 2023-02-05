import random
import numpy as np
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "trailer_to_lane.settings")
import django
django.setup()
from django.db import IntegrityError
from main.models import Package



def seed_data():
    for i in range(29000):
        # Set the destination_lane to a random number between 1 and 3
        destination_lane = random.randint(1, 4)

        # Set the size using a normal distribution
        size = np.random.choice(["sml", "med", "lrg"], p=[0.6, 0.3, 0.1])

        # Set the trailer id to a random number between 1 and 14
        trailer_id = random.randint(1, 15)

        # Create the Package object and save it to the database
        try:
            Package.objects.create(
                destination_lane=destination_lane,
                size=size,
                trailer_id=trailer_id
            )
        except IntegrityError:
            continue

if __name__ == '__main__':
    seed_data()
