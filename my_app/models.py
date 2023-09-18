from time import timezone

from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.Users.id, filename)

class FileModel(models.Model):
    file_name = models.CharField(max_length=255) # 文件名称
    upload = models.FileField(upload_to=user_directory_path)
    # 文件类型
    file_type = models.CharField(max_length=100)
    # 文件大小
    file_size = models.DecimalField(max_digits=10, decimal_places=1)
    # 文件保存路径
    file_path = models.CharField(max_length=255)
    # 上传时间
    upload_time = models.DateTimeField(default=timezone.now)
    # 是否删除
    delete = models.BooleanField(default=False)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name
    class Meta:
        indexes = [models.Index(fields=['id'])]
