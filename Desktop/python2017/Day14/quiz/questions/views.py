from django.http import HttpResponse
from .models import Person, ClassRoom
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

def index(request):
	courses = ClassRoom.objects.all()

	html = "<ul>"

	for course in courses:
		html = html+"<li>"+course.name+"</li>"

	html = html+"</ul>"

	return HttpResponse(html)


def aboutus(request):

	courses = ClassRoom.objects.all()

	html = "<select>"

	for course in courses:
		html = html+"<option>"+course.name+"</option>"

	html = html+"</select>"

	return HttpResponse(html)


def courses(request):
	subjects = ClassRoom.objects.all()
	template = loader.get_template("index.html")
	context = {
		"subjects":subjects,
		"name":"youstart",
		"heading":"Hello"
	}
	return HttpResponse(template.render(context,request))

def form(request):
	subjects = ClassRoom.objects.all()
	template = loader.get_template("form.html")
	context = {
		"subjects":subjects,
	}
	return HttpResponse(template.render(context,request))

@csrf_exempt
def submit(request):

	fname = request.POST.get("first_name")
	lname = request.POST.get("last_name")
	roll = request.POST.get("roll_no")
	c = request.POST.get("course")

	p1  = Person()
	p1.first_name = fname
	p1.last_name = lname
	p1.roll_no = int(roll)
	p1.class_room_id = int(c)
	p1.save()

	course = ClassRoom.objects.get(id=p1.class_room_id)
	print(course)

	registered = Person.objects.filter(class_room_id=p1.class_room_id)

	template = loader.get_template("register.html")
	context = {
		"registered":registered,
		"course":course,
		"person":p1
	}


	return HttpResponse(template.render(context,request))



