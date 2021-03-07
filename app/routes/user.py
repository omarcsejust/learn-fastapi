from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from ..dependency.db_dependency import get_db
from ..services.user import UserService
from ..schemas import User as UserSchema

router = InferringRouter()


@cbv(router)
class User:
    db: Session = Depends(get_db)

    @router.post("/")
    def add_user(self, user: UserSchema):
        service = UserService(db=self.db)
        import requests
        from fastapi.responses import FileResponse
        import tempfile
        r = requests.get("https://picsum.photos/id/237/200/300")
        with tempfile.NamedTemporaryFile(mode="w+b", suffix=".png", delete=False) as FOUT:
            FOUT.write(r.content)
            return {
                "name": user.name,
                "image": FileResponse(FOUT.name, media_type="image/png")
            }
        print(r.content)
        return service.add_user(user_schema=user, image=r.content)


