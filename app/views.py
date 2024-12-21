from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics, viewsets, mixins, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@permission_classes([IsAuthenticated])
class BrainBytesViewSet(viewsets.ModelViewSet):
    queryset = BrainBytes.objects.all()
    serializer_class = BrainBytesSerializer


class CommentsBViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsBSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Получаем комментарии только для конкретного видео
        video_pk = self.kwargs.get('video_pk')
        return CommentsB.objects.filter(video_id=video_pk).order_by('-created_at')

    def perform_create(self, serializer):
        # Устанавливаем автора и видео автоматически
        video_pk = self.kwargs.get('video_pk')
        video = BrainBytes.objects.get(pk=video_pk)
        serializer.save(video=video)


@permission_classes([IsAuthenticated])
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@permission_classes([IsAuthenticated])
class ResearchViewSet(viewsets.ModelViewSet):
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer


@permission_classes([IsAuthenticated])
class CooperationViewSet(viewsets.ModelViewSet):
    queryset = Cooperation.objects.all()
    serializer_class = CooperationSerializer


class CommentsCViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsCSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Получаем комментарии только для конкретного видео
        video_pk = self.kwargs.get('video_pk')
        return CommentsC.objects.filter(video_id=video_pk).order_by('-created_at')

    def perform_create(self, serializer):
        # Устанавливаем автора и видео автоматически
        video_pk = self.kwargs.get('video_pk')
        video = Post.objects.get(pk=video_pk)
        serializer.save(video=video)


class LikeBrainBytesView(APIView):
    def post(self, request, pk):
        try:
            brain_byte = BrainBytes.objects.get(pk=pk)
            brain_byte.likes += 1
            brain_byte.save()
            return Response({"likes": brain_byte.likes}, status=status.HTTP_200_OK)
        except BrainBytes.DoesNotExist:
            return Response({"error": "Объект не найден"}, status=status.HTTP_404_NOT_FOUND)


class ShareBrainBytesView(APIView):
    def post(self, request, pk):
        try:
            brain_byte = BrainBytes.objects.get(pk=pk)
            brain_byte.shares += 1
            brain_byte.save()
            return Response({"shares": brain_byte.shares}, status=status.HTTP_200_OK)
        except BrainBytes.DoesNotExist:
            return Response({"error": "Объект не найден"}, status=status.HTTP_404_NOT_FOUND)

