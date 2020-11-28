import django_filters
from django_filters import *

from .models import *

class PropertyFilter(django_filters.FilterSet):
	price = RangeFilter()
	class Meta:
		model = Property
		fields = '__all__'
		exclude = ['about', 'street','pic','latitude','longitude']