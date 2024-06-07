from rest_framework import serializers
from .models import Color, Person

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if len(data.get('password')) < 8:
            # return serializers.ValidationError("Password must be atleast 8 characters long.") # Throws an error
            return {"message": "Password must be atleast 8 characters long."}
        return data

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True) # for nested serializer data.
    color_info = serializers.SerializerMethodField() # to show extra data from different tables
    class Meta:
        model = Person
        fields = '__all__'               # for all the fields.
        # exclude = ['name']             # to exclude only these fields.
        # fields = ['name', 'age']       # to include only these fields.
        # depth = 1      
    
    def get_color_info(self, obj):
        color_obj = Color.objects.get(id=obj.color.id)
        return {"color_name":color_obj.name, "Hex code" : color_obj.name + "#000000"}         # for nested serializer. Showing all the data of nested models

    def validate_name(self, value):
        if value == "admin":
            raise serializers.ValidationError("Name cannot be admin")
        return value

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age cannot be less than 18")
        return value