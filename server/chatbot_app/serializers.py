from rest_framework import serializers

class ChatbotSerializer(serializers.Serializer):
    user_query = serializers.CharField()
    bot_response = serializers.CharField()
