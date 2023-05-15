# django imports
from django.shortcuts import render

# external imports
from rest_framework import serializers, viewsets

# local imports
from .models import Country, UserInfo


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"


class CountryView(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = ()
    authentication_classes = ()


class UserView(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
    authentication_classes = ()
    http_method_names = ["post", "get"]

    def download_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=export.csv'
        writer = csv.writer(response)
        field_names = ["id", "country", "org_name", "role", "name", "email", "phone"]
        writer.writerow(field_names)
        for obj in self.queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response
