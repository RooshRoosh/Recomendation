# -*- coding: utf-8 -*-
def change_or_neW_score(user,film,score):
    """
    1) Извлекаем пользователей, которые тоже оценили этот фильм
    2) Для каждого из этих пользователей пересчитываем "близость"
    """        
    rel_users = [ record.user for record in ScoreRank.objects.filter(film=film)]
    our_person = [ zip(record.film,record.score) for record in SсoreRank.objects.filter(user.name=user)]
    our_person = {user:dict(our_person)}
    for rel_user in rel_users:
        second_person = [ zip(record.film,record.score) for record in ScoreRank.objects.filter(rel_user.name=user)]
        second_person = {rel_user:dict(second_person)}
        #########################################################
        rank_fucn(our_person.update(second_person),user,rel_user)
        #########################################################
        
        
