from apps.blog.models import Blog
from apps.common.models import models, BaseModel
from apps.user.models import User


class Comments(BaseModel):
    content = models.TextField(blank=True, default='')
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"
