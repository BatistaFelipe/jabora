import logging
from dotenv import load_dotenv
import os

load_dotenv()

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_env(env_name):
    value = os.environ.get(env_name)
    if not value:
        raise KeyError(f"Environment variable '{env_name}' is not set.")
    return value
