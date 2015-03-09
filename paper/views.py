from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import *
from haystack.query import SearchQuerySet



# Question Paper views

def index(request):
	return render_to_response("index.html")



def fetch_qpapers_all(request):
	var = Branch.objects.all()
	return render_to_response("branches.html", {"branches":var},)



def fetch_qpapers_branch(request, branch):
	var = Semester.objects.all()
	return render_to_response("semesters.html",{"semester":var},)


def fetch_qpapers_branch_semester(request, branch, semester):
	bname = Branch.objects.get(branch_code=str(branch.upper()))
	snumber = Semester.objects.get(semester_no=str(semester))
	var = Subject.objects.filter(questionpaper__branch=bname, questionpaper__semester=snumber).distinct()
	return render_to_response("subjects.html", {"subjects":var},)

def fetch_qpapers_branch_semester_subject(request, branch, semester, subject):
	bname = Branch.objects.get(branch_code=str(branch.upper()))
	subject_id = Subject.objects.get(subject_slug=subject)
	snumber = Semester.objects.get(semester_no=str(semester))
	var = QuestionPaper.objects.filter(branch=bname, semester=snumber, subject=subject_id)
	return render_to_response("papers.html", {"papers":var,"subject_name":subject_id},)





### Lab Software Views


def fetch_lab_software_all(request):
	var = Branch.objects.all()
	return render_to_response("branches_lab.html", {"branches":var},)

def fetch_lab_software_branch(request, branch):
	var = Semester.objects.all()
	return render_to_response("semesters_lab.html",{"semester":var},)

def fetch_lab_software_branch_semester(request, branch, semester):
	bname = Branch.objects.get(branch_code=str(branch.upper()))
	snumber = Semester.objects.get(semester_no=str(semester))
	var = LabPackage.objects.filter(branch=bname, semester=snumber)
	return render_to_response("lab_packages.html", {"packages":var},)

def fetch_lab_software_branch_semester_package(request, branch, semester, title_slug):
	bname = Branch.objects.get(branch_code=str(branch.upper()))
	snumber = Semester.objects.get(semester_no=str(semester))
	var = LabPackage.objects.get(branch=bname, semester=snumber, title_slug=str(title_slug))
	return render_to_response("articles.html", {"article":var},)



### Course Notes Views

def fetch_course_notes_all(request):
	var = Branch.objects.all()
	return render_to_response("branches_coursenotes.html", {"branches":var},)


def fetch_course_notes_branch(request, branch):
	var = Semester.objects.all()
	return render_to_response("semesters_cn.html",{"semester":var},)


def fetch_course_notes_branch_semester(request, branch, semester):
	bname = Branch.objects.get(branch_code=str(branch.upper()))
	snumber = Semester.objects.get(semester_no=str(semester))
	var = Subject.objects.filter(coursenotes__branch=bname, coursenotes__semester=snumber, is_a_lab=False).distinct()
	return render_to_response("subjects_cn.html", {"subjects":var},)


def fetch_course_notes_branch_semester_subject(request, branch, semester, subject):
	bname = Branch.objects.get(branch_code=str(branch.upper()))
	subject_id = Subject.objects.get(subject_slug=subject )
	snumber = Semester.objects.get(semester_no=str(semester))
	var = CourseNotes.objects.filter(branch=bname, semester=snumber, subject=subject_id)
	return render_to_response("notes.html", {"notes":var,"subject_name":subject_id},)





# Lab Manual Views

def fetch_lab_manuals_all(request):
	var = Branch.objects.all()
	return render_to_response("branches_lm.html", {"branches":var},)



def fetch_labmanuals_branch(request,branch):
	var = Semester.objects.all()
	return render_to_response("semesters_lm.html",{"semester":var},)



def fetch_lab_manual_branch_semester(request, branch, semester):
	bname = Branch.objects.get(branch_code=str(branch.upper()))
	snumber = Semester.objects.get(semester_no=str(semester))
	var = Subject.objects.filter(labmanual__branch=bname, labmanual__semester=snumber, is_a_lab=True).distinct()
	return render_to_response("subjects_lm.html", {"subjects":var},)


def fetch_lab_manual_branch_semester_subject(request, branch, semester, subject):
	bname = Branch.objects.get(branch_code=str(branch.upper()))
	subject_id = Subject.objects.get(subject_slug=subject, is_a_lab = True)
	snumber = Semester.objects.get(semester_no=str(semester))
	var = LabManual.objects.filter(branch=bname, semester=snumber, subject=subject_id)
	return render_to_response("manuals.html", {"manuals":var,"subject_name":subject_id},)




# Search views

#def search_cousenotes(request):
	#course_notes = SearchQuerySet()autocomplete(content_auto=request.POST.get('coursenotes_text',''))
	#return render_to_response('search.html', {'course_notes':course_notes})
