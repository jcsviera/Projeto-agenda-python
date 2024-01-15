from django.shortcuts import get_object_or_404,render,redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator



from django.apps import apps

def index(request):
   #contacts = apps.get_model('contact','Contact')
   contacts = Contact.objects\
              .filter(show = True)\
              .order_by('-id')
   
   paginator = Paginator(contacts,10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   
   context = {
      'page_obj': page_obj,
   }
     
   return render(
         request,
        'contact/index.html',
         context         
     )


def search(request):
   #contacts = apps.get_model('contact','Contact')
   search_value = request.GET.get('q','').strip()

   if search_value == '': 
      return redirect('contact:index')

   contacts = Contact.objects\
              .filter(show = True)\
              .filter(Q(first_name__icontains = search_value) |
                      Q(last_name__icontains = search_value) |
                      Q(phone__icontains = search_value) |
                      Q(email__icontains = search_value) 

                      )\
              .order_by('-id')
   
   paginator = Paginator(contacts,10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   
   context = {
      'page_obj': page_obj,
      'search_value': search_value,
   }
     
   return render(
         request,
        'contact/index.html',
         context         
     )


def contact(request,contact_id):
   #contacts = apps.get_model('contact','Contact')
   #single_contact = Contact.objects.filter(pk = contact_id).first()
   
   single_contact = get_object_or_404(Contact,pk = contact_id,show = True)
   context = {
      'contact': single_contact,
   }
     
   return render(
         request,
        'contact/contact.html',
         context         
     )