from django.db import models
from django.template.defaultfilters import slugify

class Branch(models.Model):
	branch_code = models.CharField(max_length=6)
	branch_name = models.CharField(max_length=255)


	def __unicode__(self):
		return self.branch_name
	class Meta:
	        verbose_name_plural = "Branches"

class Semester(models.Model):
	semester_no = models.IntegerField(max_length=1)
	semester_name = models.CharField(max_length=20)
	no_of_subjects = models.IntegerField(max_length=2)

	def __unicode__(self):
		return self.semester_name

	class Meta:
	        verbose_name_plural = "Semesters"




class Subject(models.Model):
	subject_code = models.CharField(max_length=10, primary_key=True)
	subject_name = models.CharField(max_length=255)
	subject_slug = models.SlugField()
	is_a_lab = models.BooleanField(default=False)

	def __unicode__(self):
		return self.subject_name

class Year(models.Model):
	year_name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.year_name

class QuestionPaper(models.Model):
	branch = models.ForeignKey('Branch')
	semester = models.ForeignKey('Semester')
	subject = models.ForeignKey('Subject')
	year = models.ForeignKey('Year')
	qpaper=models.FileField()

	class Meta:
		unique_together=(('subject','year'),)


	def __unicode__(self):
		return '%s >> %s' % (self.subject.subject_name,self.year.year_name)


class CourseNotes(models.Model):
	title = models.CharField(max_length=255)
	branch = models.ForeignKey('Branch')
	semester = models.ForeignKey('Semester')
	subject = models.ForeignKey('Subject')
	notes=models.FileField()


	def __unicode__(self):
		return self.title

	class Meta:
	        verbose_name_plural = "Course notes"



class LabManual(models.Model):
	title = models.CharField(max_length=255)
	branch = models.ForeignKey('Branch')
	semester = models.ForeignKey('Semester')
	subject = models.ForeignKey('Subject')
	manual = models.FileField(upload_to='media/lab-manuals')
	def __unicode__(self):
		return self.title



class LabPackage(models.Model):

	title = models.CharField(max_length=255)
	branch = models.ForeignKey('Branch')
	semester = models.ForeignKey('Semester')
	body = models.TextField(blank=True)
	title_slug = models.SlugField()

	def __unicode__(self):
		return self.title
