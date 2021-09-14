from django.db import models
from wagtail.core import rich_text

from wagtail.core.models import Page
from wagtail.core.fields import *
from wagtail.admin.edit_handlers import *

class HomePage(Page):
    rich_text = RichTextField(bank=True)
    stream_text = StreamField(bank=True)
    
    # 使得该字段可以在
    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full')
    ]
