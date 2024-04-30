from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, HelpPanel, \
    TitleFieldPanel, InlinePanel


class Feedback(models.Model):
    UNDECIDED = 0
    APPROVED = 1
    ANSWERED = 2
    REJECTED = 3

    STATUS_CHOICES = (
        (UNDECIDED, _("Undecided")),
        (APPROVED, _("Approved")),
        (ANSWERED, _("Answered")),
        (REJECTED, _("Rejected")),
    )
    answer = models.ForeignKey(
        to="cms.Answer",
        on_delete=models.SET_NULL,
        null=True,
    )

    feedback = models.TextField(
        verbose_name=_("Have a question or comment? Leave it here!"),
        help_text=_("We will forward this response to the expert."),

    )

    grade = models.PositiveSmallIntegerField(
        verbose_name=_(
            "Do you find this article clearly explained and easy to follow?"
        ),
        help_text=_("(0 = not clear, 5 = very clear)"), blank=True
    )
    reliability_grade = models.PositiveSmallIntegerField(
        verbose_name=_("Do you find this AI-Helpdesk article reliable?"),
        help_text=_("(0 = not reliable, 5 = very reliable)"),
    )

    user_name = models.TextField(verbose_name=_("What is your name?"),
                                 blank=True)
    user_email = models.EmailField(
        verbose_name=_("Email"),
        help_text=_("We will forward the expert's response when we receive it."),
        blank=True,
    )
    user_age = models.PositiveSmallIntegerField(verbose_name=_("What is your age?"),
                                                null=True, blank=True)

    feedback_by_ip = models.GenericIPAddressField(null=True, blank=True)
    date_asked = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=UNDECIDED)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("answer", read_only=True),
            ],
            heading=_("Answer"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("status"),
                FieldPanel("feedback", read_only=True),
                FieldPanel("grade", read_only=True),
                FieldPanel("reliability_grade", read_only=True),
            ],
            heading=_("Feedback"),
        ),
        MultiFieldPanel(
            [

                FieldPanel("user_name", read_only=True),
                FieldPanel("user_email", read_only=True),
                FieldPanel("user_age", read_only=True),
                FieldPanel("feedback_by_ip", read_only=True),

            ],
            heading=_("User information"),
        ),
    ]
