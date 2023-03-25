from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import LeaveApplicationForm

def leave_application(request):
    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Leave/thankyou.html')
    else:
        form = LeaveApplicationForm()
    return render(request, 'Leave/leave_application.html', {'form': form})
