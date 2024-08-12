# 文件位置 demo/models.py

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from common.core.models import DbAuditModel, upload_directory_path
from system.models import UserInfo


class Book(DbAuditModel):
    class CategoryChoices(models.IntegerChoices):
        DIRECTORY = 0, _("小说")
        MENU = 1, _("文学")
        PERMISSION = 2, _("哲学")

    # covers = models.ManyToManyField(to=UploadFile,verbose_name="封面")
    admin = models.ForeignKey(to=UserInfo, verbose_name="管理员", on_delete=models.CASCADE)
    # avatar = ProcessedImageField(verbose_name="用户头像", null=True, blank=True,
    #                              upload_to=upload_directory_path,
    #                              processors=[ResizeToFill(512, 512)],  # 默认存储像素大小
    #                              scales=[1, 2, 3, 4],  # 缩略图可缩小倍数，
    #                              format='png')
    cover = models.ImageField(verbose_name="书籍封面", null=True, blank=True)
    book_file = models.FileField(verbose_name="书籍存储", upload_to=upload_directory_path, null=True, blank=True)
    name = models.CharField(verbose_name="书籍名称", max_length=100, help_text="书籍名称啊，随便填")
    isbn = models.CharField(verbose_name="标准书号", max_length=20)
    author = models.CharField(verbose_name="书籍作者", max_length=20, help_text="坐着大啊啊士大夫")
    publisher = models.CharField(verbose_name="出版社", max_length=20, default='大宇出版社')
    publication_date = models.DateTimeField(verbose_name="出版日期", default=timezone.now)
    price = models.FloatField(verbose_name="书籍售价", default=999.99)
    is_active = models.BooleanField(verbose_name="是否启用", default=False)
    category = models.SmallIntegerField(choices=CategoryChoices, default=CategoryChoices.DIRECTORY,
                                        verbose_name="书籍类型")

    class Meta:
        verbose_name = '书籍名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"