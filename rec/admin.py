from django.contrib import admin
from recomendation.rec.models import *

class OurUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(OurUser,OurUserAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('call',)
admin.site.register(Movie,MovieAdmin)

class ScoreRankAdmin(admin.ModelAdmin):
    list_display = ('user','rank','film')
admin.site.register(ScoreRank,ScoreRankAdmin)

class BitRankAdmin(admin.ModelAdmin):
    list_display = ('user','rank','film')
admin.site.register(BitRank,BitRankAdmin)

class TriRankAdmin(admin.ModelAdmin):
    list_display = ('user','rank','film')
admin.site.register(TriRank,TriRankAdmin)

class Range10EuclidDistanceAdmin(admin.ModelAdmin):
    list_display = ('user','user2','range10')
admin.site.register(Range10EuclidDistance,Range10EuclidDistanceAdmin)

class Range10CorrelationOfPearsonAdmin(admin.ModelAdmin):
    list_display = ('user','user2','range10')
admin.site.register(Range10CorrelationOfPearson,Range10CorrelationOfPearsonAdmin)

class Range10IndexOfJaccardAdmin(admin.ModelAdmin):
    list_display = ('user','user2','range10')
admin.site.register(Range10IndexOfJaccard,Range10IndexOfJaccardAdmin)

class Range10ManhattanDistanseAdmin(admin.ModelAdmin):
    list_display = ('user','user2','range10')
admin.site.register(Range10ManhattanDistanse,Range10ManhattanDistanseAdmin)

    
