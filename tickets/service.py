from django_filters import rest_framework as filters
from tickets.models import Ticket


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TicketFilter(filters.FilterSet):
    company = CharFilterInFilter(field_name='company', lookup_expr='in')
    from_city = CharFilterInFilter(field_name='from_ti', lookup_expr='in')
    to_city = CharFilterInFilter(field_name='to_city', lookup_expr='in')
    price = filters.RangeFilter()

    class Meta:
        model = Ticket
        fields = ['company', 'from_city', 'to_city']
