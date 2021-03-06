from django import template
from home.models import Footer
from home.views import render_live_articles
import datetime
import json

register = template.Library()

@register.simple_tag(takes_context=True)
def dump_context(context: template.RequestContext):
    return context.request

@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer(context):
    return {
        'footer': Footer.objects.first(),
        'request': context['request'],
    }


@register.inclusion_tag('home/tags/articles_list.html')
def render_articles_list(articles):
    return {'articles': render_live_articles(articles)}
