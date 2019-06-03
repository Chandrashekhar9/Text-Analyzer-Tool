from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'About.html')

def Analyzed(request):
    Usertext = request.POST['textarea']
    rvmpunc = request.POST.get('checkboxx1')
    uprcs = request.POST.get('checkboxx2')
    rvmnwln = request.POST.get('checkboxx3')
    extrspc = request.POST.get('checkboxx4')
    chrcnt = request.POST.get('checkboxx5')
    data = Usertext
    if rvmpunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in data:
            if char not in punctuations:
                analyzed= analyzed+char
        data = analyzed

    if uprcs == 'on':
        Uppercase = data.upper()
        data = Uppercase
        print(data)

    if rvmnwln == 'on':
        analyzed = ""
        for char in data:
            if char != '\n' and char !='\r':
                analyzed = analyzed + char

        data = analyzed


    if extrspc == 'on':
        analyzed = ""
        for index, char in enumerate(data):
            if not (data[index] == " " and data[index + 1] == " "):
                analyzed = analyzed + char
        data = analyzed

    if chrcnt == 'on':
        analyzed = " "
        sum = 0
        i = 0
        for char in data:
            if char not in analyzed:
                sum= sum + len(char)
        words = data.split()
        word_list = {}
        for word in words:
            if word not in word_list:
                i = i + 1
        return render(request, 'Analyzed.html', {'result': data,'result1':sum, 'words': i, 'sndchrcnt':chrcnt})
    return render(request, 'Analyzed.html', {'result': data})

