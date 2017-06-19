from django.shortcuts import redirect


def views_post(request):
    return redirect('post:post_list')
