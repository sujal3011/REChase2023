from django.shortcuts import render, redirect
from teams.models import Team, Player
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import answerForm
from .models import Question
from teams.decorators import team_required

THIS_LEVEL = 12


@login_required
@team_required
def home(request):
    context = {}
    user = request.user
    profile = Player.objects.get(user=user)
    team = Team.objects.get(id=profile.team.pk)

    if team.current_level != THIS_LEVEL:
        return redirect(reverse_lazy('teams:get-level'))

    question = Question.objects.all().first()
    answer = answerForm(request.POST or None)
    context['team'] = team
    context['question'] = question
    context['profile'] = profile
    
    correct_ans = "INCORRECT"
    context['answer'] = answer
    if request.method == 'POST':
        if answer.is_valid():
            ans = answer.cleaned_data['answer'].upper()
            if correct_ans == ans:
                team.answerCorr(THIS_LEVEL, correct_ans)
                question.answered(right=1)
                return redirect(reverse_lazy('teams:get-level'))

            else:
                question.answered(right=0)
                context['wrong'] = 1
        else:
            context['invalid'] = 1

    return render(request, 'xor12/question.html', context)
