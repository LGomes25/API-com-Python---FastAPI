from datetime import datetime, UTC
from typing import Annotated


from fastapi import Response, Cookie, status, Header, APIRouter, Depends



from fastApi_blog.schemas.post import PostIn
from fastApi_blog.views.post import PostOut
from fastApi_blog.models.post_model import Post
from fastApi_blog.database import SessionLocal
from sqlalchemy.orm import Session
from fastApi_blog.security import verify_jwt_token

router = APIRouter(prefix="/posts")



# Body Parameters - envio de json no corpo da requisicao.
# para o exemplo, enviando apenas o title ja e suficiente pois os outros atributos sao incializados.
# mas nada impede de passar todos os atributos, respeitando suas caracteristicas e tipos

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn, user=Depends(verify_jwt_token)):
    db: Session = SessionLocal()
    db_post = Post(
        title=post.title,
        published_at=post.published_at,
        published=post.published,
        author=post.author
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db.close()
    return db_post


# Query parameters - limites devem vir pela url ex: ../posts?skip=0&limit=4&published=true
# como no exemplo já é inicializado, não são obrigatórios, mas em outros casos podem ser requeridos
# pelo mesmo motivo anterior, nao e necessario ambos queries estarem no path, pode existir apenas um

@router.get("/", response_model=list[PostOut])
def read_posts(published: bool, limit: int, skip: int = 0, user=Depends(verify_jwt_token)):
    db: Session = SessionLocal()
    query = db.query(Post).filter(Post.published == published).offset(skip).limit(limit)
    posts = query.all()
    db.close()
    return posts



@router.get("/more/", response_model=list[PostOut])
def read_posts_more(response: Response, published: bool, limit: int, skip: int = 0, ads_id: Annotated[str | None, Cookie()] = None, user_agent: Annotated[str | None, Header()] = None, user=Depends(verify_jwt_token)):
    response.set_cookie(key='user', value='leo@mail.com')
    db: Session = SessionLocal()
    query = db.query(Post).filter(Post.published == published).offset(skip).limit(limit)
    posts = query.all()
    db.close()
    return posts


# Path parameters - precisa informar via url o parametro de framewrok
# aceita colocar o tipo, str, int para regular.

@router.get("/{framework}", response_model=list[PostOut])
def read_framework_posts(framework: str, user=Depends(verify_jwt_token)):
    db: Session = SessionLocal()
    posts = db.query(Post).filter(Post.title.ilike(f"%{framework}%")).all()
    db.close()
    return posts
    