# 文件位置 logistics/models.py

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from common.core.models import DbAuditModel

class FreightBill(DbAuditModel):
    class PaymentMethodChoices(models.TextChoices):
        ADVANCE = '垫付', _("垫付")
        CASH = '现付', _("现付")
        CREDIT = '月结', _("月结")
        OTHER = '其他', _("其他")

    class ShippingMethodChoices(models.TextChoices):
        LTL = '零担', _("零担")
        FTL = '整车', _("整车")

    class PricingMethodChoices(models.TextChoices):
        UNIT = '件', _("件")
        WEIGHT = '重量', _("重量")
        VOLUME = '体积', _("体积")

    class CarTypeChoices(models.TextChoices):
        FOUR_TWO_METERS = '4.2米车', _("4.2米车")
        SIX_EIGHT_METERS = '6.8米车', _("6.8米车")
        OTHER = '其他', _("其他")

    shipping_date = models.DateTimeField(verbose_name="发货日期", default=timezone.now)
    origin = models.CharField(verbose_name="发货地", max_length=100)
    destination = models.CharField(verbose_name="目的地", max_length=100)
    calculation_address = models.CharField(verbose_name="计算地址", max_length=255)
    contact_person = models.CharField(verbose_name="联系人", max_length=50)
    plan_number = models.CharField(verbose_name="计划单号", max_length=50)
    package_count = models.IntegerField(verbose_name="件数")
    total_weight = models.FloatField(verbose_name="总重量（KG）")
    total_volume = models.FloatField(verbose_name="总方数(m³）")
    payment_method = models.CharField(verbose_name="运费支付方式", max_length=10, choices=PaymentMethodChoices.choices)
    shipping_method = models.CharField(verbose_name="发货方式", max_length=10, choices=ShippingMethodChoices.choices)
    pricing_method = models.CharField(verbose_name="零担计价方式", max_length=10, choices=PricingMethodChoices.choices)
    car_type = models.CharField(verbose_name="专车车型", max_length=10, choices=CarTypeChoices.choices)
    is_carpool = models.BooleanField(verbose_name="是否拼车", default=False)
    unit_price = models.FloatField(verbose_name="单价(元)")
    amount = models.FloatField(verbose_name="金额(元)")
    other_fees = models.FloatField(verbose_name="其他费用")
    total_amount = models.FloatField(verbose_name="总金额")
    remark = models.TextField(verbose_name="备注", null=True, blank=True)

    class Meta:
        verbose_name = '运费账单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.plan_number} - {self.contact_person}"
