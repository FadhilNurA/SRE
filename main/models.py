from django.db import models

class Team(models.Model):
    email = models.EmailField()
    team_name = models.CharField(max_length=100)

class Member(models.Model):
    ROLE_CHOICES = [('leader', 'Leader'), ('member1', 'Member 1'), ('member2', 'Member 2')]

    team = models.ForeignKey(Team, related_name='members', on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    name = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    institution = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    batch = models.CharField(max_length=10)
    student_id_card = models.FileField(upload_to='id_cards/')
    proof_mention = models.FileField(upload_to='proof_mentions/')
    registration_post = models.FileField(upload_to='reg_posts/')
    proof_following = models.FileField(upload_to='following/')
    proof_posting = models.FileField(upload_to='postings/', null=True, blank=True)
