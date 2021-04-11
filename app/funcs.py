from django.contrib.auth.models import User 

def block(ids):
    for id in ids:
        user = User.objects.get(id=id)
        user.is_active = False
        user.save()

def unblock(ids):
    for id in ids:
        user = User.objects.get(id=id)
        user.is_active = True
        user.save()

def delete(ids):
    for id in ids:
        user = User.objects.get(id=id)
        user.delete()
