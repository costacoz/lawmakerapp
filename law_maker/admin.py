"""Custom admin site"""
from django.contrib import admin


class CustomAdminSite(admin.AdminSite):
    """Custom admin site class"""
    site_header = 'Law Maker administration panel'
    site_title = 'Law Maker admin panel'
