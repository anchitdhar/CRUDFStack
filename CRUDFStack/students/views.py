from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics
from rest_framework import mixins 


class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
						mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
	serializer_class = StudentSerializer
	queryset = Student.objects.all()
	lookup_field='pk'

	def get(self,request, pk=None):
		if pk:
			return self.retrieve(request)
		else:
			return self.list(request)

	def post(self,request):
		return self.create(request)

	def put(self,request,pk =None):
		return self.update(request, pk)

	def delete(self,request,pk):
		return self.destroy(request,pk)