# Generated by Django 5.1.3 on 2025-01-05 19:19

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_msg', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('featured', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('feedback', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Discover Your Next Favorite Product', max_length=500)),
                ('description', models.TextField(default='Shop our latest collections and exclusive offers')),
                ('button_text', models.CharField(default='Shop Now', max_length=50)),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='hero_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CouponUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_at', models.DateTimeField(auto_now_add=True)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.coupon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default='-', null=True, upload_to='profile_pic/CustomerProfilePic/')),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HeroSectionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hero_images/')),
                ('hero_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ecom.herosection')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=100, unique=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Order Confirmed', 'Order Confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=50)),
                ('order_date', models.DateField(auto_now_add=True, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('address_line_1', models.CharField(max_length=500, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('zip_code', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('payment_method', models.CharField(max_length=50, null=True)),
                ('delivery_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('product_image', models.ImageField(blank=True, default='-', null=True, upload_to='product_image/')),
                ('additional_image1', models.ImageField(blank=True, null=True, upload_to='product_image/other/')),
                ('additional_image2', models.ImageField(blank=True, null=True, upload_to='product_image/other/')),
                ('additional_image3', models.ImageField(blank=True, null=True, upload_to='product_image/other/')),
                ('additional_image4', models.ImageField(blank=True, null=True, upload_to='product_image/other/')),
                ('price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(blank=True, help_text='Discount Price', null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('short_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('is_digital', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('popular', models.BooleanField(default=False)),
                ('free_delivery', models.BooleanField(default=False)),
                ('priority', models.IntegerField(default=1000)),
                ('popular_priority', models.IntegerField(default=1000)),
                ('feautered_priority', models.IntegerField(default=1000)),
                ('exclusive', models.BooleanField(default=False, help_text='Select this product to display exclusively')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecom.category')),
                ('colors', models.ManyToManyField(blank=True, related_name='products', to='ecom.color')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ecom.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.product')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='ecom.category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecom.sub_category'),
        ),
    ]
