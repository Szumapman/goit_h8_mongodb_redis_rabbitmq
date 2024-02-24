import sys

from mongoengine import connect
from pymongo.errors import ConfigurationError
import configparser

config = configparser.ConfigParser()
config.read("config_dev.ini")

mongo_user = config.get("DB", "user")
mongodb_pass = config.get("DB", "pass")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")

try:
    # connect to cluster on AtlasDB with connection string
    connect(
        host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""",
        ssl=True,
    )
except ConfigurationError as e:
    print("Problem with database connection, check your connection and credentials settings.")
    print(f"Error: {e}")
    sys.exit(1)
