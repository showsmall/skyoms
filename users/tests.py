from django.test import TestCase
import redis
# Create your tests here.


conn = redis.Redis(host='localhost',port=6379,password='Redis@123')

