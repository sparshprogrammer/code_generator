from odoo.models import OdooReport
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender= OdooReport)
def save_odoo_report(sender, instance, created, **kwargs):
    if created:
        print(instance.model_name)
        print("Signals Working")
        class_name = instance.model_name.replace('.', '').replace('_', '').upper()
        fname = 'generated.py'
        data = """
from odoo import fields, models, api, _

            
class """ + class_name + """(models.Model):
    _name = '""" + instance.model_name + """'"""
        with open(fname, 'w') as f:
            f.write(data)
