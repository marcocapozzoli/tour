
from uuid import UUID
from django.http import HttpResponseNotFound
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.viewsets import ViewSet

from rest_framework.generics import ListAPIView

from rest_framework.permissions import IsAdminUser
from app.serializers import CompanySerializer


from pydantic import ValidationError
from dataclasses import asdict
from django_filters.rest_framework import DjangoFilterBackend

from infra.factory import ControllerFactory, controller_factory
from infra.register.models import Company, Department


class BaseView(ViewSet):

    permission_classes = (IsAdminUser, )

    def dispatch(self, request, *args, **kwargs):
        
        if kwargs.get('model') not in ['company', 'department', 'employee']:
            return HttpResponseNotFound('Endpoint não encontrado.')
        
        self.controller = controller_factory(ControllerFactory(request.path))
        
        return super().dispatch(request, *args, **kwargs)
        
    def create(self, request: Request, **kwargs) -> Response:
        try:
            object = self.controller.create_object(
                params=request.data
            )
            return Response(
                status=201,
                data={
                    'success': True,
                    'error': None,
                    'data': asdict(object)
                }
            )
        except ValidationError as error:
            return Response(
                status=422,
                data={
                    'success': False,
                    'error': error.errors(),
                    'data': None,
                },
            )
        except Exception as error:
            return Response(
                status=400,
                data={
                    'success': False,
                    'error': error.to_dict(),
                    'data': None,
                },
            )

    def retrieve(self, request: Request, object_id: UUID, **kwargs) -> Response:
        try:
            object = self.controller.detail_object(object_id)
            return Response(
                status=200,
                data={
                    'success': True,
                    'error': None,
                    'data': asdict(object)
                }
            )
        except ValidationError as error:
            return Response(
                status=422,
                data={
                    'success': False,
                    'error': error.errors(),
                    'data': None,
                },
            )
        except Exception as error:
            return Response(
                status=400,
                data={
                    'success': False,
                    'error': error.to_dict(),
                    'data': None,
                },
            )

    def update(self, request: Request, object_id: UUID, **kwargs) -> Response:
        try:
            request.data.update({"id": str(object_id)})
            object = self.controller.update_object(params=request.data)
            return Response(
                status=200,
                data={
                    'success': True,
                    'error': None,
                    'data': asdict(object)
                }
            )
        except ValidationError as error:
            return Response(
                status=422,
                data={
                    'success': False,
                    'error': error.errors(),
                    'data': None,
                },
            )
        except Exception as error:
            return Response(
                status=400,
                data={
                    'success': False,
                    'error': error.to_dict(),
                    'data': None,
                },
            )


class CompanyListView(ListAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


# class DepartmentListView(ListAPIView):
#     permission_classes = (IsAdminUser, )
#     queryset = Department.objects.all()
#     serializer_class = CompanySerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['name']


# class EmployeeListView(ListAPIView):
#     permission_classes = (IsAdminUser, )
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['country']
