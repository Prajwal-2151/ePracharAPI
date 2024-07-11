from django.urls import path

from electionadmin.views import AdminAPI, AdminLoginAPI, GetMessagebyCode

urlpatterns = [
          path('allAdmins/', AdminAPI.as_view({'get': 'list'})),
          path('adminDetails/<int:pk>/', AdminAPI.as_view({'get': 'retrieve'})),
          path('createAdmin/', AdminAPI.as_view({'post': 'create'})),
          path('updateAdmin/<int:pk>', AdminAPI.as_view({'put': 'update'})),
          path('partialupdateAdmin/<int:pk>/', AdminAPI.as_view({'patch': 'partial_update'})),
          path('deleteAdmin/<int:pk>/', AdminAPI.as_view({'delete': 'destroy'})),

          path('adminLogin/', AdminLoginAPI.as_view()),

          path('getMessagebyCode/<str:a_contactno>/', GetMessagebyCode.as_view()),

]
