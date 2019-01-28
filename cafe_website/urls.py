from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from cafe.views import cafe_view
from cafe_website import settings
from orders.views import order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('cart/', include('cart.urls')),
    path('ordered/', order, name='order'),
    path('menu/', include(('menus.urls', 'menus'), namespace='menus')),
    path('places/', cafe_view, name='cafe_view'),
    path('delivery/', TemplateView.as_view(template_name='delivery.html')),
    path('blog/', include('blog.urls')),
    path('contacts/', TemplateView.as_view(template_name='contacts.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
