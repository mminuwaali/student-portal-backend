from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from academy.urls import router as academy_router
from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()
router.register('payments', views.PaymentViewSet, "payments")
router.register('next-of-kin', views.NextOfKinViewSet,'next-of-kin')
router.register('registration', views.StudentRegistrationViewSet,'registration')
router.register("registered-courses", views.RegisteredCourseViewSet,"registered-courses")
router.register("registered-semesters", views.RegisteredSemesterViewSet,"registered-semesters")

nested_academy_router = NestedDefaultRouter(academy_router, "academic-years", lookup="academic_year")
nested_academy_router.register("registered-semesters", views.RegisteredSemesterViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("", include(nested_academy_router.urls)),
]
