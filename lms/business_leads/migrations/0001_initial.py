# Generated by Django 4.2.6 on 2023-12-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_identifiers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.CharField(blank=True, default='-', max_length=100)),
                ('marketplace', models.CharField(blank=True, default='-', max_length=100)),
                ('request_id', models.CharField(blank=True, default='-', max_length=150)),
                ('provider_id', models.CharField(blank=True, default='-', max_length=150)),
                ('service_requester_type', models.CharField(blank=True, default='-', max_length=200)),
                ('requester_name', models.CharField(blank=True, default='-', max_length=100)),
                ('requester_id', models.CharField(blank=True, default='-', max_length=150)),
                ('phone_number', models.CharField(blank=True, default='-', max_length=50)),
                ('email_id', models.CharField(blank=True, default='-', max_length=100)),
                ('city', models.CharField(blank=True, default='-', max_length=100)),
                ('created_date', models.CharField(blank=True, default='-', max_length=200)),
                ('service_category', models.CharField(blank=True, default='-', max_length=200)),
                ('requester_location', models.CharField(blank=True, default='-', max_length=200)),
                ('requester_sell_in_country', models.CharField(blank=True, default='-', max_length=200)),
                ('current_status', models.CharField(blank=True, default='-', max_length=200)),
                ('change_status_to', models.CharField(blank=True, default='-', max_length=200)),
                ('shipment_id', models.CharField(blank=True, default='-', max_length=200)),
                ('fulfillment_center', models.CharField(blank=True, default='-', max_length=200)),
                ('delivery_date', models.CharField(blank=True, default='-', max_length=200)),
                ('total_weight', models.CharField(blank=True, default='-', max_length=200)),
                ('shipment_tracking_id_awb', models.CharField(blank=True, default='-', max_length=200)),
                ('pickup_pincode', models.CharField(blank=True, default='-', max_length=200)),
                ('followup_date', models.CharField(blank=True, default='-', max_length=200)),
                ('pitch_in_progress_request_status_reason_code', models.CharField(blank=True, default='-', max_length=200)),
                ('not_interested_request_status_reason_code', models.CharField(blank=True, default='-', max_length=200)),
                ('not_reachable_request_status_reason_code', models.CharField(blank=True, default='-', max_length=200)),
                ('cancelled_request_status_reason_code', models.CharField(blank=True, default='-', max_length=200)),
                ('sales_manager', models.CharField(blank=True, default='-', max_length=200)),
                ('comments', models.CharField(blank=True, default='-', max_length=200)),
                ('amazon_comments', models.CharField(blank=True, default='-', max_length=200)),
                ('note_from_requester', models.TextField(blank=True, default='-')),
                ('account_manager', models.CharField(blank=True, default='-', max_length=200)),
                ('start_date_pickup_date', models.CharField(blank=True, default='-', max_length=200)),
                ('end_date', models.CharField(blank=True, default='-', max_length=200)),
                ('type_of_service_offered', models.CharField(blank=True, default='-', max_length=200)),
                ('mode_of_training', models.CharField(blank=True, default='-', max_length=200)),
                ('number_of_products_model_shoot', models.CharField(blank=True, default='-', max_length=200)),
                ('number_of_products_table_top', models.CharField(blank=True, default='-', max_length=200)),
                ('number_of_products_editing', models.CharField(blank=True, default='-', max_length=200)),
                ('number_of_products_cataloging_ebc_compliance', models.CharField(blank=True, default='-', max_length=200)),
                ('date_of_filing_poa', models.CharField(blank=True, default='-', max_length=200)),
                ('test_result', models.CharField(blank=True, default='-', max_length=200)),
                ('trademark_type', models.CharField(blank=True, default='-', max_length=200)),
                ('trademark_serial_number', models.CharField(blank=True, default='-', max_length=200)),
                ('trademark_pto', models.CharField(blank=True, default='-', max_length=200)),
                ('actual_date_of_reaching_destination_port', models.CharField(blank=True, default='-', max_length=200)),
                ('date_of_shipping_out_of_origin_port', models.CharField(blank=True, default='-', max_length=200)),
                ('container_number', models.CharField(blank=True, default='-', max_length=200)),
                ('order_date', models.CharField(blank=True, default='-', max_length=200)),
                ('estimated_dispatch_date_sample', models.CharField(blank=True, default='-', max_length=200)),
                ('assured_delivery_date', models.CharField(blank=True, default='-', max_length=200)),
                ('production_start_date', models.CharField(blank=True, default='-', max_length=200)),
                ('dispatch_date', models.CharField(blank=True, default='-', max_length=200)),
                ('interest_rate', models.CharField(blank=True, default='-', max_length=200)),
                ('loan_amount', models.CharField(blank=True, default='-', max_length=200)),
                ('loan_tenure_in_months', models.CharField(blank=True, default='-', max_length=200)),
                ('processing_fee', models.CharField(blank=True, default='-', max_length=200)),
                ('pre_closure_charges', models.CharField(blank=True, default='-', max_length=200)),
                ('upload_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='business_identifiers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.CharField(blank=True, default='-', max_length=500)),
                ('business_name', models.CharField(blank=True, default='-', max_length=500)),
                ('business_type', models.CharField(blank=True, default='-', max_length=500)),
                ('business_category', models.CharField(blank=True, default='-', max_length=500)),
                ('brand_name', models.CharField(blank=True, default='-', max_length=500)),
                ('firm_type', models.CharField(blank=True, default='-', max_length=500)),
                ('name_for_mou', models.CharField(blank=True, default='-', max_length=500)),
                ('designation', models.CharField(blank=True, default='-', max_length=500)),
                ('turnover', models.CharField(blank=True, default='-', max_length=500)),
                ('monthly_sales', models.CharField(blank=True, default='-', max_length=500)),
                ('gst', models.CharField(blank=True, default='-', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.CharField(blank=True, default='-', max_length=500)),
                ('comment', models.CharField(blank=True, default='-', max_length=500)),
                ('comment_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='contact_preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.CharField(blank=True, default='-', max_length=500)),
                ('contact_preference', models.CharField(blank=True, default='-', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='followup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.CharField(blank=True, default='-', max_length=50)),
                ('followup_date', models.DateField(null=True)),
                ('followup_time', models.TimeField(null=True)),
                ('followup_notes', models.TextField(blank=True, default='-')),
                ('created_by', models.CharField(blank=True, default='-', max_length=50)),
                ('service_category', models.CharField(blank=True, default='-', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='seller_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.CharField(blank=True, default='-', max_length=50)),
                ('address_line1', models.CharField(blank=True, default='-', max_length=50)),
                ('address_line2', models.CharField(blank=True, default='-', max_length=50)),
                ('country', models.CharField(blank=True, default='-', max_length=50)),
                ('state', models.CharField(blank=True, default='-', max_length=50)),
                ('city', models.CharField(blank=True, default='-', max_length=50)),
                ('pin_code', models.CharField(blank=True, default='-', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.CharField(blank=True, default='-', max_length=50)),
                ('platform', models.CharField(blank=True, default='-', max_length=50)),
                ('service_country', models.CharField(blank=True, default='-', max_length=50)),
                ('service_category', models.CharField(blank=True, default='-', max_length=50)),
                ('service_name', models.CharField(blank=True, default='-', max_length=50)),
                ('team_leader', models.CharField(blank=True, default='-', max_length=50)),
                ('team_leader_id', models.CharField(blank=True, default='-', max_length=50)),
                ('associate', models.CharField(blank=True, default='-', max_length=50)),
                ('associate_id', models.CharField(blank=True, default='-', max_length=50)),
                ('lead_status', models.CharField(blank=True, default='-', max_length=50)),
                ('lead_status_reason', models.CharField(blank=True, default='-', max_length=50)),
                ('fees_slab', models.CharField(blank=True, default='-', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='website_store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.CharField(blank=True, default='-', max_length=50)),
                ('seller_website', models.CharField(blank=True, default='-', max_length=50)),
                ('amazon_store_link', models.CharField(blank=True, default='-', max_length=50)),
                ('facebook_store_link', models.CharField(blank=True, default='-', max_length=50)),
                ('instagram_store_link', models.CharField(blank=True, default='-', max_length=50)),
            ],
        ),
    ]
