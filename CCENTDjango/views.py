from wsgiref.util import request_uri
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render,redirect
from carrusel.models import HomeSlide
from document.models import Document
def inicio(request):
    return render(request,"nuevapagina.html",{"var1":HomeSlide.objects.all()})
    
def quienes_somos(request):
    return render(request,"quienes_somos.html")

#cursos
def cursos(request):
    return render(request,"cursos.html")

def av(request):
    return render(request,"av.html")

def autom(request):
    return render(request,"autom.html")

def EAD(request):
    return render(request,"EAD.html")

def pcylap(request):
    return render(request,"pcylap.html")

def robotica(request):
    return render(request,"robotica.html")

#fin de cursos 
def materiales(request):
    return render(request,"herramientas.html")

def servicios(request):
    return render(request,"servicios.html")

def faq(request):
    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.save()
            return redirect('/?docid=%i' % docid)
        else:
            document = Document.objects.create(title=title, content=content)

            return redirect('/?docid=%i' % document.id)

    if docid > 0: 
        document = Document.objects.get(pk=docid)
    else:
        document = Document.objects.first()

    context = {
        'docid': docid,
        'documents': documents,
        'document': document
    }

    return render(request, 'faq.html', context)

    
