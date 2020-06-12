from django.urls import path


from . import views

app_name = "article"


urlpatterns = [
    path('', views.articles, name="articles"),
    path('detail/<int:article_id>', views.detail, name="detail"),
    path('add_article/', views.create_article, name="createArticle"),
    path('edit/<int:article_id>', views.edit, name="edit"),
    path('delete/<int:article_id>', views.delete, name="delete"),
    path('comment/<int:article_id>', views.addComment, name="comment")
]