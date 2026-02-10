from django.shortcuts import render
from django.views.generic import View ,TemplateView
from fishta.tasks import subtract, calculate_task, factorial_task
from celery.result import AsyncResult
# Create your views here.

# enqueuing the task using delay
# class HomeView(View):
#     def get(self, request):
#       print('Results: ')
      
#       result1 = subtract.apply_async(args=[40, 20])
#       print("Result1:", result1)
#       result2 = calculate_task.apply_async(args=[10, 5])
#       print("Result2:", result2)
#       result3 = factorial_task.delay(9)
#       print("Result3:", result3)
#       return render(request, 'fishta/home.html')
  
# enqueuing the task using the apply_async()
# class HomeView(View):
#     def get(self, request):
#       print('Results: ')
      
#       result1 = subtract.delay(40, 20)
#       print("Result1:", result1)
#       result2 = calculate_task.delay(10, 5)
#       print("Result2:", result2)
#       result3 = factorial_task.delay(9)
#       print("Result3:", result3)
#       return render(request, 'fishta/home.html')
  
# displaying the subtract value after the task execution
class HomeView(View):
    def get(self, request):
        print('Results: ')
        result = subtract.delay(50, 15)
        return render(request, 'fishta/home.html', {'result':result})
    
class CheckResultView(View):
    template_name = 'fishta/result.html'
    
    def get(self, request, task_id):
    # Retrieving the task result using the task_id
      result = AsyncResult(task_id)
      context = {'result':result}
      return render(request, self.template_name, context)
        
    
class AboutView(TemplateView):
    template_name = 'fishta/about.html'
    
class ContactView(TemplateView):
    template_name = 'fishta/contact.html'