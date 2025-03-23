#pip install jinja2
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")