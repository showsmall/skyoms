from django.test import TestCase
from .models import Clusters
# Create your tests here.

clusters = Clusters.objects.all()

json_list =[]
json_dict ={}
for c in clusters:
    json_dict["virtual"] = c.vmscount
    json_dict["py"] = c.numshosts





