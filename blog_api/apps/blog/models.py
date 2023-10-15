from ckeditor.fields import RichTextField
from apps.common.models import models, BaseModel
from apps.user.models import User
from django.utils.text import get_valid_filename
import datetime


# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    sanitized_title = get_valid_filename(instance.title)
    return f'images/blogs/{sanitized_title}_{current_time}/{filename}'


class Blog(BaseModel):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    title_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    content = RichTextField()

    class Meta:
        db_table = "blog"
