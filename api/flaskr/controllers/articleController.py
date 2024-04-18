from flask import Blueprint, request
from flaskr.services import articleService
import json
from flaskr.models.articleModel import ArticleModel

article_route = Blueprint('product_route', __name__,url_prefix="/test")

@article_route.route("",methods=['POST'])
def get_article():
    data=request.get_json()
    url=data.get('url')
    return articleService.get_article(url)

@article_route.route("/originalArticle",methods=['POST'])
def get_original_article():
    article = ArticleModel(request.get_json().get('url'),None)
    print(article)
    return articleService.get_original_article(article)










     