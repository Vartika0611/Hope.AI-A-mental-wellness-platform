from django.contrib import admin
from .models import PanelMember
from .models import Assessment, Question
from .models import OCDTestResult
from .models import PTSDTestResult
from .models import Music
from .models import Video

admin.site.register(Music)
admin.site.register(Video)


admin.site.register(PanelMember)
admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register(OCDTestResult)
admin.site.register(PTSDTestResult)

