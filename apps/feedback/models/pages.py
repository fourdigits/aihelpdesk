from django.apps import apps
from django.http import HttpResponseRedirect
from django.shortcuts import render
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, path, re_path, route
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail_helpdesk.cms.models import Answer

from apps.feedback.forms import FeedbackForm


class FeedbackFormPage(RoutablePageMixin, Page):
    intro = RichTextField(
        verbose_name="Intro",
    )
    thank_you_text = RichTextField(
        verbose_name="Tekst",
        default="<p>Bedankt voor het stellen van je vraag. "
        "We nemen je vraag in behandeling en proberen zo snel mogelijk een "
        "expert te vinden die je vraag kan beantwoorden.</p>",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("intro"),
                FieldPanel("thank_you_text"),
            ],
            heading="Formulier tekst",
        ),
    ]

    @path("<int:answer_id>/")
    def form(self, request, answer_id):
        """
        Index page, the form is spread over two steps using JavaScript.
        """
        if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.answer_id = answer_id
                obj.asked_by_ip = request.META.get("REMOTE_ADDR", "")
                obj.save()
                return HttpResponseRedirect(
                    self.url + self.reverse_subpage("thank-you")
                )
        else:
            form = FeedbackForm()

        template = "feedback/feedback_form_page.html"
        context = self.get_context(request)
        context.update({"answer": Answer.objects.get(id=answer_id)})
        context.update({"form": form})
        return render(request, template, context)

    @re_path(r"^dank/", name="thank-you")
    def thank_you(self, request):
        template = "wagtail_helpdesk/cms/ask_question_page_thank_you.html"
        context = self.get_context(request)
        return render(request, template, context)

    class Meta:
        verbose_name = "Feedback formulier pagina"
        verbose_name_plural = "Feedback formulier pagina's"
