# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Calendarevent(models.Model):
    calendareventid = models.AutoField(db_column='CALENDAREVENTID', primary_key=True)  # Field name made lowercase.
    marketid = models.ForeignKey('Market', models.DO_NOTHING, db_column='MARKETID')  # Field name made lowercase.
    eventtypeid = models.ForeignKey('Eventtype', models.DO_NOTHING, db_column='EVENTTYPEID')  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CALENDAREVENT'


class Company(models.Model):
    campanyid = models.AutoField(db_column='CAMPANYID', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='COMPANYNAME', max_length=500, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMPANY'


class Correlation(models.Model):
    marketdataid = models.OneToOneField('Marketdata', models.DO_NOTHING, db_column='MARKETDATAID', primary_key=True)  # Field name made lowercase.
    value = models.TextField(db_column='VALUE', db_collation='French_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CORRELATION'


class Correlationforex(models.Model):
    correlationforexid = models.OneToOneField(Correlation, models.DO_NOTHING, db_column='CORRELATIONFOREXID', primary_key=True)  # Field name made lowercase.
    forexmarketdataid = models.ForeignKey('Forexmarketdata', models.DO_NOTHING, db_column='FOREXMARKETDATAID')  # Field name made lowercase.
    underlyingid = models.ForeignKey('Underlying', models.DO_NOTHING, db_column='UNDERLYINGID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CORRELATIONFOREX'


class Correlationunderlying(models.Model):
    correlationunderlyingid = models.OneToOneField(Correlation, models.DO_NOTHING, db_column='CORRELATIONUNDERLYINGID', primary_key=True)  # Field name made lowercase.
    underlyingid1 = models.ForeignKey('Underlying', models.DO_NOTHING, db_column='UNDERLYINGID1', related_name='correlations1')
    underlyingid2 = models.ForeignKey('Underlying', models.DO_NOTHING, db_column='UNDERLYINGID2', related_name='correlations2')

    class Meta:
        managed = False
        db_table = 'CORRELATIONUNDERLYING'


class Currency(models.Model):
    currencyid = models.AutoField(db_column='CURRENCYID', primary_key=True)  # Field name made lowercase.
    symbol = models.CharField(db_column='SYMBOL', max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=500, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CURRENCY'


class Dividendmarketdata(models.Model):
    marketdataid = models.OneToOneField('Underlyingmarketdata', models.DO_NOTHING, db_column='MARKETDATAID', primary_key=True)  # Field name made lowercase.
    value = models.TextField(db_column='VALUE', db_collation='French_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'DIVIDENDMARKETDATA'


class Eventtype(models.Model):
    eventtypeid = models.AutoField(db_column='EVENTTYPEID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=500, db_collation='French_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENTTYPE'


class Forexmarketdata(models.Model):
    marketdataid = models.IntegerField(db_column='MARKETDATAID', primary_key=True)  # Field name made lowercase.
    currencyid1 = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CURRENCYID1', related_name='forex_data1')
    currencyid2 = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CURRENCYID2', related_name='forex_data2')
    spotvalue = models.FloatField(db_column='SPOTVALUE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FOREXMARKETDATA'


class Market(models.Model):
    marketid = models.AutoField(db_column='MARKETID', primary_key=True)  # Field name made lowercase.
    currencyid = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CURRENCYID')  # Field name made lowercase.
    symbol = models.CharField(db_column='SYMBOL', max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=500, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MARKET'


class Marketdata(models.Model):
    marketdataid = models.AutoField(db_column='MARKETDATAID', primary_key=True)  # Field name made lowercase.
    insertiondate = models.TextField(db_column='INSERTIONDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    date = models.DateTimeField(db_column='DATE')  # Field name made lowercase.
    iscutoff = models.BooleanField(db_column='ISCUTOFF')  # Field name made lowercase.
    parametersetpersonalid = models.ForeignKey('Parameterset', models.DO_NOTHING, db_column='PARAMETERSETPERSONALID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MARKETDATA'


class Parameterset(models.Model):
    personalid = models.AutoField(db_column='PERSONALID', primary_key=True)  # Field name made lowercase.
    parametersetname = models.TextField(db_column='PARAMETERSETNAME', db_collation='French_CI_AS')  # Field name made lowercase.
    user_uid = models.ForeignKey('User', models.DO_NOTHING, db_column='USER_UID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PARAMETERSET'


class Repomarketdata(models.Model):
    marketdataid = models.OneToOneField('Underlyingmarketdata', models.DO_NOTHING, db_column='MARKETDATAID', primary_key=True)  # Field name made lowercase.
    value = models.TextField(db_column='VALUE', db_collation='French_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'REPOMARKETDATA'


class Riskfreerateserie(models.Model):
    marketdataid = models.OneToOneField(Marketdata, models.DO_NOTHING, db_column='MARKETDATAID', primary_key=True)  # Field name made lowercase.
    currencyid = models.ForeignKey(Currency, models.DO_NOTHING, db_column='CURRENCYID')  # Field name made lowercase.
    value = models.TextField(db_column='VALUE', db_collation='French_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'RISKFREERATESERIE'


class Spotmarketdata(models.Model):
    marketdataid = models.OneToOneField('Underlyingmarketdata', models.DO_NOTHING, db_column='MARKETDATAID', primary_key=True)  # Field name made lowercase.
    spotvalue = models.FloatField(db_column='SPOTVALUE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SPOTMARKETDATA'


class TmpDatarequest(models.Model):
    request_id = models.IntegerField(db_column='REQUEST_ID', primary_key=True)  # Field name made lowercase.
    symbol = models.CharField(db_column='SYMBOL', max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    marketsymbol = models.CharField(db_column='MARKETSYMBOL', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMP_DATAREQUEST'


class TmpForexDatarequest(models.Model):
    request_id = models.IntegerField(db_column='REQUEST_ID', primary_key=True)  # Field name made lowercase.
    currency1 = models.CharField(db_column='CURRENCY1', max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    currency2 = models.CharField(db_column='CURRENCY2', max_length=50, db_collation='French_CI_AS')  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMP_FOREX_DATAREQUEST'


class Underlying(models.Model):
    underlyingid = models.AutoField(db_column='UNDERLYINGID', primary_key=True)  # Field name made lowercase.
    marketid = models.ForeignKey(Market, models.DO_NOTHING, db_column='MARKETID')  # Field name made lowercase.
    campanyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='CAMPANYID')  # Field name made lowercase.
    symbol = models.CharField(db_column='SYMBOL', max_length=50, db_collation='French_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UNDERLYING'


class Underlyingmarketdata(models.Model):
    marketdataid = models.OneToOneField(Marketdata, models.DO_NOTHING, db_column='MARKETDATAID', primary_key=True)  # Field name made lowercase.
    underlyingid = models.ForeignKey(Underlying, models.DO_NOTHING, db_column='UNDERLYINGID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UNDERLYINGMARKETDATA'


class User(models.Model):
    uid = models.AutoField(db_column='UID', primary_key=True)  # Field name made lowercase.
    username = models.TextField(db_column='USERNAME', db_collation='French_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER'


class Volatilitymarketdata(models.Model):
    marketdataid = models.OneToOneField(Underlyingmarketdata, models.DO_NOTHING, db_column='MARKETDATAID', primary_key=True)  # Field name made lowercase.
    value = models.TextField(db_column='VALUE', db_collation='French_CI_AS')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'VOLATILITYMARKETDATA'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='French_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='French_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='French_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='French_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='French_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='French_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='French_CI_AS')
    email = models.CharField(max_length=254, db_collation='French_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='French_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='French_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='French_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='French_CI_AS')
    model = models.CharField(max_length=100, db_collation='French_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='French_CI_AS')
    name = models.CharField(max_length=255, db_collation='French_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='French_CI_AS')
    session_data = models.TextField(db_collation='French_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='French_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
