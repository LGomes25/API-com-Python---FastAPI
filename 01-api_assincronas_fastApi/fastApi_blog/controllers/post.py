from datetime import datetime, UTC
from typing import Annotated

from fastapi import Response, Cookie, status, Header, APIRouter
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")

fake_db = [
    {'title': f'Criando uma aplicação com Java', 'published_at': datetime.now(UTC), 'published': True, 'author': 'Zacahrias'},
    {'title': f'Criando uma aplicação com C#', 'published_at': datetime.now(UTC), 'published': False, 'author': 'Zacahrias'},
    {'title': f'Criando uma aplicação com Cobol', 'published_at': datetime.now(UTC), 'published': True, 'author': 'Zacahrias'},
    {'title': f'Criando uma aplicação com Delphi', 'published_at': datetime.now(UTC), 'published': True, 'author': 'Zacahrias'},
    {'title': f'Criando uma aplicação com FastApi', 'published_at': datetime.now(UTC), 'published': True, 'author': 'Zacahrias'}
]


# Body Parameters - envio de json no corpo da requisicao.
# para o exemplo, enviando apenas o title ja e suficiente pois os outros atributos sao incializados.
# mas nada impede de passar todos os atributos, respeitando suas caracteristicas e tipos
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    post_dict = post.model_dump()
    fake_db.append(post_dict)
    return post_dict


# Query parameters - limites devem vir pela url ex: ../posts?skip=0&limit=4&published=true
# como no exemplo já é inicializado, não são obrigatórios, mas em outros casos podem ser requeridos
# pelo mesmo motivo anterior, nao e necessario ambos queries estarem no path, pode existir apenas um
@router.get("/", response_model=list[PostOut])
def read_posts(published: bool, limit: int, skip: int =0 ):
    posts =[]
    for post in fake_db:
        if len(posts) == limit:
            break
        if post ['published'] is published:
            posts.append(post)
    return posts


@router.get("/more/", response_model=list[PostOut])
def read_posts(response: Response, published: bool, limit: int, skip: int =0, ads_id: Annotated[str | None, Cookie()] = None, user_agent: Annotated[str | None, Header()] = None):
    response.set_cookie(key='user', value='leo@mail.com')
    print(f'Cookie: {ads_id}')
    print(f'User_Agent: {user_agent}')
    tail = skip + limit
    return [post for post in fake_db[skip:tail] if post['published'] is published]


# Path parameters - precisa informar via url o parametro de framewrok
# aceita colocar o tipo, str, int para regular.
@router.get("/{framework}", response_model=list[PostOut])
def read_framework_posts(framework: str):
    return [
            {'title': f'Criando uma aplicação com {framework}', 'published_at': datetime.now(UTC), 'author': 'Graoiker'},
            {'title': f'Internacionalizando uma app {framework}', 'published_at': datetime.now(UTC), 'author': 'Graoiker'}
        ]
    