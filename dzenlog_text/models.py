from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_dzenlog.models import GeneralPost
from django_autolinks.utils import process_links

class TextPost(GeneralPost):
    list_template             = 'dzenlog_text/list.html'
    detail_template           = 'dzenlog_text/detail.html'
    body_detail_template      = 'dzenlog_text/body_detail.html'
    body_list_template        = 'dzenlog_text/body_list.html'
    feed_description_template = 'dzenlog_text/text_feed_detail.html'

    annotation = models.CharField(
                    _('Post\'s annotaion'),
                    help_text = _('A short post\'s description.'),
                    blank = True,
                    max_length = 255)
    body = models.TextField(_('Post\'s body'))
    seo_keywords = models.CharField(
                    _('SEO keywords'),
                    help_text = _('Comma separated keywords list for search optimisation.'),
                    blank = True,
                    max_length = 255)

    def save(self):
        self.body = process_links(self.body)
        super(TextPost, self).save()

    class Meta:
        verbose_name = _('textual post')
        verbose_name_plural = _('textual posts')
