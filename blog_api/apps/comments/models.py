from apps.common.models import *
from apps.posts.models import Post


class Comments(BaseModel):
    content = models.TextField(blank=True, default='')
    post = models.ForeignKey(Post, related_name='Post', on_delete=models.CASCADE)
