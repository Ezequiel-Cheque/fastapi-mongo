from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
    title="REST APi with FastApi and MongoDB",
    description="This is a simple REST API using FastApi and MongoDb",
    version="0.0.1",
    openapi_tags=tags_metadata
)

app.include_router(user)
