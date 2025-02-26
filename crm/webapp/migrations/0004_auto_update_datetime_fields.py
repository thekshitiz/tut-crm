from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_client_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ] 