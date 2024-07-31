from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.store, name="store"),
                  path('cart/', views.cart, name="cart"),
                  path('checkout/', views.checkout, name="checkout"),
                  path('update_item/', views.updateItem, name="update_item"),
                  path('process_order/', views.processOrder, name="process_order"),
                  path('product/<int:id>/', views.product_detail, name='product_detail'),
                  path('signup/', views.signup, name='signup'),
                  path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='store/logout.html'), name='logout'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
