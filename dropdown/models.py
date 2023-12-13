from django.db import models
# Create your models here.



#xsup

# class banking_account_type(models.Model):
#     title = models.CharField(max_length=200, null=True)

class business_type(models.Model):
    title = models.CharField(max_length=200, null=True)

class firm_type(models.Model):
    title = models.CharField(max_length=200, null=True)

# class prop_dir(models.Model):
#     title = models.CharField(max_length=200, null=True)

# class prop_dir_designation(models.Model):
#     title = models.CharField(max_length=200, null=True)

# class cities(models.Model):
#     city = models.CharField(max_length=300, null=True)
#     state = models.CharField(max_length=300, null=True)
#     coutry = models.CharField(max_length=300, null=True)

class decision(models.Model):
    title = models.CharField(max_length=200, null=True)

# class ev_departments(models.Model):
#     title = models.CharField(max_length=200, null=True)
#     sub_department = models.CharField(max_length=200, null=True)
#     created_by = models.CharField(max_length=500, null=True)

class dropdown_fields(models.Model):
    dropdown_fields = models.CharField(max_length=500, null=True)
    ref_tb = models.CharField(max_length=500, null=True)



class ev_services(models.Model):
    country = models.CharField(max_length=300, null=True)
    marketplace = models.CharField(max_length=300, null=True)
    services = models.CharField(max_length=300, null=True)
    slab = models.CharField(max_length=300, null=True)
    static_service_fees = models.CharField(max_length=300, null=True)
    percentage_service_fees = models.CharField(max_length=300, null=True)
    service_currency = models.CharField(max_length=300, null=True)

class contact_preference(models.Model):
    title = models.CharField(max_length=200, null=True)


    
    # CharField(max_length=500, null=True)

# class ev_admin(models.Model):
#     title = models.CharField(max_length=200, null=True)
#     created_by = models.CharField(max_length=500, null=True)
    
class ev_bank_details(models.Model):
    account_name = models.CharField(max_length=200, null=True)
    bank_name = models.CharField(max_length=500, null=True)
    account_number = models.CharField(max_length=200, null=True)
    ifsc = models.CharField(max_length=500, null=True)
    
class ev_branch_location(models.Model):
    title = models.CharField(max_length=500, null=True)
    location = models.CharField(max_length=200, null=True)
    created_by = models.CharField(max_length=500, null=True)

class ev_products(models.Model):
    title = models.CharField(max_length=500, null=True)
    department = models.CharField(max_length=200, null=True)
    created_by = models.CharField(max_length=500, null=True)

# class ev_commercials(models.Model):
#     platform = models.CharField(max_length=500, null=True)
#     service_country = models.CharField(max_length=200, null=True)
#     service_category = models.CharField(max_length=500, null=True)

class ev_department_designation(models.Model):
    title = models.CharField(max_length=500, null=True)
    designation = models.CharField(max_length=200, null=True)
    created_by = models.CharField(max_length=500, null=True)

class ev_employee_status(models.Model):
    title = models.CharField(max_length=500, null=True)
    created_by = models.CharField(max_length=500, null=True)

# class ev_super_admin(models.Model):
#     title = models.CharField(max_length=500, null=True)
#     created_by = models.CharField(max_length=500, null=True)


# class ev_team_leader(models.Model):
#     title = models.CharField(max_length=500, null=True)
#     marketplace = models.CharField(max_length=500, null=True)
#     segment = models.CharField(max_length=500, null=True)
#     created_by = models.CharField(max_length=500, null=True)

# class ev_team_manager(models.Model):
#     title = models.CharField(max_length=500, null=True)
#     created_by = models.CharField(max_length=500, null=True)

class user_links(models.Model):
    title = models.CharField(max_length=500, default='', blank=True)
    link_type = models.CharField(max_length=500, default='', blank=True)
    user_link = models.CharField(max_length=500, default='', blank=True)
    access_department = models.CharField(max_length=500, default='', blank=True)
    table_ref = models.CharField(max_length=500, default='', blank=True)
    link_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class service_category(models.Model):
    title = models.CharField(max_length=500, null=True)

class service_country(models.Model):
    title = models.CharField(max_length=500, null=True)

class user_role(models.Model):
    title = models.CharField(max_length=500, null=True)

class gender(models.Model):
    title = models.CharField(max_length=500, null=True)

class lead_status(models.Model):
    title = models.CharField(max_length=500, null=True)

# class marital_status(models.Model):
#     title = models.CharField(max_length=500, null=True)

class not_interested_reason(models.Model):
    title = models.CharField(max_length=500, null=True)

class unresponsive_reason(models.Model):
    title = models.CharField(max_length=500, null=True)

class list_business_leads(models.Model):
    table_name = models.CharField(max_length=500, null=True)
    table_type = models.CharField(max_length=500, null=True)
    table_atr = models.CharField(max_length=500, null=True)

class list_client(models.Model):
    table_name = models.CharField(max_length=500, null=True)
    table_type = models.CharField(max_length=500, null=True)
    table_atr = models.CharField(max_length=500, null=True)

class list_employee(models.Model):
    table_name = models.CharField(max_length=500, null=True)
    table_type = models.CharField(max_length=500, null=True)
    table_atr = models.CharField(max_length=500, null=True)


class image_src(models.Model):
    title = models.CharField(max_length=100, null=True)
    src = models.TextField(null=True)
    status = models.BooleanField(default=True)


# class ref_service_country(models.Model):
#     title = models.CharField(max_length=150, null=True)