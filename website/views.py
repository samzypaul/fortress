from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



# Home View
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

#the service page view
def services(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render({}, request))

#the experience view
def experience(request):
    template = loader.get_template('experience.html')

    return HttpResponse(template.render({}, request))

#about page view
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))

#contact us page view
def quotation(request):
    template = loader.get_template('quotation.html')
    return HttpResponse(template.render({}, request))

#
# from django.shortcuts import render
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib import messages
#
#
# def get_quote(request):
#     """
#     Handles the quotation form submission and sends an email to the site owner.
#     """
#     if request.method == 'POST':
#         # 1. Extract data from the POST request
#         contact_name = request.POST.get('contactName')
#         institution = request.POST.get('institution')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         service_type = request.POST.get('serviceType')
#         equipment_details = request.POST.get('equipmentDetails', 'N/A')
#         description = request.POST.get('description', 'No additional details')
#
#         # 2. Construct the Email Message
#         subject = f"New Quotation Request: {service_type} - {institution}"
#
#         message_body = f"""
#         NEW QUOTATION REQUEST RECEIVED
#
#         CONTACT INFORMATION:
#         --------------------
#         Name: {contact_name}
#         Institution: {institution}
#         Email: {email}
#         Phone: {phone}
#
#         SERVICE REQUEST DETAILS:
#         -----------------------
#         Service Type: {service_type}
#         Equipment: {equipment_details}
#
#         DESCRIPTION/FAULT INFO:
#         -----------------------
#         {description}
#
#         --
#         This email was sent from the Fortress Medical Engineers Website.
#         """
#
#         try:
#             # 3. Send the Email
#             send_mail(
#                 subject=subject,
#                 message=message_body,
#                 from_email=settings.DEFAULT_FROM_EMAIL,  # Usually set in settings.py
#                 recipient_list=['samzypaul@gmail.com.com'],  # Your specific target email
#                 fail_silently=False,
#             )
#
#             # Return a success state (you can use Django messages or a specific success flag)
#             return render(request, 'quotation.html', {
#                 'success_name': contact_name,
#                 'submitted': True
#             })
#
#         except Exception as e:
#             # Handle potential SMTP errors (e.g., network issues)
#             messages.error(request, "There was an error sending your request. Please try again later.")
#
#     return render(request, 'quotation.html')


from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def get_quote(request):
    """
    Handles the quotation form submission and sends an email to the site owner.
    """
    if request.method == 'POST':
        # 1. Extract data from the POST request
        # The .get() keys must match the 'name' attributes in the HTML form
        contact_name = request.POST.get('contactName')
        institution = request.POST.get('institution')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service_type = request.POST.get('serviceType')
        equipment_details = request.POST.get('equipmentDetails', 'N/A')
        description = request.POST.get('description', 'No additional details')

        # 2. Construct the Email Message
        subject = f"New Quotation Request: {service_type} - {institution}"

        message_body = f"""
        NEW QUOTATION REQUEST RECEIVED

        CONTACT INFORMATION:
        --------------------
        Name: {contact_name}
        Institution: {institution}
        Email: {email}
        Phone: {phone}

        SERVICE REQUEST DETAILS:
        -----------------------
        Service Type: {service_type}
        Equipment: {equipment_details}

        DESCRIPTION/FAULT INFO:
        -----------------------
        {description}

        --
        This email was sent from the Fortress Medical Engineers Website.
        """

        try:
            # 3. Send the Email
            send_mail(
                subject=subject,
                message=message_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['samzypaul@gmail.com'],
                fail_silently=False,
            )

            # Return a success state to the template
            return render(request, 'quotation.html', {
                'success_name': contact_name,
                'submitted': True
            })

        except Exception as e:
            # Handle potential SMTP errors
            messages.error(request, f"There was an error sending your request: {e}")

    return render(request, 'quotation.html')