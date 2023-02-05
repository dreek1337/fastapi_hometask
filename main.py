from enum import Enum
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse


class MembersName(str, Enum):
    danila = 'Danila'


app = FastAPI()


@app.get('/')
def page_root() -> Response:
    """
    Endpoint главной страницы
    """
    return RedirectResponse(url='/docs')


@app.get('/hello/{name}')
def hello_name(name: MembersName | str) -> Response:
    """
    Endpoint приветствия по имени из параметров url
    """
    if name == MembersName.danila:
        return Response(content=f'Hello {name}! You are boss!')

    return Response(content=f'Hello {name}!')
