from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'articles'

urlpatterns = [
                  path('', views.index, name='index'),
                  path('<int:article_id>', views.detail, name='detail'),
                  path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
                  path('<int:article_id>/delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
                  path('<int:article_id>/edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'),
                  path('<int:article_id>/detail_comment/<int:comment_id>', views.detail_comment, name='detail_comment'),
              ]
