from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_dzenlog.models import GeneralPost

class TextPost(GeneralPost):
    body_detail_template = 'dzenlog_text/post.html'
    feed_description_template = 'dzenlog_text/text_feed_detail.html'

    body = models.TextField(_('Post\'s body'))

