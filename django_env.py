import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_manager.settings")
import django
django.setup()
from news_app.models import NewsPost
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission, Group
import re
from django.contrib.auth.decorators import permission_required, login_required



# print(NewsPost.objects.all())

# ps = Permission.objects.filter(name__contains="news post")
# ps = Permission.objects.filter(codename__regex='[^auth]')
# print(ps)
# u = User.objects.first()
# u = User.objects.filter(username__contains='ll')[0]
# print(u.has_perm('news_app.Create_post'))
# u.user_permissions.add()
# print(u.user_permissions.all())

# print(u.user_permissions)


# g = Group.objects.create(name="editors")
# g = Group.objects.create(name="subscribers")
# g = Group.objects.filter(name="editors")[0]
# g = Group.objects.all()[0]
# g = Group.objects.all()[1]
# perm_id = Permission.objects.filter(codename='change_newspost')[0].id

# perms = Permission.objects.filter(codename__contains='newspost')
# for perm in perms:
#     g.permissions.add(perm.id)

# perms = Permission.objects.all()
# for perm in perms:
#     g.permissions.add(perm.id)
# perm_id = Permission.objects.filter(codename='view_newspost')[0].id
# print(g.permissions.add(perm_id))
# g.permissions.add(perm_id)
# u.groups.add(g)
# u.groups.remove(g)

