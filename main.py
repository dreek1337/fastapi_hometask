from fastapi import FastAPI, Response

app = FastAPI()


@app.get('/root')
def page_root():
    return Response(content='Hello World!')


@app.get('/hello/')
def page_root():
    pass
