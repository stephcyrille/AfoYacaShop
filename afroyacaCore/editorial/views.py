from django.shortcuts import render


def editorial(request):
    template_name = "editorial/editorial.html"
    context = {}

    return render(request, template_name, context)