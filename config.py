# config.py — hardcoded secrets (bad practice)
DATABASE_URL = "postgresql://admin:password123@localhost/mydb"
SECRET_KEY   = "supersecretkey_do_not_share"
API_KEY      = "sk-1234567890abcdef"

def get_db():
    return DATABASE_URL
