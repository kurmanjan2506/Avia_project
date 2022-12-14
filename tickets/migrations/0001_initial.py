

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_city', models.CharField(max_length=100)),
                ('to_city', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('count_of_product', models.SmallIntegerField(blank=True, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='tickets.company')),
            ],
        ),
    ]
