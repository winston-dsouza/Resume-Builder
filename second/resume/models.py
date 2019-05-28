from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import render, redirect

import sqlite3



def Connect():
    Myuser = sqlite3.connect('db1.sqlite3')
    return Myuser


def Resuts():
    query = "select * from user"
    Cursor = Connect().cursor()
    Cursor.execute(query)
    result = Cursor.fetchall()
    Connect().close()
    return  result
# Create your models here.

def signup(email,password,firstname,lastname,phone):
    Myuser = sqlite3.connect('db1.sqlite3')
    querys = "insert into user (emailId,password,first_name,last_name,phone_no) values ('"+email+"','"+password+"','"+firstname+"','"+lastname+"','"+phone+"');"
    Cursor = Myuser.cursor()
    Cursor.execute(querys)
    print(Cursor.lastrowid)
    s=Cursor.lastrowid
    Myuser.commit()
    Myuser.close()
    print("signup created")
    return s

def login(email,password):
    Myuser = sqlite3.connect('db1.sqlite3')
    query="select id from user where emailId='"+email+"'and password='"+password+"';"
    Cursor = Myuser.cursor()
    Cursor.execute(query)
    result = Cursor.fetchall()
    if result:
        for i in result:
            print(i[0])
            global g
            g=i[0]
            return i[0]
    else:
        return

def session():
    try:
        return g
    except:
        return -1

def logout():
    Myuser = sqlite3.connect('db1.sqlite3')
    querys = "delete from django_session"
    Cursor = Myuser.cursor()
    Cursor.execute(querys)
    Myuser.commit()
    Myuser.close()
    print("deleted")

def header(userid):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    Cursor.execute("select first_name,last_name,emailId,phone_no from user where id=?",(userid,))
    result = Cursor.fetchall()[0]
    Myuser.close()
    print(result)
    return result

def insert_education(edu_id,startdate=None,yearofcomplete=None,board=None,scale=None,performance=None,school=None,stream=None,degree=None):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("insert into education (edu_id,startdate,yearofcomplete,board,scale,performance,school,stream,degree) values (?,?,?,?,?,?,?,?,?)",(edu_id,startdate,yearofcomplete,board,scale,performance,school,stream,degree))
    except:
        print('error in inserting education')
    Myuser.commit()
    Myuser.close()
    return

def ret_education(userid):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    Cursor.execute("select degree,stream,strftime('%Y',yearofcomplete) ,school,scale,performance,board from education where edu_id=? ORDER BY  yearofcomplete DESC", (userid,))
    result = Cursor.fetchall()
    Myuser.close()
    print(result)
    return result




def delete_edu(id):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("DELETE FROM education WHERE pri_id=(SELECT MAX(pri_id) FROM education) and edu_id=?", (id,))
    except:
        print('error in deleting education')
    Myuser.commit()
    Myuser.close()
    return

def deletejob(id):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("DELETE FROM jobs WHERE pri_id = (SELECT MAX(pri_id) FROM jobs ) and job_id=?",(id,))
    except:
        print('error in deleting job')
    Myuser.commit()
    Myuser.close()
    return


def insert_job(job_id,profile, organization,location,sdate,edate, description):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    Cursor.execute("insert into jobs (job_id,profile,organization,location,sdate,edate,description) values (?,?,?,?,?,?,?)",(job_id,profile, organization,location,sdate,edate, description))

    Myuser.commit()
    Myuser.close()
    return

def ret_job(userid):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    Cursor.execute("select profile,organization,location,sdate,edate,description from jobs where job_id=? ", (userid,))
    result = Cursor.fetchall()
    Myuser.close()
    print(result)
    return result

def insert_intern(intern_id,profile, organization,location,sdate,edate, description):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    Cursor.execute("insert into internship (intern_id,profile,organization,location,sdate,edate,description) values (?,?,?,?,?,?,?)",(intern_id,profile, organization,location,sdate,edate, description))

    Myuser.commit()
    Myuser.close()
    return

def ret_intern(userid):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    Cursor.execute("select profile,organization,location,sdate,edate,description from internship where intern_id=? ", (userid,))
    result = Cursor.fetchall()
    Myuser.close()
    print(result)
    return result

def deleteintern(id):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("DELETE FROM internship WHERE pri_id = (SELECT MAX(pri_id) FROM internship ) and intern_id=?",(id,))
    except:
        print('error in deleting intern')
    Myuser.commit()
    Myuser.close()
    return

def insert_train(train_id,program, organization,sdate,edate, description):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("insert into training (train_id,program,organization,sdate,edate,description) values (?,?,?,?,?,?)",(train_id,program, organization,sdate,edate, description))
    except:
        print("insertion train failed")
    Myuser.commit()
    Myuser.close()
    return

def ret_train(userid):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    Cursor.execute("select program,organization,sdate,edate,description from training where train_id=? ", (userid,))
    result = Cursor.fetchall()
    Myuser.close()
    print(result)
    return result

def deletetrain(id):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("DELETE FROM training WHERE pri_id = (SELECT MAX(pri_id) FROM training ) and train_id=?",(id,))
    except:
        print('error in deleting ')
    Myuser.commit()
    Myuser.close()
    return

def insert_pro(pro_id,pname,sdate,edate,link,description):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("insert into project (pro_id,pname,sdate,edate,link,description) values (?,?,?,?,?,?)",(pro_id,pname,sdate,edate,link,description))
    except:
        print("insertion project failed")
    Myuser.commit()
    Myuser.close()
    return

def ret_pro(userid):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    Cursor.execute("select pname,sdate,edate,link,description from project where pro_id=? ", (userid,))
    result = Cursor.fetchall()
    Myuser.close()
    print(result)
    return result

def deletepro(id):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("DELETE FROM project WHERE pri_id = (SELECT MAX(pri_id) FROM project ) and pro_id=?",(id,))
    except:
        print('error in deleting ')
    Myuser.commit()
    Myuser.close()
    return

def insert_skill(skill_id,skill):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("insert into skills (skill_id,skill) values (?,?)",(skill_id,skill))
    except:
        print("insertion skill failed")
    Myuser.commit()
    Myuser.close()
    return

def ret_skill(userid):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    Cursor.execute("select skill from skills where skill_id=? ", (userid,))
    result = Cursor.fetchall()
    Myuser.close()
    print(result)
    return result

def deleteskill(id):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("DELETE FROM skills WHERE pri_id = (SELECT MAX(pri_id) FROM skills ) and skill_id=?",(id,))
    except:
        print('error in deleting ')
    Myuser.commit()
    Myuser.close()
    return

def insert_add(add_id,des):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("insert into additional (add_id,description) values (?,?)",(add_id,des))
    except:
        print("insertion additional failed")
    Myuser.commit()
    Myuser.close()
    return
def ret_add(userid):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    Cursor.execute("select description from additional where add_id=? ", (userid,))
    result = Cursor.fetchall()
    Myuser.close()
    print(result)
    return result

def deleteadd(id):
    Myuser = sqlite3.connect('db1.sqlite3')
    Cursor = Myuser.cursor()
    try:
        Cursor.execute("DELETE FROM additional WHERE pri_id = (SELECT MAX(pri_id) FROM additional ) and add_id=?",(id,))
    except:
        print('error in deleting ')
    Myuser.commit()
    Myuser.close()
    return
























