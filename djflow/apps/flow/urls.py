from django.urls import path
from .views import Dashboard, AccountList, AccountNew, AccountDelete, AccountEdit
from .views import TransactionList, TransactionNew, TransactionEdit, TransactionDelete
from .views import CategoryList, CategoryNew, CategoryEdit, CategoryDelete
from .views import TransactionCommentList, TransactionCommentNew

app_name = 'flow'

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('flow/account/list/', AccountList.as_view(), name="account-list"),
    path('flow/account/new/', AccountNew.as_view(), name="account-new"),
    path('flow/account/delete/(?P<pk>.*)/', AccountDelete.as_view(), name="account-delete"),
    path('flow/account/edit/(?P<pk>.*)/', AccountEdit.as_view(), name="account-edit"),
    path('flow/transaction/list/', TransactionList.as_view(), name="transaction-list"),
    path('flow/transaction/new/', TransactionNew.as_view(), name="transaction-new"),
    path('flow/transaction/edit/(?P<pk>.*)/', TransactionEdit.as_view(), name="transaction-edit"),
    path('flow/transaction/delete/(?P<pk>.*)/', TransactionDelete.as_view(), name="transaction-delete"),
    path('flow/category/list/', CategoryList.as_view(), name="category-list"),
    path('flow/category/new/', CategoryNew.as_view(), name="category-new"),
    path('flow/category/edit/(?P<pk>.*)/', CategoryEdit.as_view(), name="category-edit"),
    path('flow/category/delete/(?P<pk>.*)/', CategoryDelete.as_view(), name="category-delete"),
    path('flow/transaction/comment/list/', TransactionCommentList.as_view(), name="transaction-comment-list"),
    path('flow/transaction/(?P<trans_id>.*)/comment/new/', TransactionCommentNew.as_view(), name="transaction-comment-new"),
]
