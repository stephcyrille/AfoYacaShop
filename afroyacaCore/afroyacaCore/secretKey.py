import os
AYD_APP_BASE_DIR = ''.join([os.path.dirname(os.path.dirname(__file__)), '/afroyacaCore'])

# Use a separate file for configurations
with open(os.path.join(AYD_APP_BASE_DIR, 'settings.txt')) as f:
    for setting in f.read().strip().split(';'):
        if 'AYD_ENV' == setting.split(':')[0]:
            AYD_ENV = setting.split(':')[1]
        elif 'AYD_DB_NAME' == setting.split(':')[0]:
            AYD_DB_NAME = setting.split(':')[1]
        elif 'AYD_DB_USER' == setting.split(':')[0]:
            AYD_DB_USER = setting.split(':')[1]
        elif 'AYD_DB_PASSWORD' == setting.split(':')[0]:
            AYD_DB_PASSWORD = setting.split(':')[1]

with open(os.path.join(AYD_APP_BASE_DIR, 'secretkey.txt')) as f:
    AYD_SECRET_KEY = f.read().strip()
