from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from xhtml2pdf import pisa 

def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

def index(request):
    return render(request, "website/index.html")

def tempo(request):
    return render(request, "website/tempp.html")


def view(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        #do something
        request_data = request.POST.get('printContents')
        
        return HttpResponse("OK")


