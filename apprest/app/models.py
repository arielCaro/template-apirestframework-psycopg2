from django.db import models

class user(models.Model):
    name = models.CharField(max_length=200),
    last_name = models.CharField(max_length=200),
    email =  models.CharField(max_length=200),
    active = models.BooleanField(),
    date_created = models.DateTimeField(auto_now_add=True),
    date_modified = models.DateTimeField(auto_now=True),
    user_created = models.CharField(max_length=200),
    user_modified = models.CharField(max_length=200), 
    id_company =  models.IntegerField(),
    password = models.TextField(),
    id_role = models.IntegerField(),
    phone = models.IntegerField(),
    phone_mobile =  models.IntegerField(),
    code_phone_country = models.CharField(max_length=10)
    
class role(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(),
    active = models.BooleanField()

class company(models.Model):
    name = models.CharField(max_length=200),
    address = models.TextField(),
    contact_phone = models.IntegerField(),
    active = models.BooleanField(),
    date_created = models.DateTimeField(auto_now_add=True),
    date_modified = models.DateTimeField(auto_now=True),
    user_created = models.CharField(max_length=200),
    user_modified = models.CharField(max_length=200)

class session(models.Model):
    session_on = models.DateTimeField(auto_now_add=True),
    session_out = models.DateTimeField(),
    token_bearer = models.TextField(),
    active = models.BooleanField(),
    iduser = models.BigIntegerField(),
    idapp = models.IntegerField()
