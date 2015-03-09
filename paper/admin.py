from django.contrib import admin
from paper.models import *
from django.db import models
from django import forms

class ProjectAdmin(admin.ModelAdmin):

    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
    prepopulated_fields = {'title_slug':('title',),}

    class Media:
        js = ('ckeditor/ckeditor.js',)

admin.site.register(Branch)


###################################################################

class SubjectAdmin(admin.ModelAdmin):
	prepopulated_fields = {'subject_slug':('subject_name',),}

admin.site.register(Subject, SubjectAdmin)

####################################################################




admin.site.register(Semester)
admin.site.register(Year)
admin.site.register(QuestionPaper)
admin.site.register(CourseNotes)
admin.site.register(LabManual)
admin.site.register(LabPackage, ProjectAdmin)
