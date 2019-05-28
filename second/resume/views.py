from django.shortcuts import render, redirect



from . import models

# Create your views here.
def index(request):

    print(models.Resuts())
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    if request.session.keys():
        return render(request, 'index.html', {'condition': True})
    else:
        return render(request, 'index.html', {'condition': False})


def resume(request):
    for key, value in request.session.items():
        print("key in resume",key)
        i=value
        print(i)

    try:
        resumeheader=models.header(i)
    except:
        return render(request, 'index.html', {'condition': False})

    educate=models.ret_education(i)
    jobs=models.ret_job(i)
    intern=models.ret_intern(i)
    train=models.ret_train(i)
    project=models.ret_pro(i)
    skill=models.ret_skill(i)
    add=models.ret_add(i)
    print(educate)
    print(jobs)
    print(intern)
    print(train)
    print(project)
    print(skill)
    print(add)

    if request.session.keys():
        return render(request, 'resume.html', {'condition': True,'resumeheader':resumeheader,'educate':educate,'jobs':jobs,'intern':intern,'train':train,'project':project,'skill':skill,'add':add})
    else:
        return render(request, 'index.html', {'condition': False})

def signup(request):
    email=request.POST['email']
    password=request.POST['password']
    firstname=request.POST['firstName']
    lastname=request.POST['lastName']
    phone=request.POST['phone']
    signupid=models.signup(email,password,firstname,lastname,phone)
    print(signupid)
    request.session['id']=signupid
    return redirect("/resume")

def login(request):
    email=request.POST['lemail']
    password=request.POST['lpassword']
    models.login(email,password)
    if True:
        if models.session() < 0:
            return render(request, 'index.html', {'condition': False})
        else:
            request.session['id'] = models.session()
            print(models.session())
            return redirect("/resume")
    else:
        return render(request, 'index.html', {'condition': False})

def logout(request):
    try:
        del request.session['id']
    except:
        print("none")
    return redirect("/index")

def education(request):
    for key, value in request.session.items():
        print("key in resume",key)
        i=value
        print(i)
    try:
        board = request.POST['board']
    except:
        board=None
    try:
        stream=request.POST['stream']
    except:
        stream=None
    try:
        degree=request.POST['degree']
    except:
        degree=None
    try:
        sdate=request.POST['sdate']
    except:
        sdate=None


    models.insert_education(i,sdate,request.POST['edate'],board,request.POST['scale'],request.POST['perf'],request.POST['school'],stream,degree)
    print("inserted edu")
    return redirect("/resume")


def jobs(request):
    for key, value in request.session.items():
        i=value
        print("job",i)
    profile=request.POST['profile']
    organization=request.POST['organization']
    location=request.POST['location']
    sdate=request.POST['sdate']
    edate=request.POST['edate']
    description=request.POST['description']
    models.insert_job(i,profile, organization,location,sdate,edate, description)
    print("inserted job")
    return redirect("/resume")

def deletejob(request):
    for key, value in request.session.items():
        i=value
    models.deletejob(i)
    print("deleted job")
    return redirect("/resume")

def deleteintern(request):
    for key, value in request.session.items():
        i=value
    models.deleteintern(i)
    print("deleted intern")
    return redirect("/resume")

def intern(request):
    for key, value in request.session.items():
        i=value
        print("job",i)
    profile=request.POST['profile']
    organization=request.POST['organization']
    location=request.POST['location']
    sdate=request.POST['sdate']
    edate=request.POST['edate']
    description=request.POST['description']
    models.insert_intern(i,profile, organization,location,sdate,edate, description)
    print("inserted internship")
    return redirect("/resume")

def deleteedu(request):
    for key, value in request.session.items():
        i = value
    models.delete_edu(i)
    print("deleted job")
    return redirect("/resume")

def training(request):
    for key, value in request.session.items():
        i=value
        print("train",i)
    program=request.POST['program']
    organization=request.POST['organization']
    sdate=request.POST['sdate']
    edate=request.POST['edate']
    description=request.POST['description']
    models.insert_train(i,program, organization,sdate,edate, description)
    print("inserted training")
    return redirect("/resume")

def deletetrain(request):
    for key, value in request.session.items():
        i=value
    models.deletetrain(i)
    print("deleted train")
    return redirect("/resume")

def project(request):
    for key, value in request.session.items():
        i=value
        print("train",i)
    pname=request.POST['pname']
    sdate=request.POST['sdate']
    edate=request.POST['edate']
    link = request.POST['link']
    description=request.POST['description']
    models.insert_pro(i,pname,sdate,edate,link,description)
    print("inserted project")
    return redirect("/resume")

def deletepro(request):
    for key, value in request.session.items():
        i=value
    models.deletepro(i)
    print("deleted project")
    return redirect("/resume")

def skill(request):
    for key, value in request.session.items():
        i=value
        print("skill",i)
    skill=request.POST['skill']
    models.insert_skill(i,skill)
    print("inserted skill")
    return redirect("/resume")

def deleteskill(request):
    for key, value in request.session.items():
        i=value
    models.deleteskill(i)
    print("deleted project")
    return redirect("/resume")

def additional(request):
    for key, value in request.session.items():
        i=value
        print("skill",i)
    des=request.POST['description']
    models.insert_add(i,des)
    print("inserted additional")
    return redirect("/resume")

def deleteadd(request):
    for key, value in request.session.items():
        i=value
    models.deleteadd(i)
    print("deleted additional")
    return redirect("/resume")




















