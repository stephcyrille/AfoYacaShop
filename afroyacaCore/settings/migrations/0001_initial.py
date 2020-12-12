# Generated by Django 2.0 on 2020-12-11 13:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreTrackedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_archived', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('coretrackedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='settings.CoreTrackedModel')),
                ('name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('subTitle', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('linkText', models.CharField(max_length=250)),
                ('linkUrl', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('picture', models.FileField(blank=True, null=True, upload_to='banner')),
                ('is_home', models.BooleanField(default=False)),
            ],
            bases=('settings.coretrackedmodel',),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('coretrackedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='settings.CoreTrackedModel')),
                ('address', models.CharField(max_length=200)),
                ('address_precision', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('main', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile')),
            ],
            bases=('settings.coretrackedmodel',),
        ),
        migrations.CreateModel(
            name='MainMenuNavPicture',
            fields=[
                ('coretrackedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='settings.CoreTrackedModel')),
                ('clothing', models.FileField(blank=True, null=True, upload_to='main_menu_nav')),
                ('shoes', models.FileField(blank=True, null=True, upload_to='main_menu_nav')),
                ('bag', models.FileField(blank=True, null=True, upload_to='main_menu_nav')),
                ('accessory', models.FileField(blank=True, null=True, upload_to='main_menu_nav')),
                ('jewelery', models.FileField(blank=True, null=True, upload_to='main_menu_nav')),
                ('lingerie', models.FileField(blank=True, null=True, upload_to='main_menu_nav')),
                ('beauty', models.FileField(blank=True, null=True, upload_to='main_menu_nav')),
                ('editorial', models.FileField(blank=True, null=True, upload_to='main_menu_nav')),
            ],
            bases=('settings.coretrackedmodel',),
        ),
        migrations.CreateModel(
            name='SeoPage',
            fields=[
                ('coretrackedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='settings.CoreTrackedModel')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('keywords', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('url', models.TextField()),
                ('picture', models.FileField(blank=True, null=True, upload_to='seo')),
            ],
            bases=('settings.coretrackedmodel',),
        ),
        migrations.AddField(
            model_name='coretrackedmodel',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='account.UserProfile'),
        ),
        migrations.AddField(
            model_name='coretrackedmodel',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='account.UserProfile'),
        ),
    ]
