from django.shortcuts import render, redirect
from .models import User, Question, Report, Answer, Review, Delete
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    all_users = User.objects.all()
    if User.objects.filter(status='1').exists():
        flag = 1
    else:
        flag = 0
    context ={
        'all_users': all_users,
        'f': flag,
    }
    return render(request, 'homepage/index.html', context)


def regist(request):
    if request.method =='POST':
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        email = request.POST['email']
        phoneno = request.POST['phone']
        password = request.POST['password']
        gender = request.POST['gender']
        user = User()
        fname.istitle()
        mname.istitle()
        lname.istitle()
        if gender == 'Male':
            user.gender = 'Male'
        elif gender == 'Female':
            user.gender = 'Female'
        else:
            user.gender = 'Other'
        if User.objects.filter(email=email).exists():
            message = 'emailtaken'
            context = {
                'email': email,
                'mess': message,
            }
            return render(request, 'homepage/error.html', context)
        elif User.objects.filter(phoneno=phoneno).exists():
            message = 'phonenotaken'
            context = {
                'phoneno': phoneno,
                'mess': message,
            }
            return render(request, 'homepage/error.html', context)
        else:
            user.fname = fname
            user.mname = mname
            user.lname = lname
            user.email = email
            user.password = password
            user.phoneno = phoneno
            user.save()
            message = 'accountcreated'
            context = {
                'mess': message,
            }
            return render(request, 'homepage/error.html', context)
    else:
        return render(request, 'homepage/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            person = User.objects.filter(email=email).first()
            if person.password == password:
                context = {
                    'person': person,
                }
                all_users = User.objects.all()
                for loged in all_users:
                    loged.status = '0'
                    loged.save()
                person.status = '1'
                person.save()
                return redirect('/login/mainpage')
            else:
                message = 'wrongpassword'
                context = {
                    'email': email,
                    'password': password,
                    'mess': message,
                }
                return render(request, 'homepage/error.html', context)
        else:
            message='wrongemail'
            context = {
                'email': email,
                'password': password,
                'mess': message,
            }
            return render(request, 'homepage/error.html', context)
    else:
        return render(request, 'homepage/loginpage.html')


def forgot(request):
    if request.method == 'POST':
        mail = request.POST['email']
        person = User.objects.filter(email=mail).first()
        toemail = [mail]
        if User.objects.filter(email=mail).exists():
            subject = 'Your password for Online Q&A System'
            message = 'Password :'+ person.password
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject=subject, from_email=from_email, recipient_list=toemail, message=message, fail_silently=True)
            message = 'Password has been sent to your email'
            context = {
                'mess': message,
            }
            return render(request, 'homepage/error.html', context)
        else:
            message = 'wrongemail'
            context = {
                'mess': message,
            }
            return render(request, 'homepage/error.html', context)
    else:
        return render(request, 'homepage/forgot.html')


def mainpage(request):
    if request.method == 'POST':
        search = request.POST['search']
        finding = 1
    else:
        search = ''
        finding = 0
    all_users = User.objects.all()
    all_ques = Question.objects.all()
    flag = 0
    context = {
        'all_users': all_users,
        'all_ques': all_ques,
        'keyword': search,
        'flag': flag,
        'finding': finding,
    }
    logged = User.objects.filter(status='1').first()
    if logged.imgpicture == '':
        logged.imgpicture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnm2xMHtdgM-AQu_HFt_81GhkfnpyyjGIpJVbYcTPgQsAK9gjX'
        logged.save()
    return render(request, 'homepage/mainpage.html', context)


def profile(request):
    if request.method == 'POST':
        file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(file.name, file)
        url = fs.url(name)
        logged = User.objects.filter(status='1').first()
        logged.imgpicture = url
        logged.save()
    logged = User.objects.filter(status='1').first()
    if logged.imgpicture == '':
        logged.imgpicture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnm2xMHtdgM-AQu_HFt_81GhkfnpyyjGIpJVbYcTPgQsAK9gjX'
        logged.save()
    all_users = User.objects.all()
    context = {
        'all_users': all_users,
    }
    return render(request, 'homepage/profile.html', context)


def signout(request):
    if User.objects.filter(status='1').exists():
        person = User.objects.filter(status='1').first()
        person.status = '0'
        person.save()
        message = 'loggedout'
        context = {
            'mess': message,
        }
        return render(request, 'homepage/error.html', context)
    else:
        return redirect("/")


def women(request):
    if request.method == 'POST':
        wquestion = request.POST['wquestion']
        name = User.objects.filter(status='1').first()
        f = 0
        for w in wquestion:
            if w.isalnum():
                f+=1
        if f>=10:
            q2 = Question()
            q2.name = name.fname
            q2.question = wquestion
            q2.length = len(wquestion)
            q2.email = name.email
            q2.wquestion = '1'
            q2.topic = 'Women Question'
            q2.save()
            return redirect("/login/mainpage/")
        else:
            mess = 'wrongformat'
            context = {
                'mess': mess,
            }
            return render(request, 'homepage/error.html', context)
    else:
        return render(request, 'homepage/women.html')


def question(request):
    if request.method == 'POST':
        question = request.POST['question']
        topic = request.POST['topic']
        name = User.objects.filter(status='1').first()
        print(name.fname)
        f, k = 0, 0
        for w in topic:
            if w.isalnum():
                f += 1
        for l in question:
            if l.isalnum():
                k += 1
        if f >= 2 and k >= 10:
            print(f, k)
            q1 = Question()
            name.queasked = name.queasked + 1
            name.save()
            question.istitle()
            q1.topic = topic
            q1.question = question
            q1.length = len(question)
            q1.email = name.email
            q1.name = name.fname
            q1.save()
            return redirect("/login/mainpage/")
        else:
            mess = 'wrongformat'
            context = {
                'mess': mess,
            }
            return render(request, 'homepage/error.html', context)
    else:
        all_users = User.objects.all()
        context = {
            'all_users': all_users,
        }
        return render(request, 'homepage/question.html', context)


def report(request):
    if request.method == 'POST':
        helper = request.POST['helper']
        describ = request.POST['describ']
        user = User.objects.filter(status='1').first()
        funame = user.fname + ' ' + user.mname + ' ' + user.lname
        q1 = Report()
        q1.helper = helper,
        q1.email = user.email,
        q1.funame = funame,
        q1.describ = describ,
        q1.save()
        return redirect("/login/mainpage/")
    else:
        all_users = User.objects.all()
        context = {
            'all_users': all_users,
        }
        return render(request, 'homepage/report.html', context)


def about(request):
    return render(request, 'homepage/about.html')


def answer(request, question_id):
    qw = Question.objects.filter(id=question_id).first()
    logged = User.objects.filter(status='1').first()
    if request.method == 'POST':
        answe = request.POST.get('answer')
        ans = Answer()
        ans.idanswer = qw.id
        ans.name = logged.fname
        ans.answer = answe
        ans.email = logged.email
        ans.question = qw.question
        ans.asked = qw.name
        qw.totalans = qw.totalans + 1
        logged.ansgive = logged.ansgive + 1
        qw.save()
        ans.save()
        logged.save()
        return redirect('/login/mainpage/')
    else:
        context ={
            'qw': qw,
        }
        return render(request, 'homepage/answer.html', context)


def seeanswers(request, question_id):
    personasked = Question.objects.filter(id=question_id).first()
    allanswered = Answer.objects.all()
    logged = User.objects.filter(status='1').first()
    if Answer.objects.filter(idanswer=personasked.id).exists():
        exists = 'exists'
    else:
        exists = 'notexists'
    all_users = User.objects.all()
    context = {
        'personasked': personasked,
        'allanswered': allanswered,
        'exists': exists,
        'logged': logged,
        'all_users': all_users,
    }
    return render(request, 'homepage/seeanswers.html', context)


def upvotes(request, question_id, ans_id):
    answered = Answer.objects.filter(id=ans_id).first()
    logged = User.objects.filter(status='1').first()
    allreview = Review.objects.all()
    flag = 0
    if allreview:
        for w in allreview:
            if w.answerid == ans_id and w.rid == logged.id:
                Review.objects.filter(rid=logged.id, answerid=ans_id).delete()
                answered.upvotes = answered.upvotes - 1
                answered.save()
                return redirect('/login/mainpage/seeanswers/' + str(question_id) + '/')
            else:
                flag = 1
        if flag == 1:
            newrev = Review()
            newrev.rid = logged.id
            newrev.answerid = ans_id
            answered.upvotes = answered.upvotes + 1
            answered.save()
            newrev.save()
            return redirect('/login/mainpage/seeanswers/' + str(question_id) + '/')
    else:
        rev = Review()
        rev.rid = logged.id
        rev.answerid = ans_id
        answered.upvotes = answered.upvotes + 1
        answered.save()
        rev.save()
        return redirect('/login/mainpage/seeanswers/' + str(question_id) + '/')


def options(request):
    if request.method == 'POST':
        newfname = request.POST['fname']
        newmname = request.POST['mname']
        newlname = request.POST['lname']
        newpassword = request.POST['password']
        logged = User.objects.filter(status='1').first()
        logged.fname = newfname
        logged.mname = newmname
        logged.lname = newlname
        logged.password = newpassword
        logged.save()
        return redirect("/login/mainpage/profile/")
    else:
        return render(request, 'homepage/optavil.html')


def delete(request):
    if request.method == 'POST':
        reason = request.POST.get('reason')
        logged = User.objects.filter(status='1').first()
        email = logged.email
        all_questions = Question.objects.all()
        all_answers = Answer.objects.all()
        for ty in all_questions:
            if ty.email == email:
                deleteq = Question.objects.filter(email=email).delete()
        for tr in all_answers:
            if tr.email == email:
                deletea = Answer.objects.filter(email=email).delete()
        q1 = Delete()
        q1.reason = reason
        q1.email = email
        q1.save()
        User.objects.filter(status='1').delete()
        return redirect("/")
    else:
        return render(request, 'homepage/delete.html')


def your(request, your):
    if your == 1881:
        finding = 2
    elif your == 8118:
        finding = 3
    all_users = User.objects.all()
    all_ques = Question.objects.all()
    flag = 0
    logged = User.objects.filter(status='1').first()
    if logged.imgpicture == '':
        logged.imgpicture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnm2xMHtdgM-AQu_HFt_81GhkfnpyyjGIpJVbYcTPgQsAK9gjX'
        logged.save()
    keyword = ''
    context = {
        'all_users': all_users,
        'all_ques': all_ques,
        'flag': flag,
        'finding': finding,
        'logged': logged,
        'keyword': keyword
    }
    print(logged.email)
    return render(request, 'homepage/mainpage.html', context)