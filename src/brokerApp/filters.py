import django_filters
from django_filters import *

from .models import *

class PropertyFilter(django_filters.FilterSet):
	price = RangeFilter()
	class Meta:
		model = Property
		fields = '__all__'
		exclude = [
			'about',
			'street',
			'pic',
			'latitude',
			'longitude',
			'rented',
			'pic2',
			'pic3',
			'pic4',
			'pic5',
			'glft_file',
			'bin_file']