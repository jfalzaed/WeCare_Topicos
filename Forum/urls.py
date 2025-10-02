from django.urls import path
from . import views

app_name = "Forum"

urlpatterns = [
    path('create/', views.comentario_create, name='crear-comentario'),                          # /forum/comments/create/
    path('edit/<int:id>/', views.comentario_edit, name='editar-comentario'),                    # /forum/comments/edit/1/
    path('delete/<int:id>/', views.comentario_delete, name='eliminar-comentario'),              # /forum/comments/delete/1/
    path('favorite/<int:comentario_id>/', views.favorite, name='marcar-favorito'),              # /forum/comments/favorite/1/
    path('<int:comentario_id>/reply/create/', views.respuesta_create, name='crear-respuesta'),  # /forum/comments/1/reply/create/
    path('<int:comentario_id>/like/', views.like_toggle, name='like-toggle'),                   # /forum/comments/1/like/
    path('reply/delete/<int:id>/', views.respuesta_delete, name='eliminar-respuesta'),          # /forum/comments/reply/delete/1/
    path('search/', views.buscar_comentario, name='buscar-comentario'),                         # /forum/comments/search/
    path('detail/<int:id>/', views.detalle_comentario, name='detalle-comentario'),              # /forum/comments/1/
    path('', views.comentarios_view, name='comentarios'),                                       # /forum/comments/
]