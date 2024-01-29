from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
# models 파일과 admin 파일을 항상 같이 수정!
admin.site.register(Question)
admin.site.register(Choice)
