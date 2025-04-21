import requests

def send_to_gsheet_free(team, members):
    url = 'https://script.google.com/macros/s/AKfycbxkQFCKxU3emHAUyQhbBoNf9IApfuUvWF4ZcShKcGtojaR6T5JHXZ_Uh3ZMgrSTxONY/exec'

    for m in members:
        data = {
            'team_name': team.team_name,
            'email': team.email,
            'name': m.name,
            'role': m.role,
            'whatsapp': m.whatsapp,
            'institution': m.institution,
            'major': m.major,
            'batch': m.batch,
            'student_id_card': m.student_id_card.url if m.student_id_card else '',
            'proof_mention': m.proof_mention.url if m.proof_mention else '',
            'registration_post': m.registration_post.url if m.registration_post else '',
            'proof_following': m.proof_following.url if m.proof_following else '',
            'proof_posting': m.proof_posting.url if m.proof_posting else '',
        }

        try:
            response = requests.post(url, data=data)
            print(f"Submitted to Google Sheets: {response.status_code} - {response.text}")
        except Exception as e:
            print("Google Sheets integration failed:", e)
