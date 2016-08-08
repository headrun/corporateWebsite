from django.shortcuts import render
from django.http import HttpResponse
from django.template import  loader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

# Create your views here.

def portfolio3(request): 
    template = loader.get_template('portfolio3.html')
    context = {}
    return HttpResponse(template.render(context, request))
    #return render(request, "landingpage.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def error404(request): 
    template = loader.get_template('404.html')
    context = {}
    return HttpResponse(template.render(context, request))

def profile(request): 
    with open('/var/www/ARAVIND/headrun/headrun_pages/templates/Headrun_profile.pdf', 'r') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=headrun_profile.pdf'
            return response

def blackbuck(request): 
    template = loader.get_template('blackbuck.html')
    context = {}
    return HttpResponse(template.render(context, request))


def miebach(request): 
    template = loader.get_template('miebach.html')
    context = {}
    return HttpResponse(template.render(context, request))

def notemonk(request): 
    template = loader.get_template('notemonk.html')
    context = {}
    return HttpResponse(template.render(context, request))

def cloudlibs(request): 
    template = loader.get_template('cloudlibs.html')
    context = {}
    return HttpResponse(template.render(context, request))

def tlg(request): 
    template = loader.get_template('tlg.html')
    context = {}
    return HttpResponse(template.render(context, request))

def floretz(request): 
    template = loader.get_template('floretz.html')
    context = {}
    return HttpResponse(template.render(context, request))

def incog(request): 
    template = loader.get_template('incog.html')
    context = {}
    return HttpResponse(template.render(context, request))

def juicer(request): 
    template = loader.get_template('juicer.html')
    context = {}
    return HttpResponse(template.render(context, request))

def paymentgateway(request): 
    template = loader.get_template('paymentgateway.html')
    context = {}
    return HttpResponse(template.render(context, request))

def buzzinga(request): 
    template = loader.get_template('buzzinga.html')
    context = {}
    return HttpResponse(template.render(context, request))
    #return render(request, "landingpage.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def index(request): 
    template = loader.get_template('landingpage.html')
    context = {}
    return HttpResponse(template.render(context, request))
    #return render(request, "landingpage.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def contact(request): 
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))
    #return render(request, "contact.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def contact_(request): 
    #template = loader.get_template('contact.html')
    name = request.GET.get('name', '')
    mail = request.GET.get('email', '')
    content = request.GET.get('comment', '')
    message = "Hi,\n\nName : \t %s\nEmail : \t %s\nMessage : \t %s\n" % (name, mail, content)
    msgRoot = MIMEText(message)
    msgRoot['subject'] = 'New Contact Information'
    msgRoot['From'] = 'Headrun'
    msgRoot['To'] = ",".join(['contact@headrun.com'])

    #TO = ['aravind@headrun.com']
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login('head201509@gmail.com', 'head201509$')
    #s.sendmail('head201509@gmail.com' , TO[0], msgRoot.as_string())
    s.sendmail('head201509@gmail.com' , TO[0], msgRoot.as_string())
    s.quit()
    x = str(1)
    #x = str(mailsend.main_mail(name, mail, content))
    return HttpResponse(x)

def about(request): 
    template = loader.get_template('about_bkp_march.html')
    context = {}
    return HttpResponse(template.render(context, request))
    #return render(request, "landingpage.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")


def testimonials(request): 
    template = loader.get_template('testimonials.html')
    context = {}
    return HttpResponse(template.render(context, request))
    #return render(request, "testimonials.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def timeline(request): 
    template = loader.get_template('timeline.html')
    context = {}
    return HttpResponse(template.render(context, request))
    #return render(request, "timeline.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def services(request): 
    template = loader.get_template('services.html')
    context = {}
    return HttpResponse(template.render(context, request))
    #return render(request, "services.html", context)
    #return HttpResponse("Hello, world. You're at the polls index.")
