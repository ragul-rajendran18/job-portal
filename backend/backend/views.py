from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from backend.serializers import Applicationserializer, Jobserializer, RegisterSerializer
from django.contrib.auth.models import User
from .models import Application, Job

@api_view(['GET'])
def hello_api(request):
    return Response({"message":"hello from django API"})

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"success"}, status=status.HTTP_201_CREATED)
   
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POSt'])
def basic_login(request):
    username=request.data.get('username')
    password=request.data.get('password')

    try:
        user = User.objects.get(username=username,password=password)
        return Response({"user_id":user.id ,"username":user.username , "message": "login success"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"message": "invalid credential"}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])    
def job_list(request):
    jobs = Job.objects.all()
    serializer = Jobserializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def apply_job(request):
    seriallizer=Applicationserializer(data=request.data)
    job_id= request.data.get("job")
    applicant_id = request.data.get("Applicant")
    if Application.objects.filter(job_id=job_id , Applicant_id=applicant_id).exists():
          return Response({"message":"already applied"}, status=status.HTTP_400_BAD_REQUEST)
    if seriallizer.is_valid():
        seriallizer.save()
        return Response({"message":"Application Submitted"}, status=status.HTTP_202_ACCEPTED)
    return Response(seriallizer.errors, status=status.HTTP_400_BAD_REQUEST)