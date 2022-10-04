from django.urls import path
from . import views

# url을 app별로 분리하기 위해 이름을 명시
app_name = "todos"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:todo_pk>', views.update, name='update'),
    path('delete/<int:todo_pk>', views.delete, name='delete'),
    # 요청 - 응답
    # 어떤 주소(datail/)로 요청하면
    # 어떤 VIEW 함수(datail)를 응답할까?
    path('detail/<int:pk_>', views.detail, name='detail'),
    path('edit/<int:pk_>', views.edit, name='edit'),
    #path('update/<int:pk_>', views.update, name='update'),
]