#from django.core.mail import send_mail, mail_admins, EmailMessage, BadHeaderError
from django.shortcuts import render
from .tasks import notify_customers
#from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    notify_customers.delay('Hello')
    '''try:
        message = BaseEmailMessage(
            template_name= 'emails/hello_mail.html',
            context= {'name': 'Ihor'}
        )
        message.send(['john@mosh.com'])
        #message = EmailMessage('subject', 'message', 'sporteqlviv@gmail.com', ['dodik@gmail.com'])
        #message.attach_file('playground/static/images/dog.jpg')
        #message.send()
        #mail_admins('subject', 'message',html_message='message')
        #send_mail('subject', 'message', 'sporteqlviv@gmail.com', ['dodik@gmail.com'])
    except BadHeaderError:
        pass'''    
    return render(request, 'hello.html', {'name': 'Mosh'})
