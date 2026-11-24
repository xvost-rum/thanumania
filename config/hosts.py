from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns('',
    host(r'game', 'config.urls_game', name='game'),
    host(r'www', settings.ROOT_URLCONF, name='www'),
)
    