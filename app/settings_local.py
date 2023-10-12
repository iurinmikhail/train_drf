from dotenv import dotenv_values

config = dotenv_values(".env")




DATABASES = {
    'default': {
        'ENGINE': config.get("DB_ENGINE"),
        'NAME': config.get("DB_NAME"),
        'USER': config.get("DB_USER"),
        'PASSWORD': config.get("DB_PASSWORD"),
        'HOST': config.get("DB_HOST"),
        'PORT': config.get("DB_PORT"),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }