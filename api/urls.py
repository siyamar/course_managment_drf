from django.urls import path
from .views import RegisterView, LoginView, LogoutView, CourseListCreateView, CourseRetrieveDeleteView, PurchaseCreateView, MyPurchasesListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # auth
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', LoginView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout', LogoutView.as_view(), name='logout'),

    # courses
    path('courses/', CourseListCreateView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseRetrieveDeleteView.as_view(), name='course-detail'),

    # purchases
    path('purchases/', PurchaseCreateView.as_view(), name='buy-course'),
    path('purchases/me/', MyPurchasesListView.as_view(), name='my-purchases'),
]
