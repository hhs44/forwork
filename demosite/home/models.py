from django.db import models
from wagtail.core import rich_text

from wagtail.core.models import Page
from wagtail.core.fields import *
from wagtail.admin.edit_handlers import *

class HomePage(Page):
    body = RichTextField()
    
    # 使得该字段可以在
    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full')
    ]
