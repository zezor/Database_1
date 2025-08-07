from rest_framework.utils.representation import serializer_repr
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ("email","password")


# Create a custom representation for the serializer( Generic, Mixins, ViewSets)
# for serializing HTTP request data
class UserInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

# for deserializing HTTP response data
class UserOutputSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ("email", "password")  


class BookInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    published_date = serializers.DateField()
    is_recent = serializers.SerializerMethodField()
    
    #get_<field_name> method to compute the value of a SerializerMethodField
    def get_is_recent(self, obj):
        return "alx"
    
    #custom create and update methods
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance
    
    # FIELD-LEVEL VALIDATION
        # validate_field_name method for field-level validation
    def validate_published_date(self, value):
        ...

    def validadte_author(self, value):
        ...

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

 # OBJECT-LEVEL VALIDATION
    def validate(self, data):
        data