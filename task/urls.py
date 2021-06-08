from django.urls import path
from task import views

urlpatterns = [
    path('',views.main,name='main'),
    path('register/',views.registration,name='register'),
    path('save_register/',views.save_register,name='save_register'),
    path('login_validate/',views.login_request,name='login_validate'),
    path('compose/',views.compose,name='compose'),
    path('save_mail/',views.save_mail,name='save_mail'),
    path('inbox/',views.inbox,name='inbox'),
    path('sent_mail/',views.sent_mail,name='sent_mail'),
    path('<int:id>/make_spam/',views.make_spam,name='make_spam'),
    path('<int:id>/make_unspam/',views.make_unspam,name='make_spam'),
    path('spam/',views.spam,name='spam'),
    path('view/',views.view,name='view'),
    path('logout/',views.logout_page,name='logout'),
    path('<int:id>/make_draft/',views.make_draft,name='make_draft'),
    path('draft/',views.draft,name='draft'),
    path('<int:id>/make_trash/',views.make_trash,name='make_trash'),
    path('trash/',views.trash,name='trash'),
    path('<int:id>/un_trash/',views.make_untrash,name='un_trash'),
    path('<int:id>/delete/',views.delete,name='delete'),
    path('save_draft/',views.save_draftmail,name='save_draft'),

]
