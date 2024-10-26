from rest_framework import serializers
from django.apps import apps
from users.models import CustomUser


class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = apps.get_model('projects.Genre')
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = apps.get_model('projects.Band')
        fields = '__all__'

class BandDetailSerializer(serializers.ModelSerializer):
    # genre = GenreSerializer(many=True, read_only=True)
    genre = serializers.PrimaryKeyRelatedField(queryset=apps.get_model('projects.Genre').objects.all(), many=True)

    class Meta:
        model = apps.get_model('projects.Band')
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.country = validated_data.get('country', instance.country)
        instance.description = validated_data.get('description', instance.description)
        instance.cover_image = validated_data.get('cover_image', instance.cover_image)
        instance.website = validated_data.get('website', instance.website)
        instance.is_current = validated_data.get('is_current', instance.is_current)
        instance.owner = validated_data.get('owner', instance.owner)        
        if 'genre' in validated_data:
            genre_data = validated_data.pop('genre')
            instance.genre.set(genre_data)
        instance.save()
        return instance


class TourSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    genre = serializers.PrimaryKeyRelatedField(queryset=apps.get_model('projects.Genre').objects.all(), many=True)

    class Meta:
        model = apps.get_model('projects.Tour')
        fields = '__all__'


class TourDetailSerializer(serializers.ModelSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        # instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        # instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        if 'genre' in validated_data:
            genre_data = validated_data.pop('genre')
            instance.genre.set(genre_data)
        instance.save()
        return instance
    
    class Meta:
        model = apps.get_model('projects.Tour')
        fields = '__all__'    

