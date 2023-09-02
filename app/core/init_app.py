import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse



from secure import Server, StrictTransportSecurity, ReferrerPolicy, CacheControl, Secure

from app.core.exceptions import (
    on_value_error,
)

from app.settings.config import settings
from app.settings.log import DEFAULT_LOGGING

logger = logging.getLogger(__name__)

# Adding the Secure Headers
server = Server().set("Secure")
hsts = StrictTransportSecurity().include_subdomains().preload().max_age(2592000)
referrer = ReferrerPolicy().no_referrer()
cache_value = CacheControl().must_revalidate()

secure_headers = Secure(
    server=server,
    hsts=hsts,
    referrer=referrer,
    cache=cache_value
)

def configure_logging(log_settings: dict = None):
    log_settings = log_settings or DEFAULT_LOGGING
    logging.config.dictConfig(log_settings)

def init_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )
    app.add_middleware(
        GZipMiddleware
    )
    @app.middleware("http")
    async def set_secure_headers(request:Request, call_next):
        response = await call_next(request)
        secure_headers.framework.fastapi(response)
        return response

def register_exceptions(app: FastAPI):
    app.add_exception_handler(ValueError, on_value_error)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc:RequestValidationError):
        logger.debug("RequestValidationError occured")
        ed_ = exc.errors()[0]
        x = ed_["loc"]
        
        return PlainTextResponse(f"{ed_['msg']}", status_code=200)