from pydoc import describe
from turtle import title
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title='My Blog'
    link=reverse_lazy('blog:post_list')
    description='New posts of my blog'
    
    def items(self):
        return Post.published.all()[:5]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return truncatewords(item.body, 30)# You use the truncatewords built-in template filter to build the description of the blog post with the first 30 words.
    