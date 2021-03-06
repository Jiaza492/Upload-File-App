
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from myproject.uploadPic.forms import DocumentForm


def list(request):
    
    if request.method == 'POST':
        # If this page was accessed by a post method
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Define a new document which is the picture uploaded.
            newdoc = request.FILES['docfile']
            # Redirect to the document after POST
            return HttpResponse(newdoc,content_type="image")
        else:
            return HttpResponse("No Picture Selected, Please go back to select a valid picture!")
    else:
        # If this page was accessed by a redirect way.
        form = DocumentForm()
        # Render list page with the form
        return render_to_response(
                'list.html',
                {'form': form},
                context_instance=RequestContext(request)
        )
