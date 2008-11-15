from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_dzenlog.models import GeneralPost

class TextPost(GeneralPost):
    body_detail_template = 'dzenlog_text/post.html'
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

