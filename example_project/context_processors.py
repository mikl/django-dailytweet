from django.conf import settings
from django.contrib.sites.models import Site

def site_info(request):
    """
    Provide site-specific context variables.

    Expose the STATIC_URL setting and the current site from the sites
    framework from django.contrib.
    """
    return {
        'STATIC_URL': getattr(settings,'STATIC_URL', ''),
        'SITE': Site.objects.get_current(),
    }

