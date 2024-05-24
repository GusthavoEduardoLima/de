from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/orders/', include('orders.urls')),  # Placeholder
    path('api/items/', include('items.urls')),    # Placeholder
]
