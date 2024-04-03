# Generated by Django 3.1.5 on 2021-03-03 12:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0038_auto_20210301_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_master',
            name='attendance_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='attendance_master',
            name='time_in',
            field=models.TimeField(help_text='Coming Time'),
        ),
        migrations.AlterField(
            model_name='attendance_master',
            name='time_out',
            field=models.TimeField(help_text='Leaving Time'),
        ),
        migrations.AlterField(
            model_name='feedback_master',
            name='details',
            field=models.TextField(help_text='Feedback Description'),
        ),
        migrations.AlterField(
            model_name='feedback_master',
            name='feedback_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='feedback_master',
            name='ratings',
            field=models.IntegerField(help_text='Must be less than or equal to 10 \n 10:- Highest Rating \n 1:- Lowest Ratings', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='membership_master',
            name='amount',
            field=models.IntegerField(help_text='Price Must Be Less than 99999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='membership_master',
            name='details',
            field=models.TextField(help_text='Description of Membership'),
        ),
        migrations.AlterField(
            model_name='membership_master',
            name='end_date',
            field=models.DateField(help_text='Ending Date of Membership'),
        ),
        migrations.AlterField(
            model_name='membership_master',
            name='membership_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='membership_master',
            name='membership_status',
            field=models.BooleanField(help_text='Approved or Not'),
        ),
        migrations.AlterField(
            model_name='membership_master',
            name='start_date',
            field=models.DateField(help_text='Starting Date of Membership'),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='delivery_date',
            field=models.DateField(help_text='Date of Delivery'),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='delivery_status',
            field=models.BooleanField(help_text='Status of Delivery:- Deliverd or not'),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='order_details_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='price',
            field=models.IntegerField(help_text='Price Must Be Less than 99999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='qty',
            field=models.IntegerField(help_text='Quantity must be less than 100', validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='tot_amt',
            field=models.IntegerField(help_text='Price Must Be Less than 99999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='order_master',
            name='ord_date',
            field=models.DateField(help_text='Date of Placing Order'),
        ),
        migrations.AlterField(
            model_name='order_master',
            name='order_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='payment_master',
            name='amount',
            field=models.IntegerField(help_text='Amount Must Be Less than 99999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='payment_master',
            name='method',
            field=models.CharField(choices=[('Google Pay', 'Gpay'), ('Paytm', 'Paytm'), ('Cash', 'Cash')], help_text='Choose Method of Making Payment', max_length=15),
        ),
        migrations.AlterField(
            model_name='payment_master',
            name='payment_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='payment_master',
            name='payment_status',
            field=models.BooleanField(help_text='Payment Approved or not'),
        ),
        migrations.AlterField(
            model_name='payment_master',
            name='transaction_no',
            field=models.CharField(help_text='Must be a Valid Transaction Number', max_length=40),
        ),
        migrations.AlterField(
            model_name='plan_master',
            name='details',
            field=models.TextField(help_text='Description of Plan'),
        ),
        migrations.AlterField(
            model_name='plan_master',
            name='plan_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='plan_master',
            name='price',
            field=models.IntegerField(help_text='Price Must Be Less than 99999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='plan_master',
            name='title',
            field=models.CharField(choices=[('Basic Plan', 'Basic Plan'), ('Standard Plan', 'Standard Plan'), ('Ultimate Plan', 'Ultimate Plan')], help_text='Choose Type of Plan', max_length=15),
        ),
        migrations.AlterField(
            model_name='product_master',
            name='details',
            field=models.TextField(help_text='Description of Product'),
        ),
        migrations.AlterField(
            model_name='product_master',
            name='price',
            field=models.IntegerField(help_text='Price Must Be Less than 99999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product_master',
            name='product_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='product_master',
            name='product_name',
            field=models.CharField(help_text='Must be of length less than 25', max_length=25),
        ),
        migrations.AlterField(
            model_name='product_master',
            name='qty',
            field=models.IntegerField(help_text='Quantity must be less than 100', validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='trainer_details',
            name='Details',
            field=models.TextField(help_text='Additional Details About Trainer'),
        ),
        migrations.AlterField(
            model_name='trainer_details',
            name='salary',
            field=models.IntegerField(help_text='Salary of Trainer \n Must be less than 99999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='trainer_details',
            name='trainer_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='email',
            field=models.EmailField(help_text='Must Contain @ and .', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='id_proof',
            field=models.FileField(help_text='Any Government Approved Id(Aadhar/Driving License/PAN Card/Voter Id) \n Must be .pdf File Only \n Maximum Size 2MB', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='mname',
            field=models.CharField(help_text='Name of the User \n Must Be Within 25 Characters \n Enter Alphabets Only', max_length=25),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='mobile',
            field=models.CharField(help_text='Mobile no. must be of 10 Digits', max_length=10),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='password',
            field=models.CharField(help_text='Password Must be of 6 to 16 Characters ', max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='photo',
            field=models.FileField(help_text='Image File of User \n Must of be .jpg or .png \n Maximum Size 1MB', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='user_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='user_type',
            name='type_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='user_type',
            name='utype',
            field=models.CharField(choices=[('Trainer', 'Trainer'), ('Member', 'Member')], help_text='Type of User', max_length=7),
        ),
        migrations.AlterField(
            model_name='workout_master',
            name='diet_chart',
            field=models.FileField(help_text='Must be pdf file \n Maximum size:- 1MB ', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='workout_master',
            name='rewards',
            field=models.IntegerField(help_text='Must be less than 9999', validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='workout_master',
            name='videos',
            field=models.FileField(help_text='Must be of .mp4 Extension \n Maximum Size must be 300MB', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
        migrations.AlterField(
            model_name='workout_master',
            name='workout_id',
            field=models.IntegerField(help_text='Id Must Be Between 10000 to 99999', primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='workout_master',
            name='workout_schedule',
            field=models.FileField(help_text='Must be pdf file \n Maximum size:- 1MB ', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
