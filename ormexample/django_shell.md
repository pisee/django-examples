### using django-extensions
``` python
$ python3 manage.py shell_plus
# Shell Plus Model Imports
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from ormexample.models import Manager, Place, Restaurant, Waiter
from polls.models import Choice, Question
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
from django.utils import timezone
from django.urls import reverse
Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> p1 = Place(name='Demon Dogs', address='944 W. Fullerton')
>>> p1
<Place: Demon Dogs the place>
>>> p1.save()
>>> 
>>> 
>>> p2 = Place(name='Ace Hardware', address='1013 N. Ashland')
>>> p2
<Place: Ace Hardware the place>
>>> p2.save()
>>> 
>>> 
>>> r1 = Restaurant(place=p1, serves_hot_dogs=True, serves_pizza=False)
>>> r1
<Restaurant: Demon Dogs the restaurant>
>>> r1.save()
>>> 
>>> 
>>> p1
<Place: Demon Dogs the place>
>>> p1.id
1
>>> 
>>> 
>>> r1.place
<Place: Demon Dogs the place>
>>> 
>>> 
>>> p1.restaurant
<Restaurant: Demon Dogs the restaurant>
>>> 
>>> 
>>> p2.restaurant = r1
>>> p2.restaurant 
<Restaurant: Ace Hardware the restaurant>
>>> p2.save()
>>> p1.restaurant
<Restaurant: Ace Hardware the restaurant>
>>> 
>>> 
>>> p2.restaurant
<Restaurant: Ace Hardware the restaurant>
>>> 
>>> 
>>> r2 = Restaurant.objects.create(place=p1, serves_hot_dogs=True, serves_pizza=False)
<Restaurant: Demon Dogs the restaurant>
>>> 
>>> 
>>> Restaurant.objects.all()
<QuerySet [<Restaurant: Ace Hardware the restaurant>, <Restaurant: Demon Dogs the restaurant>]>
>>> 
>>> 
>>> w1 = r1.waiter_set.create(name='Joe')
>>> w2 = r1.waiter_set.create(name='pole')
>>> Waiter.objects.all()
<QuerySet [<Waiter: Joe the waiter at Ace Hardware the restaurant>, <Waiter: pole the waiter at Ace Hardware the restaurant>]>
>>> Waiter.objects.filter(restaurant__place=p1)
<QuerySet []>
>>> Waiter.objects.filter(restaurant__place=p2)
<QuerySet [<Waiter: Joe the waiter at Ace Hardware the restaurant>, <Waiter: pole the waiter at Ace Hardware the restaurant>]>
>>> 
>>> 
>>> m1 = r1.manager_set.create(name='doni')
>>> m1
<Manager: doni the name at ormexample.Restaurant.None>
>>> m2 = r1.manager_set.create(name='dani')
>>> m3 = r2.manager_set.create(name='rena')
>>> m4 = r2.manager_set.create(name='miho')
>>> 
>>> 
>>> m1.restaurant.add(r1,r2)
>>> 
>>> 
>>> r1.manager_set.all()
<QuerySet [<Manager: doni the name at ormexample.Restaurant.None>, <Manager: dani the name at ormexample.Restaurant.None>]>
>>> m1.restaurant.all()
<QuerySet [<Restaurant: Ace Hardware the restaurant>, <Restaurant: Demon Dogs the restaurant>]>
>>> 
>>>
```