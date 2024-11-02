from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()
router.register("levels", views.LevelViewSet)
router.register("courses", views.CourseViewSet)
router.register("faculties", views.FacultyViewSet)
router.register("semesters", views.SemesterViewSet)
router.register("departments", views.DepartmentViewSet)
router.register("academic-years", views.AcademicYearViewSet)
router.register("registration-periods", views.RegistrationPeriodViewSet)

faculty_router = NestedDefaultRouter(router, "faculties", lookup="faculty")
faculty_router.register("departments", views.DepartmentViewSet, "department")

academic_router = NestedDefaultRouter(router, "academic-years", lookup="academic_year")
academic_router.register("semesters", views.SemesterViewSet, "semester")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(faculty_router.urls)),
    path("", include(academic_router.urls)),
]
