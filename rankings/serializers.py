from rest_framework import serializers


class SingleRankSerializer(serializers.Serializer):
    name = serializers.CharField()
    abbreviation = serializers.CharField()
    weight = serializers.IntegerField()

class RankingSerializer(serializers.Serializer):
    ranks = SingleRankSerializer(many=True)