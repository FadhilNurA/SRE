from django.shortcuts import render, redirect
from .forms import TeamForm, MemberForm
from .models import Member
from .utils import send_to_gsheet_free

def register_team(request):
    if request.method == 'POST':
        team_form = TeamForm(request.POST)
        leader_form = MemberForm(request.POST, request.FILES, prefix='leader')
        member1_form = MemberForm(request.POST, request.FILES, prefix='member1')
        member2_form = MemberForm(request.POST, request.FILES, prefix='member2')

        if team_form.is_valid() and leader_form.is_valid() and member1_form.is_valid() and member2_form.is_valid():
            team = team_form.save()

            for form, role in [(leader_form, 'leader'), (member1_form, 'member1'), (member2_form, 'member2')]:
                member = form.save(commit=False)
                member.team = team
                member.role = role
                member.save()

            # Kirim ke Google Sheets (GRATIS)
            members = team.members.all().order_by('role')
            send_to_gsheet_free(team, members)

            return redirect('success')
    else:
        team_form = TeamForm()
        leader_form = MemberForm(prefix='leader')
        member1_form = MemberForm(prefix='member1')
        member2_form = MemberForm(prefix='member2')

    return render(request, 'registration_form.html', {
        'team_form': team_form,
        'leader_form': leader_form,
        'member1_form': member1_form,
        'member2_form': member2_form,
    })

def success(request):
    return render(request, 'success.html')

def sre_home(request):
    return render(request, 'sre.html')
