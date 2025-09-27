from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User, Course, Purchase
from .serializers import RegisterSerializer, UserSerializer, CourseSerializer, PurchaseSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    # uses SimpleJWT's serializer to return access and refresh tokens
    pass

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            # optionally clear stored refresh token on user
            request.user.refresh_token = ''
            request.user.save()
            return Response({'status':'success','message':'Logged out'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status':'failed','message':str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.AllowAny,)

class CourseRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.AllowAny,)

class PurchaseCreateView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        course_id = request.data.get('course_id')
        amount = request.data.get('amount')
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'status':'failed','message':'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        purchase = Purchase.objects.create(user=request.user, course=course, amount=amount or course.price)
        return Response({'status':'success','purchase': PurchaseSerializer(purchase).data})

class MyPurchasesListView(generics.ListAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user).select_related('course')
