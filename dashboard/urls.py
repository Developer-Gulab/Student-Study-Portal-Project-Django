
from . import views
from dashboard import *
from django.urls import path

urlpatterns= [
    # home page path

    path('',views.home, name = "home"),

    #notes section path

    path('notes', views.notes, name = "notes"),
    path('delete_note/<int:pk>', views.delete_note, name = "delete_note"),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name = "notes_detail"),

    #homework section path

    path('homework', views.homework, name = "homework"),
    path('update_homework/<int:pk>', views.update_homework, name = "update-homework"),
    path('delete_homework/<int:pk>', views.delete_homework, name = "delete-homework"),


    #YOUTUBE SECTION PATH

    path('youtube', views.youtube, name = "youtube"),


    #TODOO SECTION PATH

    path('todo', views.todo, name = "todo"),
    path('update_todo/<int:pk>', views.update_todo, name = "update-todo"),
    path('delete_todo/<int:pk>', views.delete_todo, name = "delete-todo"),


    # BOOK SECTION PATH

    path('books', views.books, name = "books"),


    # DICTIONARY SECTION PATH

    path('dictionary', views.dictionary, name = "dictionary"),


    # WIKIPEDIA SECTION PATH


    path('wiki', views.wiki, name = "wiki"),


    # CONVERSION SECTION PATH

    path('conversion', views.conversion, name = "conversion"),  


       
]