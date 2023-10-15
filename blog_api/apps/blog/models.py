from ckeditor.fields import RichTextField
from django.db.models import UniqueConstraint, CASCADE, CharField, ForeignKey, ImageField, GenericIPAddressField, \
    BigIntegerField

from apps.common.models import BaseModel
from apps.user.models import User
from django.utils.text import get_valid_filename
import datetime


# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    sanitized_title = get_valid_filename(instance.title)
    return f'images/blogs/{sanitized_title}_{current_time}/{filename}'


class Blog(BaseModel):
    title = CharField(max_length=250)
    author = ForeignKey(User, related_name='Blog', on_delete=CASCADE, null=False, blank=False)
    description = CharField(max_length=2000, blank=True)
    title_image = ImageField(upload_to=upload_to, blank=True, null=True)
    content = RichTextField()
    views = BigIntegerField(default=0)

    class Meta:
        db_table = "blog"


class BlogIP(BaseModel):
    ip_address = GenericIPAddressField(null=False, blank=False)
    blog = ForeignKey(Blog, related_name='Blog', on_delete=CASCADE, null=False, blank=False)
    user = ForeignKey(User, related_name='Blog_Ip', on_delete=CASCADE, null=True, blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['ip_address', 'blog'], name='unique_view')
        ]
        db_table = "blog_ip"
        verbose_name = 'Blog View'
