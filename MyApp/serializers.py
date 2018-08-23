from MyApp.models import Users

from rest_framework import serializers


class UserSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Users
		fields = ('name','age', )