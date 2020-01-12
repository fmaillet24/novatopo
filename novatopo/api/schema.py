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


class CreateBooking(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    participant = graphene.Int()
    date = graphene.types.datetime.DateTime()
    total = graphene.Int()
    is_staff = graphene.Boolean()
    activity = graphene.String()

    class Arguments:
        name = graphene.String()
        email = graphene.String()
        participant = graphene.Int()
        date = graphene.types.datetime.DateTime()
        is_staff = graphene.Boolean()
        activity = graphene.String()

    def mutate(self, info, name, email, participant, date, is_staff, activity):
        x = Activity.objects.get(name=activity)
        if ActivityAvailable.objects.filter(activity=x, date=date).exists():
            price = x.price
            total = int(price) * int(participant)
            booking = Booking(name=name, email=email, participant=participant,
                              date=date, is_staff=is_staff, total=total, activity=x)
            booking.save()
        else:
            raise Exception('Invalid Date')

        return CreateBooking(
            id=booking.id,
            name=booking.name,
            email=booking.email,
            participant=booking.participant,
            date=booking.date,
            total=booking.total,
            is_staff=booking.is_staff,
            activity=booking.activity)


class Mutation(graphene.ObjectType):
    create_booking = CreateBooking.Field()


class Query(object):
    all_activity = graphene.List(ActivityType)
    all_business = graphene.List(BusinessType)
    all_booking = graphene.List(BookingType)
    all_activity_available = graphene.List(ActivityAvailableType)

    def resolve_all_activity(self, info, **kwargs):
        return Activity.objects.all()

    def resolve_all_business(self, info, **kwargs):
        return Business.objects.all()

    def resolve_all_booking(self, info, **kwargs):
        return Booking.objects.all()

    def resolve_all_activity_available(self, info, **kwargs):
        return ActivityAvailable.objects.all()
