# 文件位置 demo/utils/serializer.py

from common.core.serializers import BaseModelSerializer, LabeledChoiceField, BasePrimaryKeyRelatedField
from demo import models


class BookSerializer(BaseModelSerializer):
    class Meta:
        model = models.Book
        ## pk 字段用于前端删除，更新等标识，如果有删除更新等，必须得加上pk 字段
        fields = ['pk', 'name', 'isbn', 'category', 'is_active', 'author', 'publisher', 'publication_date', 'price',
                  'created_time', 'admin', 'cover', 'book_file', 'updated_time']
        ## 用于前端table字段展示
        table_fields = ['pk', 'cover', 'category', 'name', 'is_active', 'isbn', 'author', 'publisher',
                        'publication_date', 'price', 'book_file']
        read_only_fields = ['pk']
        # fields_unexport = ['pk']  # 导入导出文件时，忽略该字段

    category = LabeledChoiceField(choices=models.Book.CategoryChoices.choices,
                                  default=models.Book.CategoryChoices.DIRECTORY, label='书籍类型')
    admin = BasePrimaryKeyRelatedField(attrs=['pk', 'username'], label="管理员", queryset=models.UserInfo.objects,
                                       required=True, format="{username}({pk})")
    # covers = BasePrimaryKeyRelatedField(attrs=['pk', 'filename'],format="{filename}({pk})", label="书籍封面", queryset=models.UploadFile.objects,
    #                                    required=True,  many=True)