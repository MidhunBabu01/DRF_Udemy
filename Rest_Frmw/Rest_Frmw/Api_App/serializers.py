from rest_framework import serializers
from Api_App.models import Expense





class ExpenseSerializers(serializers.ModelSerializer):
    amount = serializers.FloatField(required = True)
    merchant = serializers.CharField(required = True)
    description = serializers.CharField(required = False)
    category = serializers.CharField(required = True)
    date_created = serializers.DateTimeField(required = False)
    date_updated = serializers.DateTimeField(required = False)
    class Meta:
        model = Expense
        fields = "__all__"
        read_only_fields = ['id','date_created','date_updated']