import logging
from fastapi import FastAPI
from app.core.init_app import configure_logging, init_middlewares, register_exceptions
from app.settings.config import settings

configure_logging()

tags_metadata = [
    {
        "name": "Liveliness",
        "description": "**Liveliness probe**. Used by deployment manager to check the service availablity.",
    }
]

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.VERSION,
    debug=settings.DEBUG,
    root_path=settings.ROOT_PATH,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    openapi_tags=tags_metadata,
    contact=settings.CONTACT
)

logger = logging.getLogger(__name__)

init_middlewares(app)
register_exceptions(app)

@app.get('/', tags=['home'])
def home():
    return "Hello World. This is the Google App engine project"

@app.get('/healthz', tags=['Liveliness'])
def health():
    return "OK"

@app.get('/say/{name}', tags=['I say Name'])
def say_name(name: str):
    return f"You entered {name}"
