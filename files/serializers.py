from rest_framework import serializers
from files.models import File

class FileListSerializer(serializers.Serializer) :
    name = serializers.CharField(max_length=50)
    one_file = serializers.ListField(
                       child=serializers.FileField( max_length=100000,
                                         allow_empty_file=False,
                                         use_url=False )
                                )
    
    def create(self, validated_data):
        name=validated_data.pop('name')
        one_file=validated_data.pop('one_file')
        for file in one_file:
            f = File.objects.create(name=name, one_file=file,**validated_data)
        return f

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File  
        fields = '__all__'