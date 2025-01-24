from django.shortcuts import render
records={}
# Create your views here.
def home(req):
    return render(req,"app1/index.html")
def data(req):
    uname=req.GET['name']
    rno=req.GET['roll']
    py=int(req.GET['ph'])
    jv=int(req.GET['ja'])
    jas=int(req.GET['js'])
    total=py+jv+jas
    records[uname]=[{"rno":rno,'score':[ py,jv,jas],'total':total}]
    response=render(req,'app1/index.html',context={'msg':'Student Details Added'})
    return response
def display(req):
    print(records)
    res=render(req,"app1/display.html",context={'records':records})
    return res
def view(req):
    return render(req,"app1/details.html")
