# from django.shortcuts import render
# from rest_framework import permissions
# from rest_framework.viewsets import ModelViewSet
#
# from apps.comments.models import Comments
# from apps.common.utils.auth import JwtAuthentication
#
#
# class CommentsViewset(ModelViewSet):
#     queryset = Comments.objects.order_by('created_on')
#     serializer_class = CommentsSerializer
#     authentication_classes = JwtAuthentication
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly]
