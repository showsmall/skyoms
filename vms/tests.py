from django.test import TestCase

# Create your tests here.
from vms.models import DataCenters

datacenter = DataCenters.objects.filter(name='Datacenter_201_1').values(id)


print(datacenter)

