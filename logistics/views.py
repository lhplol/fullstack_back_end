# 文件位置 logistics/views.py

import logging

from django_filters import rest_framework as filters

from common.core.filter import BaseFilterSet
from common.core.modelset import BaseModelSet, ImportExportDataAction
from logistics.models import FreightBill
from logistics.utils.serializer import FreightBillSerializer

logger = logging.getLogger(__name__)


class FreightBillFilter(BaseFilterSet):
    origin = filters.CharFilter(field_name='origin', lookup_expr='icontains')
    destination = filters.CharFilter(field_name='destination', lookup_expr='icontains')
    contact_person = filters.CharFilter(field_name='contact_person', lookup_expr='icontains')
    plan_number = filters.CharFilter(field_name='plan_number', lookup_expr='icontains')

    class Meta:
        model = FreightBill
        fields = ['origin', 'destination', 'contact_person', 'plan_number', 'payment_method', 'shipping_method', 'car_type',
                  'is_carpool', 'shipping_date', 'created_time']


class FreightBillView(BaseModelSet, ImportExportDataAction):
    """
    运费账单管理
    """
    queryset = FreightBill.objects.all()
    serializer_class = FreightBillSerializer
    ordering_fields = ['created_time']
    filterset_class = FreightBillFilter
    #取消删除接口的两种办法，一种是不列出、一种是重写destroy
    #http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']
    #def destroy(self, request, *args, **kwargs):
        #return ApiResponse(code=1001, detail=_("Delete operation not allowed"), status=405)