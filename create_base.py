# -*- coding: cp1251 -*-
import sqlite3
import random
from rec.metric import *

def create_film():
    films = open('movies.txt','r')
    connect = sqlite3.connect('db.db')
    connect.text_factory = sqlite3.OptimizedUnicode
    cur = connect.cursor()
    for film in films:
        film = str(film)
        connect.execute('''INSERT INTO rec_movie (id, call) VALUES(NULL, ?)''', (film,))
        connect.commit()
    connect.commit()
    connect.close()

def create_users():
    names = open('names.txt','r')
    connect = sqlite3.connect('db.db')
    connect.text_factory = sqlite3.OptimizedUnicode
    cur = connect.cursor()
    for name in names:
        name = str(name)
        connect.execute('''INSERT INTO rec_ouruser (id, name) VALUES(NULL, ?)''', (name,))
        connect.commit()
    connect.commit()
    connect.close()

def create_content():
    names = open('names.txt','r')
    films = open('movies.txt','r')
    connect = sqlite3.connect('db.db')
    connect.text_factory = str.encode('utf-8')#sqlite3.OptimizedUnicode
    cur = connect.cursor()
    for name in names:
        name = str(name)
        connect.execute('''INSERT INTO rec_ouruser (id, name) VALUES(NULL, ?)''', (name,))
        connect.commit()
    for film in films:
        film = str(film)
        connect.execute('''INSERT INTO rec_movie (id, call) VALUES(NULL, ?)''', (film,))
        connect.commit()    
    connect.commit()
    connect.close()
    names.close()
    films.close()

def create_ranks():
    connect = sqlite3.connect('db.db')
    connect.text_factory = str#.encode('utf-8')#sqlite3.OptimizedUnicode
    cur = connect.cursor()
    print type(connect)
    users = [q[1] for q in connect.execute('''SELECT * FROM rec_ouruser''',)]
    movies = [q[1] for q in connect.execute('''SELECT * FROM rec_movie''',)]
    l= len(users)
    i=0
    for user in users:
        i+=1
        random.shuffle(movies)
        for movie in movies[:len(movies)/3]:
            connect.execute('''INSERT INTO rec_scorerank (id, user_id, rank, film_id) VALUES(NULL, ?,?,?)''',
                            (user,random.randint(1,10),movie,))
            connect.commit()
            connect.execute('''INSERT INTO rec_bitrank (id, user_id, rank, film_id) VALUES(NULL, ?,?,?)''',
                            (user,random.randint(0,1),movie,))
            connect.commit()
            connect.execute('''INSERT INTO rec_trirank (id, user_id, rank, film_id) VALUES(NULL, ?,?,?)''',
                            (user,random.randint(-1,1),movie,))
            connect.commit()
        print i,'/',l
    connect.commit()
    connect.close()
    


def delete_table(table):
    connect = sqlite3.connect('db.db')
    connect.text_factory = sqlite3.OptimizedUnicode
    cur = connect.cursor()
    q = '''DROP TABLE %s''' %table
    connect.execute(q)
    connect.commit()
    connect.close()


    
def create_10_rank():
    def create_dict(user):
        query = connect.execute('''SELECT * FROM rec_scorerank WHERE user_id=? ''', (user,))
        return dict([(i[3],i[2]) for i in query])
    connect = sqlite3.connect('db.db')
    connect.text_factory = sqlite3.OptimizedUnicode
    cur = connect.cursor()
    stack=[]
    i=0
    users = {u[1] for u in connect.execute('''SELECT * FROM rec_scorerank''')}
    for u1 in users:
        user1 = create_dict(u1)
        stack+=[u1]
        for u2 in users:
             if u2 in stack: continue
             user2 = create_dict(u2)
             rank = Manhattan_distanse({u1:user1,u2:user2},u1,u2) #correlation_of_Pearson  Euclid_distance  index_of_Jaccard
             connect.execute('''INSERT INTO rec_range10manhattandistanse (id, user_id, user2_id,range10) VALUES(NULL, ?, ?,?)''', (u1,u2,rank)) #rec_range10eucliddistance indexofjaccard
             connect.execute('''INSERT INTO rec_range10manhattandistanse (id, user_id, user2_id,range10) VALUES(NULL, ?, ?,?)''', (u2,u1,rank))
             i+=1
    connect.commit()
    connect.close()

def create_bin_rank():
    pass

def create_tri_rank():
    pass
