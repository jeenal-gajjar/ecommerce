import os
import sys

# Below Environment should exist in os.
#  If below listed env variables are not found, then an error is raised.
#  No need of assert statement. Just make sure variable is in list below

self = sys.modules[__name__]
ENVIRON_VARIABLES = [
    'ENVIRON',
    'PRODUCTION',
    'DEV',
    'LOCAL',
    'DEBUG',
    'SECRET_KEY',
    'DB_NAME',
    'DB_USERNAME',
    'DB_PASSWORD',
    'DB_HOST',
    'DB_PORT',
    'SLACK_SECRET_KEY',
]
for env in ENVIRON_VARIABLES:
    value = os.environ[env]

    if value.isdigit():
        value = int(value)
    setattr(self, env, value)
