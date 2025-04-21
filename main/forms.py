from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['email', 'team_name']
from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'name', 'whatsapp', 'institution', 'major', 'batch',
            'student_id_card', 'proof_mention', 'registration_post', 
            'proof_following', 'proof_posting'
        ]
