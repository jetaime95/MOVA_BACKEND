from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from notice.models import Notice
from notice.serializers import NoticeSerializer


# Create your views here.

class NoticeView(APIView):
    def get(self, request):
        notice = Notice.objects.all()
        serializer = NoticeSerializer(notice, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

class NoticeDetailView(APIView):
    def get(self, request, notice_id):
        notice = Notice.objects.get(id=notice_id)
        serializer = NoticeSerializer(notice)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, notice_id):
        notice = Notice.objects.get(id=notice_id)
        if request.user == notice.user:
            serializer = NoticeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)     