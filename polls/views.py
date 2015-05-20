from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# from django.template import RequestContext, loader

from .models import Question

def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list}
	return render(request,'polls/index.html',context)
	# template=loader.get_template('polls/index.html')
	# context = RequestContext(request,{'latest_question_list':latest_question_list,})
	# output=','.join([p.question_text for p in latest_question_list])
	return HttpResponse(template.render(context))

def detail(request,question_id):
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExit:
	# 	raise Http404("Question does not exit")
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})

	
	# return HttpResponse("You are looking at question %s." % question_id)

def results(request,question_id):
	response="You are looking at the request of question %s."
	return HttpResponse(response % question_id)

def vote(request,question_id):
	return HttpResponse("You are voting on question %s." % question_id)
