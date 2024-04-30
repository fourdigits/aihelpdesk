from django import forms
from django.utils.translation import gettext_lazy as _

from apps.feedback.models.models import Feedback


class FeedbackForm(forms.ModelForm):
    feedback = forms.CharField(
        label=_("Have a question or comment? Leave it here!"),
        help_text=_("We will forward this response to the expert."),
        required=False,
    )

    grade = forms.IntegerField(
        label=_("Do you find this article clearly explained and easy to follow?*"),
        help_text=_("(0 = not clear, 5 = very clear)"),
        required=True,
    )
    reliability_grade = forms.IntegerField(
        label=_("Do you find this AI-Helpdesk article reliable?*"),
        help_text=_("(0 = not reliable, 5 = very reliable)"),
        required=True,
    )

    user_name = forms.CharField(
        label=_("What is your name?"),
        required=False,
    )
    user_email = forms.CharField(
        label=_("Email"),
        help_text=_("We will forward the expert's response when we receive it."),
        required=False,
    )
    user_age = forms.IntegerField(label=_("What is your age?"), required=False)

    class Meta:
        model = Feedback
        fields = [
            "feedback",
            "grade",
            "reliability_grade",
            "user_name",
            "user_email",
            "user_age",
        ]
