from django.shortcuts import render

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .llm_core import chat_with_memory

chat_history = []

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            # If this is an AJAX request (JSON API)
            user_message = request.POST.get('message') or request.GET.get('message')
            if not user_message:
                return JsonResponse({'error': 'Message required'}, status=400)
            response = chat_with_memory(user_message)
            chat_history.append(('user', user_message))
            chat_history.append(('bot', response))
            return JsonResponse({'response': response})
        else:
            # Standard form submission
            user_message = request.POST.get('message')
            if user_message:
                response = chat_with_memory(user_message)
                chat_history.append(('user', user_message))
                chat_history.append(('bot', response))
            return render(request, 'chat.html', {'chat_history': chat_history})

    return render(request, 'chat.html', {'chat_history': chat_history})
    