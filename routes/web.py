''' Web Routes '''
from masonite.routes import Get, Post

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),
    Post().route('/invite', 'InvitationController@send').name('welcome'),
]
