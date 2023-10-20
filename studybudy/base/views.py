from django.shortcuts import render

# Create your views here.
rooms = [
    {
        'id': 1, 
        'name': 'Let\'s learn Python!',
        'instructor': 'John Doe',
        'description': 'This room is for learning Python.',
        'image': 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png'
    },
    {
        'id': 2,
        'name': 'Let\'s learn JavaScript!',
        'instructor': 'Jane Doe',
        'description': 'This room is for learning JavaScript.',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png'
    },
    {
        'id': 3,
        'name': 'Let\'s learn Django!',
        'instructor': 'John Doe',
        'description': 'This room is for learning Django.',
        'image': 'https://static.djangoproject.com/img/logos/django-logo-positive.png'
    }
]

context = {
    'rooms': rooms
}

def index(request):
    return render(request, 'base/index.html', context)

def room(request):
    return render(request, 'base/room.html')
