from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has mad inquiry alread
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id
            )
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)

        contact = Contact(
            listing=listing, listing_id=listing_id, name=name,
            email=email, phone=phone, message=message,
            user_id=user_id
        )

        contact.save()

        # Send email
        # send_mail(
            # 'Property Listing Inquiry',
            # 'There h[as been an inquiry for ' + listing + '. Sign into the admin panel for more infor',
            # settings.EMAIL_HOST_USER,
            # [realtor_email, 'c.chaiwat.store@gmail.com'],
            # fail_silently=False
        # )
#
        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/' + listing_id)
