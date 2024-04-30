from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail_helpdesk.cms.models import Answer, AnswerIndexPage

Answer.parent_page_types = []
AnswerIndexPage.subpage_types = ["citation.AIAnswer"]


class AIAnswer(Answer):
    parent_page_types = ["cms.AnswerIndexPage"]
    citation = models.CharField(
        max_length=255, blank=True, null=True, help_text="Please follow the APA format."
    )

    content_panels = Answer.content_panels + [FieldPanel("citation")]

    class Meta:
        verbose_name = "AI-answer"
        verbose_name_plural = "AI-answer"
