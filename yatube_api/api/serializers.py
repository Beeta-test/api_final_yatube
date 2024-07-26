from djoser.serializers import UserSerializer
from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'author',
            'image',
            'group',
            'pub_date'
        )


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')

    def validate_following(self, value):
        if self.context['request'].user == value:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя.")
        return value

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']

        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого пользователя.")
        return data
