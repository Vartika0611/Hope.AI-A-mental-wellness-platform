from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import hope_meet_view
from .views import chatbot_api, chatbot
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('chatbot_api/', views.chatbot_api, name='chatbot_api'),

    path('hope-meet/', hope_meet_view, name='hope_meet'),
    path('panel/', views.panel, name='panel'),
    path('panel/panel/', views.panel, name='panel'),  # Optional redundancy

    # Team members
    path('panel/mem1/', views.mem1, name='mem1'),
    path('panel/mem2/', views.mem2, name='mem2'),
    path('panel/mem3/', views.mem3, name='mem3'),
    path('panel/mem4/', views.mem4, name='mem4'),
    path('panel/mem5/', views.mem5, name='mem5'),
    path('panel/mem6/', views.mem6, name='mem6'),
    path('panel/mem7/', views.mem7, name='mem7'),
    path('panel/mem8/', views.mem8, name='mem8'),

    # Booking and payment
    path('panel/booking/', views.booking, name='booking'),
    path('panel/payment/', views.payment, name='payment'),

    # Other pages
    path('questionnaire_list/', views.questionnaire_list, name='questionnaire_list'),
    path('music/', views.music_library, name='music'),
    path('videos/', views.video_library, name='videos'),
    # path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('contact/', views.contact_us, name='contact'),
    
    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    # Admin
    path('admin/', admin.site.urls),

    # Mental health tests
    path('depression_test/', views.depression_test, name='depression_test'),
    path('personality_test/', views.personality_test, name='personality_test'),
    path('stress_level_test/', views.stress_level_test, name='stress_level_test'),
    path('anxiety_test/', views.anxiety_test, name='anxiety_test'),
    path('OCD_test/', views.OCD_test, name='OCD_test'),
    path('sleep_quality_test/', views.sleep_quality_test, name='sleep_quality_test'),
    path('self_esteem_test/', views.self_esteem_test, name='self_esteem_test'),
    path('PTSD_test/', views.PTSD_test, name='PTSD_test'),

    # Result saving
    path('depression_test_result/', views.depression_test_result, name='depression_test_result'),
    path('save_ocd_result/', views.save_ocd_result, name='save_ocd_result'),
    path('save_ptsd_result/', views.save_ptsd_result, name='save_ptsd_result'),
]

# Static and media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
