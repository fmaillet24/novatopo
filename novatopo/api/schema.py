# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType

from api.models import Activity, Business, ActivityAvailable, Booking, BusinessActivity


""" ACTIVITY """


class ActivityType(DjangoObjectType):
    class Meta:
        model = Activity


class AddActivity(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        activity = Activity(name=name)
        activity.save()

        return AddActivity(
            id=activity.id,
            name=activity.name)


class ModifyActivity(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        name = graphene.String()
        new_name = graphene.String()

    def mutate(self, info, name, new_name):
        activity = Activity.objects.get(name=name)
        activity.name = new_name
        activity.save()

        return ModifyActivity(
            id=activity.id,
            name=activity.name)


class RemoveActivity(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    ok = graphene.Boolean()

    class Arguments:
        name = graphene.String()

    def mutate(self, cls, info, name):
        activity = Activity.objects.filter(name=name)
        activity.delete()

        return RemoveActivity(ok=True)


""" BUSINESS """


class BusinessType(DjangoObjectType):
    class Meta:
        model = Business


class AddBusiness(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    address = graphene.String()

    class Arguments:
        name = graphene.String()
        address = graphene.String()

    def mutate(self, info, name, address):
        business = Business(name=name, address=address)
        business.save()

        return AddBusiness(
            id=business.id,
            name=business.name,
            address=business.address)


class ModifyBusiness(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    address = graphene.String()

    class Arguments:
        name = graphene.String()
        new_name = graphene.String()
        new_address = graphene.String()

    def mutate(self, info, name, new_name, new_address=""):
        business = Business.objects.get(name=name)
        if len(str(new_name)) > 0:
            business.name = new_name
        if len(str(new_address)) > 0:
            business.address = new_address
        business.save()

        return ModifyBusiness(
            id=business.id,
            name=business.name,
            address=business.address)


class RemoveBusiness(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    ok = graphene.Boolean()

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        business = Business.objects.filter(name=name)
        business.delete()

        return RemoveBusiness(ok=True)


""" BUSINESS ACTIVITY """


class BusinessActivityType(DjangoObjectType):
    class Meta:
        model = BusinessActivity


class AddBusinessActivity(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    price = graphene.Int()
    address = graphene.String()
    descriptions = graphene.String()
    is_staff = graphene.Boolean()
    activity = graphene.String()
    business = graphene.String()

    class Arguments:
        name = graphene.String()
        price = graphene.Int()
        address = graphene.String()
        descriptions = graphene.String()
        is_staff = graphene.Boolean()
        activity = graphene.String()
        business = graphene.String()

    def mutate(self, info, name, price, address, descriptions, is_staff, activity, business):
        activity = Activity.objects.get(name=activity)
        business = Business.objects.get(name=business)
        obj = BusinessActivity(name=name, price=price, address=address, descriptions=descriptions,
                               is_staff=is_staff, activity=activity, business=business)
        obj.save()

        return AddBusinessActivity(
            id=obj.id,
            name=obj.name,
            price=obj.price,
            address=obj.address,
            descriptions=obj.descriptions,
            is_staff=obj.is_staff,
            activity=obj.activity,
            business=obj.business)


class RemoveBusinessActivity(graphene.Mutation):
    id = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        business_activity = graphene.Int()

    def mutate(self, info, business_activity):
        obj = BusinessActivity.objects.get(id=business_activity)
        obj.delete()

        return RemoveBusinessActivity(ok=True)


""" ACTIVITY AVAILABLE """


class ActivityAvailableType(DjangoObjectType):
    class Meta:
        model = ActivityAvailable


class AddAvailability(graphene.Mutation):
    id = graphene.Int()
    date = graphene.types.datetime.DateTime()
    activity = graphene.Int()
    activity_format = graphene.String()

    class Arguments:
        date = graphene.types.datetime.DateTime()
        activity = graphene.Int()

    def mutate(self, info, date, activity):
        x = BusinessActivity.objects.get(id=activity)
        obj = ActivityAvailable(date=date, activity=x)
        obj.save()

        return AddAvailability(
            id=obj.id,
            date=obj.date,
            activity=obj.activity.id)


class RemoveAvailability(graphene.Mutation):
    id = graphene.Int()
    date = graphene.types.datetime.DateTime()
    activity = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        date = graphene.types.datetime.DateTime()
        activity = graphene.Int()

    def mutate(self, into, date, activity):
        x = BusinessActivity.objects.get(id=activity)
        obj = ActivityAvailable.objects.filter(date=date, activity=activity)
        obj.delete()

        return RemoveAvailability(ok=True)


""" BOOKING """


class BookingType(DjangoObjectType):
    class Meta:
        model = Booking


class AddBooking(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    participant = graphene.Int()
    date = graphene.types.datetime.DateTime()
    total = graphene.Int()
    paid = graphene.Boolean()
    is_staff = graphene.Boolean()
    activity = graphene.Int()

    class Arguments:
        name = graphene.String()
        email = graphene.String()
        participant = graphene.Int()
        date = graphene.types.datetime.DateTime()
        total = graphene.Int()
        paid = graphene.Boolean()
        is_staff = graphene.Boolean()
        activity = graphene.Int()

    def mutate(self, info, name, email, participant, date, total, paid, is_staff, activity):
        x = BusinessActivity.objects.get(id=activity)
        if ActivityAvailable.objects.filter(activity=x, date=date).exists():
            price = x.price
            total = int(price) * int(participant)
            booking = Booking(name=name, email=email, participant=participant, date=date,
                              total=total, paid=paid, is_staff=is_staff, activity=x)
            booking.save()

            return AddBooking(
                id=booking.id,
                name=booking.name,
                email=booking.email,
                participant=booking.participant,
                date=booking.date,
                total=booking.total,
                paid=booking.paid,
                is_staff=booking.is_staff,
                activity=booking.activity.id)
        else:
            raise Exception('Invalid Date')


""" MUTATION """


class Mutation(graphene.ObjectType):
    add_activity = AddActivity.Field()
    modify_activity = ModifyActivity.Field()
    remove_activity = RemoveActivity.Field()
    add_business = AddBusiness.Field()
    modify_business = ModifyBusiness.Field()
    remove_business = RemoveBusiness.Field()
    add_business_activity = AddBusinessActivity.Field()
    remove_business_activity = RemoveBusinessActivity.Field()
    add_availability = AddAvailability.Field()
    remove_availability = RemoveAvailability.Field()
    add_booking = AddBooking.Field()


""" QUERY """


class Query(object):
    all_activity = graphene.List(ActivityType)
    all_business = graphene.List(BusinessType)
    all_booking = graphene.List(BookingType)
    all_activity_available = graphene.List(ActivityAvailableType)
    all_business_activity = graphene.List(BusinessActivityType)

    def resolve_all_activity(self, info, **kwargs):
        return Activity.objects.all()

    def resolve_all_business(self, info, **kwargs):
        return Business.objects.all()

    def resolve_all_booking(self, info, **kwargs):
        return Booking.objects.all()

    def resolve_all_activity_available(self, info, **kwargs):
        return ActivityAvailable.objects.all()

    def resolve_all_business_activity(self, info, **kwarfs):
        return BusinessActivity.objects.all()
