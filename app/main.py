from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .routes import facebook_chat, user
from fastapi_log.log_request import LoggingRoute
from app.utils import Utils

# API Doc
app = FastAPI(
    title="Learning FastAPI",
    description="This is learning FastAPI Api project",
    version="1.0.0",
)

app.router.route_class = LoggingRoute


# Error
@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    # print(f"OMG! An HTTP error!: {repr(exc)}")
    print("this is >>>>>>>>", request.__dict__)
    # Add error logger here loguru
    # Utils.get_loguru_context().info(f"OMG! An HTTP error!: {repr(exc)}")
    Utils.log_error(f"{repr(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(
    facebook_chat.router,
    prefix="/facebook-chat-graph-api",
    tags=["Facebook Chat"],
)


app.include_router(
    user.router,
    prefix="/users",
    tags=["User Management"],
)

