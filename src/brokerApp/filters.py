import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class PropertyFilter(django_filters.FilterSet):
	class Meta:
		model = Property
		fields = '__all__'
		exclude = ['about', 'street','pic']