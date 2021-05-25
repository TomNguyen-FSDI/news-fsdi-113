
from django import template

from ..models import Article,Comment

register = template.Library()

@register.filter(name='total_stars')
def total_stars(pk):
    # all_article = Article.objects.all()
    # all_comment = Comment.objects.all()
    # print(f'all article {all_article}')
    # print(f'all comment {all_comment}')
    
    pk_article = Article.objects.filter(id=pk)
    article_title = pk_article[0]
    comments = Comment.objects.filter(article=article_title)
    total = 0
    for comment in comments:
        total += comment.star
    return total

@register.filter(name='sub')
def sub(value1, arg):
    return value1 - arg

@register.simple_tag
def average(total, length):
    if length == 0: # can not divide by zero
        return 0
    average = total / length
    average = '{:.2f}'.format(average)
    return average

@register.simple_tag
def update_variable(val):
    return val

@register.filter(name='total_num_stars')
def total_num_stars(pk, num_star):
    pk_article = Article.objects.filter(id=pk)
    article_title = pk_article[0]
    comments = Comment.objects.filter(article=article_title)
    star_num_total = 0
    for comment in comments:
        if num_star == comment.star:
            star_num_total += 1
    return star_num_total

@register.filter(name='total_stars_average')
def total_stars_average(pk):
    pk_article = Article.objects.filter(id=pk)
    article_title = pk_article[0]
    comments = Comment.objects.filter(article=article_title)
    total = total_stars(pk)
    if len(comments) != 0: # can not divide by zero
        total_stars_average = total / len(comments)
    else:
        total_stars_average = 0
    return round(total_stars_average,2)

@register.filter(name='total_bar_average')
def total_bar_average(pk, total_star):
    pk_article = Article.objects.filter(id=pk)
    article_title = pk_article[0]
    comments = Comment.objects.filter(article=article_title)
    if len(comments) == 0:  # can not divide by zero
        return 0
    total_stars_average = total_star / len(comments)
    answer_percentage = total_stars_average * 100
    round_answer = round(answer_percentage, 2)
    return round_answer

@register.filter(name='find_user_id')
def find_user_id(user):
    print(user)
    articles = Article.objects.all()
    for article in articles:
        if article.author == user:
            return article.author_id
    return 0

@register.filter(name='get_image_url')
def get_image_url(full_url):
    all_url = full_url.split('/')
    return all_url[len(all_url)-1]


register.filter('sub', sub)
register.filter('total_stars', total_stars)
register.filter('total_num_stars', total_num_stars)
register.filter('total_stars_average', total_stars_average)
register.filter('total_bar_average', total_bar_average)
register.filter('find_user_id', find_user_id)
register.filter('get_image_url', get_image_url)
