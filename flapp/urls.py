from django.contrib.urls import urls
from flapp import views

# urlpatterns

urlpatterns = [

    url(r'^about', views.about, name= "about" ),
    url(r'^contributors', views.contributors, name= "contributors" ),
    url(r'^core-team', views.coreteam, name= "coreteam" ),
    # url(r'^core-team', views.coreteam, name= "coreteam" ), non core team

    url(r'^contribute', views.contribute, name= "contribute" ),
    url(r'^science-technology', views.sciencetechnology, name= "sciencetechnology" ),
    url(r'^economics-finanace', views.economicsfinance, name= "economicsfinance" ),
    url(r'^world-affairs', views.worldaffairs, name= "worldaffairs" ),




]
