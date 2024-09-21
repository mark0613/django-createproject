def get_databases_config(db_type: str) -> dict:
    if db_type == 'sqlite':
        return {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': "BASE_DIR / 'db.sqlite3'",
        }
    elif db_type == 'mysql':
        return {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': "os.getenv('DB_HOST')",
            'PORT': "os.getenv('DB_PORT')",
            'USER': "os.getenv('DB_USER')",
            'PASSWORD': "os.getenv('DB_PASSWORD')",
            'NAME': "os.getenv('DB_NAME')",
        }
    elif db_type == 'postgres':
        return {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': "os.getenv('DB_HOST')",
            'PORT': "os.getenv('DB_PORT')",
            'USER': "os.getenv('DB_USER')",
            'PASSWORD': "os.getenv('DB_PASSWORD')",
            'NAME': "os.getenv('DB_NAME')",
        }
    else:
        raise ValueError(f'Invalid database type "{db_type}"')
