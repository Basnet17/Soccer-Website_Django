from django import forms

LEAGUE_CHOICE= ['Spanish La Liga','English Premier League','Italian Serie A']

class leagueform(forms.Form):
    select_league = forms.CharField("League", widget=forms.Select(choices=LEAGUE_CHOICE)) 
