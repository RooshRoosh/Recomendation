# -*- coding: utf-8 -*-
from models import *
from django.http import HttpResponse

import random

def create_all(request):
    
    users = OurUser.objects.all()
    users = [i for i in users]
    random.shuffle(users)
    users = users[0:(len(users)/3)]
    
    films = Movie.objects.all()
    films = [i for i in films]
    random.shuffle(films)
    films = films[0:(len(films)/3)]
    
    for user in users:
        for film in films:
            score = random.randint(2,10)
            rank = ScoreRank(user=user, rank=score,film=film)
            score = random.randint(0,1)
            rank2 = BitRank(user=user, rank=score,film=film)
            score = random.randint(-1,1)
            rank3 = TriRank(user=user, rank=score,film=film)
            for i in [rank, rank2, rank3]: i.save()
    return HttpResponse(u'Записи проранжированны по всем метрикам')

def create_10_rank(request):
    
    users = OurUser.objects.all()
    users.random.shuffle()
    users = users[0:(len(users)/3)]
    
    films = Movie.objects.all()
    films.random.shuffle()
    films = films[0:(len(films)/3)]
    
    for user in users:
        for film in films:
            rank = ScoreRank(user=user.user, rank=random.randint(2,10),film=film.call)
            rank.save()
    return HttpResponse(u'Записи проранжированны по 10 бальной шкале')
        
def create_bin_rank(request):
    
    users = OurUser.objects.all()
    users.random.shuffle()
    users = users[0:(len(users)/3)]
    
    films = Movie.objects.all()
    films.random.shuffle()
    films = films[0:(len(films)/3)]
    
    for user in users:
        for film in films:
            rank = BitRank(user=user.user, rank=random.randint(0,1),film=film.call)
            rank.save()
    return HttpResponse(u'Записи проранжированны по Критерию "Понравилось"/"Не понравилось"')
        

def create_tri_rank(request):
    
    users = OurUser.objects.all()
    users.random.shuffle()
    users = users[0:(len(users)/3)]
    
    films = Movie.objects.all()
    films.random.shuffle()
    films = films[0:(len(films)/3)]
    
    for user in users:
        for film in films:
            rank = TriRank(user=user.user, rank=random.randint(-1,1),film=film.call)
            rank.save()
    return HttpResponse(u'Записи проранжированны по Критерию "Понравилось"/"Не смотрел"/"Не понравилось"')   
