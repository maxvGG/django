from django.shortcuts import render
from .models import Questionnaire, Question, Answer

from django.http import HttpResponse

def index(request):
    all_questionnaires = Questionnaire.objects.all()
    all_questions = Question.objects.all()
    return render(request, 'questions/index.html', locals())
    # return HttpResponse("base dir path", BASE_DIR)

def questionnaire_detail(request, questionnaire_id):
    questionnaire = Questionnaire.objects.get(id=questionnaire_id)
    questions = Question.objects.filter(questionnaire=questionnaire)
    return render(request, 'questions/questionnaire.html',
                  {'questionnaire': questionnaire, 'questions': questions})

# def new_questions(request):
#     if request.method == "POST":
#         if form.is_valid():
#             obj = Question()
#             obj.question_text = form.cleaned_data['Questionnaire']
#             obj.save()
#             if obj.save():
#                 return HttpResponse('obj saved')
