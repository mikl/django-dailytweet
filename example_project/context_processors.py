from django.conf import settings

def site_info(request):
    """
    Provide site-specific context variables.

    In this case, we just make our own STATIC_URL available.
    """
    return {
        'STATIC_URL': getattr(settings,'STATIC_URL', ''),
    }

