from django.utils.translation import ugettext_lazy as _
from south.db import db
from django.db import models
from dzenlog_text.models import *

class Migration:
    
    def forwards(self):
        
        
        # Mock Models
        GeneralPost = db.mock_model(model_name='GeneralPost', db_table='django_dzenlog_generalpost', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[])
        
        # Model 'TextPost'
        db.create_table('dzenlog_text_textpost', (
            ('generalpost_ptr', models.OneToOneField(GeneralPost)),
            ('annotation', models.CharField( _('Post\'s annotaion'), help_text = _('A short post\'s description.'), blank = True, max_length = 255)),
            ('body', models.TextField(_('Post\'s body'))),
            ('seo_keywords', models.CharField( _('SEO keywords'), help_text = _('Comma separated keywords list for search optimisation.'), blank = True, max_length = 255)),
        ))
        
        db.send_create_signal('dzenlog_text', ['TextPost'])
    
    def backwards(self):
        db.delete_table('dzenlog_text_textpost')
        
