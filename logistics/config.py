# 文件位置 logistics/config.py
from django.urls import path, include

# 路由配置，当添加APP完成时候，会自动注入路由到总服务
URLPATTERNS = [
    path('api/logistics/', include('logistics.urls')),
]

# 请求白名单，支持正则表达式，可参考settings.py里面的 PERMISSION_WHITE_URL
PERMISSION_WHITE_REURL = [
    "^/api/logistics/.*choices$",
    "^/api/logistics/.*search-fields$",
]