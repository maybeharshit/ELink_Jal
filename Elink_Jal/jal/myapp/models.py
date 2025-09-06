# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class MApplicationForm(models.Model):
    form_id = models.BigAutoField(primary_key=True)
    module_id = models.IntegerField()
    form_name = models.CharField(max_length=200)
    menu_id = models.IntegerField()
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_application_form'


class MEquipment(models.Model):
    equipment_id = models.BigAutoField(primary_key=True)
    equipment_name = models.CharField(max_length=255)
    equipment_type_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()
    equip_icon_image_name = models.CharField(max_length=200, blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_equipment'


class MEquipmentType(models.Model):
    equipment_type_id = models.BigAutoField(primary_key=True)
    equipment_type_description = models.CharField(max_length=255)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_equipment_type'


class MLocation(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    location_name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    loc_latitude = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    loc_longitude = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    radius_area_mts = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_location'


class MMenu(models.Model):
    menu_id = models.BigAutoField(primary_key=True)
    menu_name = models.CharField(max_length=200)
    display_order = models.IntegerField(blank=True, null=True)
    parent_menu_id = models.IntegerField(blank=True, null=True)
    form_id = models.IntegerField(blank=True, null=True)
    action_name = models.CharField(max_length=200, blank=True, null=True)
    controller_name = models.CharField(max_length=200, blank=True, null=True)
    menu_icon_class = models.CharField(max_length=200, blank=True, null=True)
    is_default = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_access = models.BooleanField(blank=True, null=True)
    is_add = models.BooleanField(blank=True, null=True)
    is_edit = models.BooleanField(blank=True, null=True)
    is_delete = models.BooleanField(blank=True, null=True)
    route_url = models.CharField(max_length=500, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_menu'


class MModule(models.Model):
    module_id = models.BigAutoField(primary_key=True)
    module_name = models.CharField(max_length=200, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_module'


class MParameter(models.Model):
    parameter_id = models.BigAutoField(primary_key=True)
    parameter_description = models.CharField(max_length=255)
    parameter_value_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_parameter'


class MParameterMeasure(models.Model):
    parameter_measure_id = models.BigAutoField(primary_key=True)
    parameter_measure_unit = models.CharField(max_length=100)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_parameter_measure'


class MParameterValue(models.Model):
    parameter_value_id = models.BigAutoField(primary_key=True)
    parameter_value_description = models.CharField(max_length=255)
    parameter_measure_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'm_parameter_value'


class MRole(models.Model):
    role_id = models.BigAutoField(primary_key=True)
    role_description = models.CharField(max_length=255)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_role'


class MState(models.Model):
    sm_state_id = models.IntegerField(primary_key=True)
    sm_state_name = models.CharField(max_length=20)
    sm_visible = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    sm_modified_date = models.DateTimeField(blank=True, null=True)
    sm_modified_by = models.CharField(max_length=25, blank=True, null=True)
    sm_ip_addr = models.CharField(max_length=15, blank=True, null=True)
    sm_remarks = models.CharField(max_length=2000, blank=True, null=True)
    sm_state_hindi = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_state'


class MSubLocation(models.Model):
    sub_location_id = models.BigAutoField(primary_key=True)
    sub_location_name = models.CharField(max_length=100)
    location_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()
    s_loc_latitude = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    s_loc_longitude = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_sub_location'


class MUser(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    email_id = models.CharField(max_length=100)
    primary_mobile_number = models.CharField(max_length=100)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    role_id = models.IntegerField()
    user_password = models.CharField(max_length=50)
    secondary_mobile_number = models.CharField(max_length=100, blank=True, null=True)
    user_address_1 = models.CharField(max_length=255)
    user_address_2 = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()
    last_login = models.DateField(blank=True, null=True)
    login_count = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)
    employment_type_id = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    conractor_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    designation_id = models.IntegerField(blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    qualification_id = models.IntegerField(blank=True, null=True)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    pincode = models.CharField(max_length=50, blank=True, null=True)
    emergency_number = models.CharField(max_length=100, blank=True, null=True)
    contact_person_name = models.CharField(max_length=255, blank=True, null=True)
    contact_person_relation = models.CharField(max_length=100, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    location_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_user'


class TEquipmentLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipment_id = models.IntegerField(blank=True, null=True)
    sub_location_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)
    manufacturer_name = models.CharField(max_length=200, blank=True, null=True)
    model_number = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    equip_latitude = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    equip_longitude = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_equipment_location'


class TEquipmentTypeParameterValueMeasure(models.Model):
    id = models.BigAutoField(primary_key=True)
    equipment_id = models.IntegerField(blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    parameter_id = models.IntegerField(blank=True, null=True)
    value_id = models.IntegerField(blank=True, null=True)
    measure_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_equipment_type_parameter_value_measure'


class TLocationSublocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    location_id = models.IntegerField(blank=True, null=True)
    sub_location_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_location_sublocation'


class TRoleRight(models.Model):
    role_right_id = models.BigAutoField(primary_key=True)
    role_id = models.IntegerField(blank=True, null=True)
    form_id = models.IntegerField(blank=True, null=True)
    is_access = models.BooleanField(blank=True, null=True)
    is_add = models.BooleanField(blank=True, null=True)
    is_edit = models.BooleanField(blank=True, null=True)
    is_delete = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()
    modified_date = models.DateField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_role_right'


class TUserLocation(models.Model):
    user_location_id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    sub_location_id = models.IntegerField()
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()
    modified_date = models.DateField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_location'


class TUserRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    role_id = models.IntegerField()
    is_deleted = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_role'
