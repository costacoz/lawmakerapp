""" Project apps """
from django.contrib.admin.apps import AdminConfig


class CustomAdminConfig(AdminConfig):
    """CustomAdminConfig"""
    default_site = 'law_maker.admin.CustomAdminSite'
