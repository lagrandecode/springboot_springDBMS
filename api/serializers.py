from rest_framework import serializers
from .models import Student, Teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate_student_id(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Student ID must contain only letters and numbers.")
        return value

    def validate_parent_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Parent contact must contain only numbers.")
        return value

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate_teacher_id(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Teacher ID must contain only letters and numbers.")
        return value

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only numbers.")
        return value 