from ckeditor.fields import RichTextField
from apps.common.models import models, BaseModel
from apps.user.models import User


# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Blog(BaseModel):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=2000)
    title_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    content = RichTextField()

    class Meta:
        db_table = "blog"
