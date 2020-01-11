# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType

from api.models import Activity, Business, ActivityAvailable, Booking


class ActivityType(DjangoObjectType):
    class Meta:
        model = Activity


class BusinessType(DjangoObjectType):
    class Meta:
        model = Business


class ActivityAvailableType(DjangoObjectType):
    class Meta:
        model = ActivityAvailable


class BookingType(DjangoObjectType):
    class Meta:
        model = Booking


class Query(object):
    all_activity = graphene.List(ActivityType)
    all_business = graphene.List(BusinessType)
    all_booking = graphene.List(BookingType)
    all_activity_available = graphene.List(ActivityAvailableType)

    def resolve_all_activity(self, info, **kwargs):
        return Activity.objects.all()

    def resolve_all_business(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Business.objects.all()
