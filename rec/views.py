# -*- coding: utf-8 -*-
# Create your views here.
from models import *
#from django.http import HttpResponse
from django.shortcuts import *
from django.template import RequestContext
from metric import *
import random

def create_rank_view(request):
    users = OurUser.objects.all()
    movies = [i for i in Movie.objects.all()]
    for user in users:
        random.shuffle(movies)
        for movie in movies[:len(movies)/3]:
            r = ScoreRank(user=user, rank=random.randint(1,10), film=movie)
            r.save()
            r1 = BitRank(user=user, rank=random.randint(0,1), film=movie)
            r1.save()
            r2 = TriRank(user=user, rank=random.randint(-1,1), film=movie)
            r2.save()      
    return 'Потрачено'

def get_movies(user, metric=''):
    MODELS = {'r10Euclid': Range10EuclidDistance ,
              'r10Pearson': Range10CorrelationOfPearson,
              'r10Jaccar': Range10IndexOfJaccard,
              'r10Manhattan': Range10ManhattanDistanse}
    model = MODELS[metric]
    list_for_our_user = {i.film for i in ScoreRank.objects.filter(user=user)}
    list_of_score = [ i for i   in model.objects.filter(user=user).order_by('range10') ]
    rec_list = []
    for l in list_of_score:
         if len(rec_list)==10:break
         list_for_other_user = {i.film for i in ScoreRank.objects.filter(user=l.user)}
         target_list = list_for_our_user & list_for_other_user
         for target in target_list:
             rec_list.append(target)
             if len(rec_list) ==10: break
    return rec_list


def recomendation(uid):
    metrics = ['r10Euclid','r10Pearson','r10Jaccar','r10Manhattan']
    xmetrics = map(get_movies,[uid for i in range(len(metrics)) ], metrics)
    rec = dict(zip(metrics,xmetrics))
    return rec

def user_detail(request, uid):
    FILMS_TABLE = ['film','range10','range3','range2']
    user = get_object_or_404(OurUser, id=uid)
    film_list = ScoreRank.objects.filter(user=user)#.name.encode('cp1251')) #if q.user==user.name] #Оцениваем по фильмам, которые оценил пользователь
##    film_context = []
##    for film in film_list:
##        values = [film.call,
##                  get_object_or_404(ScoreRank, user=user, film=film),
##                  get_object_or_404(TriRank,user=user, film=film),
##                  get_object_or_404(BitRank,user=user, film=film)
##                  ]
##        film_context += [dict(zip(FILMS_TABLE,values))]
##    #film_context=[{'film':'Izya', 'range10':8,'range3':0,'range2':1}]
    s = user.name#film_list #context)
    return render_to_response('user.html',
                              {#'films': film_context,
                               's':s,
                               'user': user,
                               'recomendation': recomendation(uid)},
                              context_instance=RequestContext(request)
                              )

