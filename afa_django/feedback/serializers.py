
from rest_framework import serializers

from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Feedback
        fields = (
            "name",
            "family_name",
            "phone",
            "email",
            "message",
        )