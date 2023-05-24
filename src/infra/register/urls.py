from django.urls import path
from infra.api import BaseView, CompanyListView


urlpatterns = [
    path(
        route="api/v1/<str:model>/create",
        view=BaseView.as_view({'post': 'create'}),
        name="create"
    ),
    path(
        route="api/v1/<str:model>/detail/<uuid:object_id>",
        view=BaseView.as_view({'get': 'retrieve'}),
        name="detail"
    ),
    path(
        route="api/v1/<str:model>/update/<uuid:object_id>",
        view=BaseView.as_view({'put': 'update'}),
        name="update"
    ),
    # path(
    #     route="api/v1/company/list",
    #     view=CompanyListView.as_view(),
    #     name="list_companies"
    # )
]

# url_department = [
#     path(
#         route="api/v1/department/create",
#         view=BaseView.as_view(),
#         name="create"
#     ),
#     path(
#         route="api/v1/department/detail/<uuid:company_id>",
#         view=BaseView.as_view(),
#         name="detail"
#     ),
#     path(
#         route="api/v1/department/update/<uuid:company_id>",
#         view=BaseView.as_view(),
#         name="update"
#     ),
#     path(
#         route="api/v1/department/list",
#         view=BaseView.as_view(),
#         name="list_department"
#     )
# ]

# url_employee = [
#     path(
#         route="api/v1/employee/create",
#         view=BaseView.as_view(),
#         name="create_employee"
#     ),
#     path(
#         route="api/v1/employee/detail/<uuid:company_id>",
#         view=BaseView.as_view(),
#         name="detail_employee"
#     ),
#     path(
#         route="api/v1/employee/update/<uuid:company_id>",
#         view=BaseView.as_view(),
#         name="update_employee"
#     ),
#     path(
#         route="api/v1/employee/list",
#         view=BaseView.as_view(),
#         name="list_employee"
#     )
# ]


# urlpatterns = url_company #+ url_department + url_employee
