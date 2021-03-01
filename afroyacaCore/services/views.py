from django.shortcuts import render


def oh_my_box(request):
    template_name = "services/oh_my_box.html"
    context = {}

    return render(request, template_name, context)