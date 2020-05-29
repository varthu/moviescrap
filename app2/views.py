from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import movie_details,soundtrack
from .utils import add_soundtrack


def add_moviedetails(request):
    if request.method == 'POST':
        try:
            movie_id = request.POST.get('movie_id')
            movie_name = request.POST.get('movie_name')
            print(movie_name, "----------------->")
            details_save = movie_details(movie_id=movie_id, movie_name=movie_name)
            # print(details_save, "----------------------------->")
            details_save.save()
            #details_save.movie_id   
            soundtrack_list = add_soundtrack(movie_name)
            # print(soundtrack_list) 
            for i in soundtrack_list:
                if len(i) ==4: 
                    print(i)
                    soundtrack_list_save = soundtrack(soundtrack_id=details_save.movie_id,title=i[1],singer=i[2],length=i[3])
                    soundtrack_list_save.save()
        except Exception as e:
            print(e)
            return render(request, 'login.html',{'error':'MOVIE NAME ALREADY EXIST'})
    return render(request, 'login.html')




