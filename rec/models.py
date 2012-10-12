# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class OurUser(models.Model):
    name = models.CharField(max_length=140)

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return '/users/%s' %self.id

class Movie(models.Model):
    call = models.CharField(max_length=140)

    def __unicode__(self):
        return '%s' % self.call

    def get_absolute_url(self):
        return '/films/%s' %self.id

class ScoreRank(models.Model):
    user = models.ForeignKey('OurUser')
    rank = models.IntegerField()
    film = models.ForeignKey('Movie')

    def __unicode__(self):
        return u'Пользователь %s оценил %s на %s' % (self.user,self.film, self.rank )

class BitRank(models.Model):
    STATUS_CHOICES = (
        (1,'1'),
        (0,'0'),
        )
    user = models.ForeignKey('OurUser')
    rank = models.IntegerField(choices=STATUS_CHOICES, default='0')
    film = models.ForeignKey('Movie')
    
    def __unicode__(self):
        if self.rank == 1:
            return u'%s => %s' % (self.user, self.film)#u'Пользователь %s интересовался %s' %(self.user, self.film)
        else:
            return u'%s -- %s' % (self.user, self.film)
        
class TriRank(models.Model):
    STATUS_CHOICES = (
        (1,' 1'),
        (0,' 0'),
        (-1,'-1'),
        )
    user = models.ForeignKey('OurUser')
    rank = models.IntegerField(choices=STATUS_CHOICES, default='0')
    film = models.ForeignKey('Movie')

    def __unicode__(self):
        if self.rank == 1:
            return u'Пользователю %s понравился фильм %s'  %(self.user, self.film)
        elif self.rank == -1:
            return u'Пользователю %s не понравился фильм %s'  %(self.user, self.film)
        else:
            return u'Пользователь %s не оценил фильм %s'  %(self.user, self.film)

class Range10EuclidDistance(models.Model):
    user = models.ForeignKey('OurUser', null=False,related_name='first_user_eu')
    user2 = models.ForeignKey('OurUser',null=False,related_name='second_user_eu')
    range10 = models.DecimalField( max_digits=12, decimal_places=10)

class Range10CorrelationOfPearson(models.Model):
    user = models.ForeignKey('OurUser',null=False,related_name='first_user_pear')
    user2 = models.ForeignKey('OurUser',null=False,related_name='second_user_pear')
    range10 = models.DecimalField( max_digits=12, decimal_places=10)

class Range10IndexOfJaccard(models.Model):
    user = models.ForeignKey('OurUser',null=False,related_name='first_user_jac')
    user2 = models.ForeignKey('OurUser',null=False,related_name='second_user_jac')
    range10 = models.DecimalField( max_digits=12, decimal_places=10)

class Range10ManhattanDistanse(models.Model):
    user = models.ForeignKey('OurUser',null=False,related_name='first_user_manh')
    user2 = models.ForeignKey('OurUser',null=False,related_name='second_user_manh')
    range10 = models.DecimalField( max_digits=12, decimal_places=10)
    
