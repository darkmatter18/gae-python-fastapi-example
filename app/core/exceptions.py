import logging
from fastapi import Response
from fastapi.requests import Request
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)

class SettingNotFound(Exception):
    """This is settings not found exception
    This will fire, if there is no settings file available
    """
    pass

async def on_value_error(
    request: Request,
    exception: ValueError
) -> JSONResponse:
    str(exception)
    return Response(content=str(exception), status_code=200)
