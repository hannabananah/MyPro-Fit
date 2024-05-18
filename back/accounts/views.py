from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class DeleteAccountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
