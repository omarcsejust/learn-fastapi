from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .routes import facebook_chat, user

# API Doc
app = FastAPI(
    title="Learning FastAPI",
    description="This is learning FastAPI Api project",
    version="1.0.0",
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

