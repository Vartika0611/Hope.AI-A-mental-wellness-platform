from django.shortcuts import render
from django.db import models
from .models import PanelMember
from django.shortcuts import render, get_object_or_404
from .models import Assessment, Question

from .models import Assessment, Question
from .models import DepressionTestResult
from django.utils import timezone
from django.shortcuts import render
from .models import AnxietyQuestion
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import OCDTestResult

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
#import openai
import os
import traceback
import json
#from dotenv import load_dotenv
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from django.shortcuts import render
from django.db import models
from .models import PanelMember
from .models import Video
from .models import Music
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import render
from dotenv import load_dotenv
import random
from .models import PanelMember, EmotionReport
from .forms import EmotionReportForm



#chatbot  logic
# load_dotenv()

# client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# load_dotenv(dotenv_path=os.path.join(settings.BASE_DIR, ".env"))




# @csrf_exempt
# def chatbot_api(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             user_message = data.get("message", "")

#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": user_message}
#                 ]
#             )
#             reply = response.choices[0].message.content
#             return JsonResponse({"response": reply})
#         except Exception as e:
#             print("❌ Chatbot error:", e)
#             return JsonResponse({"error": "Something went wrong on the server."}, status=500)
    
#     return JsonResponse({"error": "Invalid request method."}, status=400)

# @csrf_exempt
# def chatbot_api(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             user_message = data.get("message", "")

#             response = client.chat.completions.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": user_message}
#                 ]
#             )

#             reply = response.choices[0].message.content
#             return JsonResponse({"response": reply})

#         except Exception as e:
#             print("❌ Chatbot error:", e)
#             traceback.print_exc()
#             return JsonResponse({"error": "Something went wrong on the server."}, status=500)

#     return JsonResponse({"error": "Invalid request method."}, status=400)


load_dotenv()
from openai import OpenAI
import os

# Load API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ]
            )

            reply = response.choices[0].message.content
            return JsonResponse({"response": reply})

        except Exception as e:
            print("❌ Chatbot error:", e)
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=400)

# chatbot logic
def chatbot(request):
    return render(request, 'chatbot.html')


#hope meet view
# Hope Meet view
def hope_meet_view(request):
    room_name = "hopeai-room-" + str(random.randint(1000, 9999))
    form = EmotionReportForm()
    latest_data = EmotionReport.objects.last()

    chart_data = [
        latest_data.stress,
        latest_data.focus,
        latest_data.mood,
        latest_data.fatigue,
        latest_data.calmness
    ] if latest_data else [0, 0, 0, 0, 0]

    if request.method == 'POST':
        form = EmotionReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hope_meet')

    context = {
        'room_name': room_name,
        'form': form,
        'chart_data': chart_data
    }
    return render(request, 'hope_meet.html', context)





#home page
def home(request):
    return render(request, 'home.html')
def static_panel(request):
    panel_members = [
        {
            "name": "Sudheer Kumar Singh",
            "title": "Ph.D. in Psychology",
            "image": "https://i.ibb.co/7kq35qw/sudheer.jpg",
            "specialties": ["Stress", "Academics", "ADHD"],
            "languages": ["English", "Hindi"],
            "description": "Experienced counselor in student stress management.",
        },
        {
            "name": "Neeta Bhatt",
            "title": "Clinical Psychologist",
            "image": "https://i.ibb.co/Jv9vN7D/neeta.jpg",
            "specialties": ["Overthinking", "Friendship", "Stress"],
            "languages": ["English", "Hindi"],
            "description": "Helping individuals cope with emotional pressure.",
        },
        {
            "name": "Chandra Tiwari",
            "title": "Masters in Counseling",
            "image": "https://i.ibb.co/zSF2zkp/chandra.jpg",
            "specialties": ["Anxiety", "Exam Pressure", "Disorder"],
            "languages": ["English", "Hindi"],
            "description": "Ready to walk you through healing.",
        },
        {
            "name": "Aradhya Solanki",
            "title": "Mental Health Consultant",
            "image": "https://i.ibb.co/qMfvtkX/aradhya.jpg",
            "specialties": ["Loneliness", "Career", "Guidance"],
            "languages": ["English", "Hindi"],
            "description": "Let’s find calmness together.",
        },
    ]
    # return render(request, 'panel.html', {'panel_members': panel_members})
    return render(request, 'panel/panel.html', {'panel_members': panel_members})
    


   

def panel(request):
    query = request.GET.get('q', '').lower()
    members = PanelMember.objects.all()

    if query:
        members = members.filter(
            models.Q(name__icontains=query) |
            models.Q(specialties__icontains=query) |
            models.Q(languages__icontains=query)
        )

    return render(request, 'panel/panel.html', {
        'panel_members': members,
        'query': query
    })



def mem1(request):
    return render(request, 'panel/mem1.html')

def mem2(request):
    return render(request, 'panel/mem2.html')

def mem3(request):
    return render(request, 'panel/mem3.html')

def mem4(request):
    return render(request, 'panel/mem4.html')

def mem5(request):
    return render(request, 'panel/mem5.html')

def mem6(request):
    return render(request, 'panel/mem6.html')

def mem7(request):
    return render(request, 'panel/mem7.html')

def mem8(request):
    return render(request, 'panel/mem8.html')

def booking(request):
    return render(request, 'panel/booking.html')

def payment(request):
    return render(request, 'panel/payment.html')


def home(request):
    return render(request, 'home.html') 




#questionnaire
def questionnaire_list(request):
    assessments = Assessment.objects.all()
    return render(request, 'questionnaire_list.html')

def assessment_detail(request, assessment_id):
    assessment = get_object_or_404(Assessment, id=assessment_id)
    questions = assessment.questions.all()
    return render(request, 'main/assessment_detail.html', {
        'assessment': assessment,
        'questions': questions
    })

# test_pages
def personality_test(request):
    return render(request, 'personality_test.html')

def stress_level_test(request):
    return render(request, 'stress_level_test.html')


# depression_test


def depression_test(request):
    # Define the 12 questions here
    questions = {
        1: "Little interest or pleasure in doing things?",
        2: "Feeling down, depressed, or hopeless?",
        3: "Trouble sleeping or sleeping too much?",
        4: "Feeling tired or having little energy?",
        5: "Poor appetite or overeating?",
        6: "Feeling bad about yourself?",
        7: "Trouble concentrating?",
        8: "Feeling restless or slowed down?",
        9: "Thoughts of self-harm or death?",
        10: "Feeling lonely or isolated?",
        11: "Low self-esteem?",
        12: "Feeling overwhelmed by daily life?"
    }

    if request.method == 'POST':
        answers = [int(request.POST.get(f'q{i}', 0)) for i in range(1, 13)]
        total_score = sum(answers)

        DepressionTestResult.objects.create(
            user=request.user if request.user.is_authenticated else None,
            score=total_score
        )

        return render(request, 'depression_test_result.html', {'score': total_score})

    return render(request, 'depression_test.html', {'questions': questions})

# anxiety test


def anxiety_test(request):
    return render(request, 'anxiety_test.html')

#OCD TEST

def OCD_test(request):
    return render(request, 'OCD_test.html')


@csrf_exempt
def save_ocd_result(request):
    if request.method == 'POST':
        try:
            score = int(request.POST.get('score', 0))
            if score <= 12:
                level = "Minimal or no OCD symptoms"
            elif score <= 24:
                level = "Moderate OCD symptoms"
            else:
                level = "Severe OCD symptoms"

            OCDTestResult.objects.create(score=score, level=level)
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
#sleep_quality test

def sleep_quality_test(request):
    questions = {
        1: "I have difficulty falling asleep.",
        2: "I wake up in the middle of the night or early morning.",
        3: "I feel refreshed upon waking up.",
        4: "I use sleep medication.",
        5: "I experience daytime sleepiness.",
        6: "I have trouble staying asleep throughout the night.",
        7: "I wake up too early and cannot fall back asleep.",
        8: "I feel tired or low-energy during the day.",
        9: "I feel anxious or stressed before bedtime.",
        10: "I wake up due to discomfort (pain, bathroom needs).",
        11: "I have vivid or disturbing dreams.",
        12: "I nap frequently during the day."
    }
    return render(request, 'sleep_quality_test.html', {'questions': questions})


def self_esteem_test(request):
    return render(request, 'self_esteem_test.html')

#ptsd

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import PTSDTestResult
def PTSD_test(request):
    return render(request, 'PTSD_test.html')
@csrf_exempt
def save_ptsd_result(request):
    if request.method == 'POST':
        data = request.POST
        total_score = sum(int(data.get(f'q{i}', 0)) for i in range(1, 13))

        result = PTSDTestResult.objects.create(
            q1=data.get('q1'),
            q2=data.get('q2'),
            q3=data.get('q3'),
            q4=data.get('q4'),
            q5=data.get('q5'),
            q6=data.get('q6'),
            q7=data.get('q7'),
            q8=data.get('q8'),
            q9=data.get('q9'),
            q10=data.get('q10'),
            q11=data.get('q11'),
            q12=data.get('q12'),
            total_score=total_score
        )
        return JsonResponse({'status': 'success', 'score': total_score})
    return JsonResponse({'status': 'fail'})


def depression_test_result(request):
    return render(request, 'depression_test_result.html')

#login logic(vartika)
def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # or your desired page
        else:
            error = "Invalid credentials. Please try again."

    return render(request, 'login.html', {'error': error})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'main/logout_success.html')
    else:
        return render(request, 'main/invalid_logout.html', status=405)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        category = request.POST.get("category")
        subcategory = request.POST.get("subcategory")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # Adjust redirection as needed
        else:
            return render(request, 'main/login.html', {'error': 'Invalid credentials'})

    return render(request, 'main/login.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})


def music_library(request):
    genre_filter = request.GET.get('genre')
    if genre_filter:
        musics = Music.objects.filter(genre__iexact=genre_filter)
    else:
        musics = Music.objects.all()
    
    genres = Music.objects.values_list('genre', flat=True).distinct()
    return render(request, 'main/music.html', {'musics': musics, 'genres': genres})

def video_library(request):
    genre_filter = request.GET.get('genre')
    if genre_filter:
        videos = Video.objects.filter(genre__iexact=genre_filter)
    else:
        videos = Video.objects.all()

    genres = Video.objects.values_list('genre', flat=True).distinct()
    return render(request, 'main/video.html', {'videos': videos, 'genres': genres})



