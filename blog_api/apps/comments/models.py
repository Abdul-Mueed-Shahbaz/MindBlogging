from django.contrib.auth import get_user_model
from apps.blog.models import Blog
from apps.common.models import models, BaseModel
from django.utils.text import get_valid_filename


def upload_to(instance, filename):
    sanitized_title = get_valid_filename(instance.blog.title)
    return f'images/comments/{sanitized_title}_{instance.user.id}/{filename}'


class Comments(BaseModel):
    content = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='user', on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"
