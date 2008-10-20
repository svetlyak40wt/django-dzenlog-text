from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_dzenlog.models import GeneralPost

class TextPost(GeneralPost):
    body = models.TextField(_('Post\'s body'))

    def _get_template(self):
        return 'dzenlog_text/post.html'
