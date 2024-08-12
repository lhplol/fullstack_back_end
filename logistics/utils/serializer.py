# 文件位置 logistics/utils/serializer.py

from common.core.serializers import BaseModelSerializer
from logistics.models import FreightBill


class FreightBillSerializer(BaseModelSerializer):
    class Meta:
        model = FreightBill
        fields = [
            'pk', 'shipping_date', 'origin', 'destination', 'calculation_address', 'contact_person', 'plan_number',
            'package_count', 'total_weight', 'total_volume', 'payment_method', 'shipping_method', 'pricing_method',
            'car_type', 'is_carpool', 'unit_price', 'amount', 'other_fees', 'total_amount', 'remark', 
            'created_time', 'updated_time'
        ]
        table_fields = [
            'pk', 'shipping_date', 'origin', 'destination', 'contact_person', 'plan_number', 'package_count',
            'total_weight', 'total_volume', 'payment_method', 'shipping_method', 'unit_price', 'amount',
            'total_amount'
        ]
        read_only_fields = ['pk']
