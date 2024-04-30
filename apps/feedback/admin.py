from django.utils.translation import gettext_lazy as _
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register

from apps.feedback.models import Feedback


class FeedbackAdmin(ModelAdmin):
    model = Feedback
    menu_label = _("Feedback")
    menu_icon = "comment"
    menu_order = 291
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("answer", "feedback", "user_email", "date_asked", "status")
    search_fields = ("user_email", "answer", "feedback", "status", "date_asked")


modeladmin_register(FeedbackAdmin)
