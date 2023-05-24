from django.urls import path

from infra.api import (
    BaseView,
    CompanyListView,
    DepartmentListView,
    EmployeeListView,
)

urlpatterns = [
    path(
        route="api/v1/<str:model>/create",
        view=BaseView.as_view({'post': 'create'}),
        name="create",
    ),
    path(
        route="api/v1/<str:model>/detail/<uuid:object_id>",
        view=BaseView.as_view({'get': 'retrieve'}),
        name="detail",
    ),
    path(
        route="api/v1/<str:model>/update/<uuid:object_id>",
        view=BaseView.as_view({'put': 'update'}),
        name="update",
    ),
    path(
        route="api/v1/company/list",
        view=CompanyListView.as_view(),
        name="list_companies",
    ),
    path(
        route="api/v1/department/list",
        view=DepartmentListView.as_view(),
        name="list_departments",
    ),
    path(
        route="api/v1/employee/list",
        view=EmployeeListView.as_view(),
        name="list_employees",
    ),
]
