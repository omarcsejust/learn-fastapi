from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi.responses import FileResponse
from ..dependency.db_dependency import get_db
from ..services.user import UserService
from ..schemas import User as UserSchema

from ..utils import Utils

router = InferringRouter()


@cbv(router)
class User:
    db: Session = Depends(get_db)

    @router.post("/")
    def add_user(self, user: UserSchema):
        service = UserService(db=self.db)
        import requests
        import tempfile
        r = requests.get("https://picsum.photos/id/237/200/300")
        with tempfile.NamedTemporaryFile(mode="w+b", suffix=".png", delete=False) as FOUT:
            FOUT.write(r.content)
            # return {
            #     "name": user.name,
            #     "image": FileResponse(FOUT.name, media_type="image/png")
            # }
        print(type(r.content))
        return service.add_user(user_schema=user, image=None)

    @router.get("/all")
    def get_all(self):
        from loguru import logger
        service = UserService(db=self.db)
        names = []
        users = service.get_all_users()
        import io
        for user in users:
            if user.image is None:
                continue
            with open(user.image, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            names.append({
                "name": user.name,
            })
        Utils.get_loguru_context().info("this is test log")
        return names

    @router.get("/test/exception")
    def test_exception(self):
        raise HTTPException(
            status_code=406,
            detail="406 log response"
        )


