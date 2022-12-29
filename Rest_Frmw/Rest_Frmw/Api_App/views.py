from django.shortcuts import render
from rest_framework.views import APIView
from .models import Expense
from Api_App.serializers import ExpenseSerializers
from rest_framework.response import Response
from django.forms.models import model_to_dict

# Create your views here.
class ExpenseListCreate(APIView):
    def get(self,request):
        expenses = Expense.objects.all()
        all_expenses = ExpenseSerializers(expenses,many=True)
        return Response(all_expenses)
    def post(self,request):
        serializers = ExpenseSerializers(data = request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response(serializers.data)