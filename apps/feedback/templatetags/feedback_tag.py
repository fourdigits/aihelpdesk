from django import template

from apps.feedback.models import FeedbackFormPage

register = template.Library()


@register.simple_tag
def get_feedback_page():
    return FeedbackFormPage.objects.live().first()
