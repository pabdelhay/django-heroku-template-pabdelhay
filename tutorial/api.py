from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from tutorial.models import SampleModel


class SampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel
        fields = ('property_a', 'property_b')


class SampleModelViewset(ReadOnlyModelViewSet):
    model = SampleModel
    serializer_class = SampleModelSerializer
    queryset = SampleModel.objects.all()

    @action(detail=False)
    def custom_method(self, request, pk=None):
        response_data = {
            'msg': "This is just a sample response for a custom method of api"
        }
        return Response(response_data)
