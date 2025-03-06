from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI() # Instance of the fastapi app created 


class Post(BaseModel):
    title: str
    content:str

@app.get('/') #app decorator used for routing
def root():
    return {"msg":"hello world"}

@app.post('/createpost')
def create_post(new_post: Post):
    # print(payload)
    # return {"new_post":f"title : {payload['title']},contents of the post is {payload['content']}"}
    # print(new_post['title'])
    return {"data":new_post}