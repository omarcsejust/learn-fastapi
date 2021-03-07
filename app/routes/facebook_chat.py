from fastapi import APIRouter
import requests

router = APIRouter()

graph_api_uri = "https://graph.facebook.com/"
graph_api_version = "v9.0"


@router.get("/user-page-info/user-id/{user_fb_id}/user-access-token/{user_access_token}")
def get_user_fb_page_info(user_fb_id: str, user_access_token: str):
    fields = "fields=name,access_token"
    uri = graph_api_uri + graph_api_version + "/" + user_fb_id + "/accounts?" + fields + "&access_token=" + user_access_token
    data = requests.get(uri)
    return data.json()


@router.get("/page-access-token/page-id/{page_id}/user-access-token/{user_access_token}")
def get_page_access_token(page_id: str, user_access_token: str):
    fields = "fields=access_token"
    uri = graph_api_uri + graph_api_version + "/" + page_id + "?" + fields + "&access_token=" + user_access_token
    data = requests.get(uri)
    return data.json()




