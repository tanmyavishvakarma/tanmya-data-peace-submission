from django.db.models import Q

from rest_framework import generics, filters
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = super().get_queryset()

        page = self.request.query_params.get('page')
        limit = self.request.query_params.get('limit', 5)
        name = self.request.query_params.get('name')
        sort = self.request.query_params.get('sort', 'id')

        if name:
            queryset = queryset.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
            )


        if sort.startswith('-'):
            sort_field = sort.lstrip('-')
            queryset = queryset.order_by(f'-{sort_field}')
        else:
            queryset = queryset.order_by(sort)

        if page:
            offset = (int(page) - 1) * int(limit)
            queryset = queryset[offset:offset + int(limit)]

        return queryset

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
