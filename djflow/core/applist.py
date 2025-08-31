BEFORE_DJANGO_APPS = (
    'tenant_schemas',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# apps local do projeto
LOCAL_APPS = (
    'tenant',
    'flow',
    'website',
    'security',
)

THIRD_PARTY_APPS = (
    'solo',
    'sslserver',
)

# Compartilhado com todos os tentant
SHARED_APPS = (
    'tenant_schemas',
    'tenant',
    'website',
    'security',
) + DJANGO_APPS

# Aps de cada tenant
TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
) + LOCAL_APPS

INSTALLED_APPS = BEFORE_DJANGO_APPS + DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
