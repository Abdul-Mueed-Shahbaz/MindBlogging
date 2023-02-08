from apps.blog.models import Blog
from apps.common.models import *


class Post(BaseModel):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True, default='')
    blog = models.ForeignKey(Blog, related_name='Blog', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']
