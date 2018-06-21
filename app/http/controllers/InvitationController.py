''' A Module Description '''
import requests
from masonite.request import Request
import json

class InvitationController:
    ''' Class Docstring Description '''

    def send(self, request: Request, Session):
        response = requests.post('https://slack.com/api/users.admin.invite', {
            'token': env('SLACK_TOKEN'),
            'email': request.input('email')
        })

        response = json.loads(response.text)
        print(response)
        if 'error' in response:
            request.session.flash('error', response['error'])
        else:
            request.session.flash('success', 'Invitation Successfully Sent!')

        return request.redirect('/')
