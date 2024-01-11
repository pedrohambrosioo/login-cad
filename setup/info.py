from pathlib import Path, os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USE_TLS = True
EMAIL_HOST = 'smpt.gmail.com'
EMAIL_HOST_USER = 'pedro.ambro@hotmail.com'
EMAIL_HOST_PASSWORD = str(os.getenv('EMAIL_HOST_PASSWORD')) 
EMAIL_PORT = 587 