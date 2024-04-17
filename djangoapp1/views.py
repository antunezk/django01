from django.shortcuts import render

def index(request):
    return render(request, 'student/index.html')

def greeting(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        school = request.POST.get('school')
        grade = request.POST.get('grade')

        if grade.lower() == 'freshman':
            message = f"Welcome to {school}, {name}!"
        elif grade.lower() == 'senior':
            message = f"Congratulations on graduating from {school}, {name}!"
        else:
            message = f"Welcome, {name}! Enjoy your time at {school}."

        return render(request, 'student/greeting.html', {'message': message})
    else:
        return render(request, 'student/index.html')
