from rest_framework import serializers


class OfficiatorRankSerializer(serializers.Serializer):
    name = serializers.CharField()
    weight = serializers.IntegerField()


class OfficiatorEnforcementSerializer(serializers.Serializer):
    date = serializers.DateField(input_formats=['%d-%m-%Y'])
    service_type = serializers.CharField()
    officiation = serializers.CharField()

class OfficiatorDtoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    rank = OfficiatorRankSerializer()
    can_conduct_on_weekdays = serializers.BooleanField()
    can_read_on_weekdays = serializers.BooleanField()
    can_preach_on_weekdays = serializers.BooleanField()
    can_conduct_on_sundays = serializers.BooleanField()
    can_read_on_sundays = serializers.BooleanField()
    can_preach_on_sundays = serializers.BooleanField()
    enforcements = OfficiatorEnforcementSerializer(many=True, allow_null=True)

class RosterDataSerializer(serializers.Serializer):
    #for TESTING
    email = serializers.EmailField()
    temp_user = serializers.CharField()  


    month = serializers.CharField()
    year = serializers.CharField()
    bible_lesson_file = serializers.CharField()
    officiators = OfficiatorDtoSerializer(many=True)


class LessonSerializer(serializers.Serializer):
    lesson = serializers.CharField()
    reader = serializers.CharField()

class ServiceSerializer(serializers.Serializer):
    date = serializers.DateField()
    day = serializers.CharField()
    conductor = serializers.CharField()
    first_lesson = LessonSerializer()
    second_lesson = LessonSerializer(allow_null=True)
    preacher = serializers.CharField()

class RosterSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    month = serializers.CharField()
    year = serializers.CharField()
    roster = ServiceSerializer(many=True)

class FileUploadSerializer(serializers.Serializer):
    roster = serializers.FileField()