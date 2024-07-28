from rest_framework import serializers
from .models import AttackTitan,MyHero,JujutsuKaisen

class  AttackTitanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttackTitan
        fields = ["id", "name", "status", "ability", "image"]

class  MyHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyHero
        fields = ["id", "name", "status", "ability", "image"]

class  JujutsuKaisenSerializer(serializers.ModelSerializer):
    class Meta:
        model = JujutsuKaisen
        fields = ["id", "name", "status", "ability", "image"]




