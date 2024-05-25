from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserProductSerializer

User = get_user_model()


class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return Response(
            {"detail": "계정이 성공적으로 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT
        )
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def joined_products(request):
    serializer = UserProductSerializer(request.user)
    return Response(serializer.data)
