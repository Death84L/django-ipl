#from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.db.models import Count, Q, F
from .models import Number_store
import json 


def house(request):
    return render(request, 'house.html')

#task1
def matches_per_year(request):
    matches_per_year = Number_store.objects.values('season').annotate(num_matches=Count('id')).order_by('season')
    json_data = json.dumps(list(matches_per_year))
    return render(request, 'matches_per_year.html', {'data': json_data})

#task2
def matches_won_by_teams(request):
    matches_won_by_teams = Number_store.objects.values('team1').annotate(num_wins=Count('team1')).order_by('team1')
    json_data = json.dumps(list(matches_won_by_teams))
    return render(request, 'matches_won_by_teams.html', {'data': json_data})

#task5
def matches_played_vs_won(request):
    years = Number_store.objects.values('season').distinct().order_by('season')
    selected_year = request.GET.get('year')  # Get the selected year from the request's GET parameters
    if selected_year:
        matches_played_vs_won = Number_store.objects.filter(season=selected_year).values('team1').annotate(
            num_matches_played=Count('team1'),
            num_matches_won=Count('team1', filter=Q(winner=F('team1')))
        )
    else:
        matches_played_vs_won = []

    context = {
        'years': years,
        'selected_year': selected_year,
        'data': json.dumps(list(matches_played_vs_won))
    }
    return render(request, 'matches_played_vs_won.html', context)

