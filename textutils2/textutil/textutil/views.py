from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #    params={'name':'manav','place':'jammu'}
    return render(request, 'index.html')
    # return HttpResponse("home")


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcapse = request.POST.get('fullcapse', 'off')
    lineremover = request.POST.get('lineremover', 'off')
    extraspaceremover = request.POST.get('extraSpaceRemover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # analyze the text
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        a = ""
        for char in djtext:
            if char not in punctuations:
                a = a + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': a}
        djtext = a
    # return render(request, 'analyze.html', params)
    if (fullcapse == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if (lineremover == "on"):
        a = ""
        for char in djtext:
            if char != "\n":
                a = a + char
        params = {'purpose': 'Extra line is removed', 'analyzed_text': a}
        djtext = a
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        a = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == "" and djtext[index + 1] == ""):
                a = a + char
        params = {'purpose': 'Extra space is removed ', 'analyzed_text': a}
        djtext = a
        # return render(request,'analyze.html', params)

    if (charcounter == "on"):
        b = 0
        for c in djtext:
            if c.isspace() != True:
                b = b + 1
        params = {'purpose': 'Length of your text is :', 'analyzed_text': b}
        djtext = b

    if (removepunc != "on" and lineremover != "on" and extraspaceremover != "on" and fullcapse != "on" ):
        return HttpResponse("please select any operation and try again")
    return render(request, 'analyze.html', params)
