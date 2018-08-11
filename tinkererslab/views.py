from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,"tl/index.html",{'title' : 'Home'});

def wishlist(request):
	return render(request,"tl/wishlist.html",{'title':'Wishlist'});

def events(request):
	return render(request,"tl/events.html",{'title':'Events'});

def about(request):
	return render(request,"tl/about.html",{'title':'About'});

def gallery(request):
	return render(request,"tl/gallery.html",{'title':'Gallery'});

def resources(request):
	return render(request,"tl/resources.html",{'title':'Resources'});

def team(request):
	return render(request,"tl/team.html",{'title':'Team'});

def feedback(request):
	return render(request,"tl/feedback.html",{'title':'Feedback'});

def contact(request):
	return render(request,"tl/contact.html",{'title':'Contact'});

def thank(request):
	return render(request,"tl/thankyou.html",{'title':''});


