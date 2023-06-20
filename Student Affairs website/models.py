# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class studstuddetail(models.Model):
    Male = 'Male'
    FeMale = 'Female'
    GENDER_CHOICES = (
    (Male, 'Male'),
    (FeMale, 'Female'),
    )
    First = 'First' 
    Second = 'Second'
    Third = 'Third'
    Fourth ='Fourth'
    LEVEL_CHOICES = (
    (First, 'First'),
    (Second, 'Second'),
    (Third, 'Third'),
    (Fourth, 'Fourth'),
    )
    Active = 'Active'
    Unactive = 'Unactive'
    STATUS_CHOICES = (
    (Active, 'Active'),
    (Unactive, 'Unactive'),
    )
    CS = 'Computer Sceince' 
    IT = 'Information Technology'
    IS = 'Information System'
    AI ='Artificial Intelligence'
    DEPART_CHOICES = (
    (CS, 'Computer Sceince'),
    (IT, 'Information Technology'),
    (IS, 'Information System'),
    (AI, 'Artificial Intelligence'),
    )
    STUDENT_ID = models.CharField(db_column='Id', unique=True, max_length=50)  # Field name made lowercase.
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    birthdate = models.DateField(db_column='birthDate')  # Field name made lowercase.
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, default = Male)
    gpa = models.IntegerField(db_column='gpa')
    level = models.CharField(max_length = 10, choices = LEVEL_CHOICES, default = First,db_column='level')
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = First)
    depart = models.CharField(max_length = 50, choices = DEPART_CHOICES, default = AI)
    email = models.EmailField(max_length=25)
    phone = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'stud_studdetail'


class studstuding(models.Model):
    studedby = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='studedBy_id')  # Field name made lowercase.
    studedstud = models.ForeignKey(studstuddetail, models.DO_NOTHING, db_column='studedstud_id')  # Field name made lowercase.
    returndate = models.DateField(db_column='returnDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stud_studing'
        unique_together = (('studedby', 'studedstud'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
