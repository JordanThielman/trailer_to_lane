from django.test import TestCase
from django.urls import reverse
import pytest
import os
from .models import Package
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "trailer_to_lane.settings")
import django
django.setup()

# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

def test_create_new_package():
    new_package = Package.objects.create(
        id=27089,
        destination_lane=4,
        size='lrg',
        trailer_id=13
    )
    assert new_package.id == 27089
