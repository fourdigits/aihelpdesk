# Generated by Django 4.2.11 on 2024-04-30 09:22

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.routable_page.models
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cms", "0003_alter_answertag_tag"),
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeedbackFormPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(verbose_name="Intro")),
                (
                    "thank_you_text",
                    wagtail.fields.RichTextField(
                        default="<p>Bedankt voor het stellen van je vraag. We nemen je vraag in behandeling en proberen zo snel mogelijk een expert te vinden die je vraag kan beantwoorden.</p>",
                        verbose_name="Tekst",
                    ),
                ),
            ],
            options={
                "verbose_name": "Feedback formulier pagina",
                "verbose_name_plural": "Feedback formulier pagina's",
            },
            bases=(
                wagtail.contrib.routable_page.models.RoutablePageMixin,
                "wagtailcore.page",
            ),
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "feedback",
                    models.TextField(
                        help_text="We will forward this response to the expert.",
                        verbose_name="Have a question or comment? Leave it here!",
                    ),
                ),
                (
                    "grade",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="(0 = not clear, 5 = very clear)",
                        null=True,
                        verbose_name="Do you find this article clearly explained and easy to follow?",
                    ),
                ),
                (
                    "reliability_grade",
                    models.PositiveSmallIntegerField(
                        help_text="(0 = not reliable, 5 = very reliable)",
                        verbose_name="Do you find this KlimaatHelpdesk article reliable?",
                    ),
                ),
                (
                    "user_name",
                    models.TextField(
                        blank=True, null=True, verbose_name="What is your name?"
                    ),
                ),
                (
                    "user_email",
                    models.EmailField(
                        blank=True,
                        help_text="We will forward the expert's response when we receive it.",
                        max_length=254,
                        null=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "user_age",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="What is your age?"
                    ),
                ),
                ("feedback_by_ip", models.GenericIPAddressField(blank=True, null=True)),
                ("date_asked", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "Undecided"),
                            (1, "Approved"),
                            (2, "Answered"),
                            (3, "Rejected"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "answer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="cms.answer",
                    ),
                ),
            ],
        ),
    ]