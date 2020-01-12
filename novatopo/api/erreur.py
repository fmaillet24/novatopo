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


class AddActivity(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    price = graphene.Int()
    address = graphene.String()
    descriptions = graphene.String()
    is_staff = graphene.Boolean()

    class Arguments:
        name = graphene.String()
        price = graphene.Int()
        address = graphene.String()
        descriptions = graphene.String()
        is_staff = graphene.Boolean()

    def mutate(self, info, name, price, address, descriptions, is_staff):
        activity = Activity(name=name, price=price, address=address,
                            descriptions=descriptions, is_staff=is_staff)
        activity.save()

        return AddActivity(
            id=activity.id,
            name=activity.name,
            price=activity.price,
            address=activity.address,
            descriptions=activity.descriptions,
            is_staff=is_staff)


class AddBusiness(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    activity = graphene.Int()

    class Arguments:
        name = graphene.String()
        activity = graphene.Int()

    def mutate(self, info, name, activity):
        print(activity)
        x = Activity.objects.get(id=activity)
        print(x.id)
        business = Business(name=name, activity=x.id)
        business.save()

        return AddBusiness(
            id=business.id,
            name=business.name,
            activity=business.activity)


class Mutation(graphene.ObjectType):
    create_booking = CreateBooking.Field()
    add_activity = AddActivity.Field()
    add_business = AddBusiness.Field()
