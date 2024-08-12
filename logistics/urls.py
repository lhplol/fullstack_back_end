from rest_framework.routers import SimpleRouter

from logistics.views import FreightBillView

router = SimpleRouter(False)  # 设置为 False ,为了去掉url后面的斜线

router.register('freightbill', FreightBillView, basename='freightbill')

urlpatterns = [
]

urlpatterns += router.urls
