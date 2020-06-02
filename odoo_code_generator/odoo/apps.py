from django.apps import AppConfig


class OdooConfig(AppConfig):
    name = 'odoo'

    def ready(self):
        import odoo.signals