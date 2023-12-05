from django.contrib import admin
from django.urls import path

from studentapp import views

urlpatterns = [
    path('',views.main_index,name='main_index'),
    path('login',views.login,name='login'),
    path('admin',views.admin,name='admin'),
    path('managestaff',views.managestaff,name='managestaff'),
    path('addstaff',views.addstaff,name='addstaff'),
    path('manageexpert',views.manageexpert,name='manageexpert'),
    path('addexpert',views.addexpert,name='addexpert'),
    path('viewparent',views.viewparent,name='viewparent'),
    path('logout',views.logout,name='logout'),

    path('staff',views.staff,name='staff'),
    path('mng_attendence',views.mng_attendence,name='mng_attendence'),
    path('add_attendence',views.add_attendence,name='add_attendence'),
    path('mng_DA',views.mng_DA,name='mng_DA'),
    path('add_DA',views.add_DA,name='add_DA'),
    path('mng_parent',views.mng_parent,name='mng_parent'),
    path('add_parent',views.add_parent,name='add_parent'),
    path('view_leave',views.view_leave,name='view_leave'),
    path('change_pw',views.change_pw,name='change_pw'),
    path('changepwd',views.changepwd,name='changepwd'),
    path('updgrade',views.updgrade,name='updgrade'),

    path('parent',views.parent,name='parent'),
    path('view_attendence',views.view_attendence,name='view_attendence'),
    path('view_attendence1',views.view_attendence1,name='view_attendence1'),
    path('view_DA',views.view_DA,name='view_DA'),
    path('view_SM',views.view_SM,name='view_SM'),
    path('chat_staff',views.chat_staff,name='chat_staff'),
    path('ask_doubt_reply',views.ask_doubt_reply,name='ask_doubt_reply'),
    path('ask_doubt',views.ask_doubt,name='ask_doubt'),
    path('adddoubt',views.adddoubt,name='adddoubt'),
    path('sendleave',views.sendleave,name='sendleave'),
    path('addleave',views.addleave,name='addleave'),
    path('viewresult_par',views.viewresult_par,name='viewresult_par'),
    path('insert_test',views.insert_test,name='insert_test'),
    path('attendtest/<int:id>',views.attendtest,name='attendtest'),


    path('expert',views.expert,name='expert'),
    path('mng_SM',views.mng_SM,name='mng_SM'),
    path('add_SM',views.add_SM,name='add_SM'),
    path('mng_ques',views.mng_ques,name='mng_ques'),
    path('add_ques',views.add_ques,name='add_ques'),
    path('mng_sugges',views.mng_sugges,name='mng_sugges'),
    path('add_sugges',views.add_sugges,name='add_sugges'),
    path('view_doubt_reply',views.view_doubt_reply,name='view_doubt_reply'),
    path('reply/<int:id>',views.reply,name='reply'),
    path('addedSM',views.addedSM,name='addedSM'),
    path('sendreply',views.sendreply,name='sendreply'),
    path('viewresult',views.viewresult,name='viewresult'),
    path('addedsugges', views.addedsugges, name='addedsugges'),

    path('logincode',views.logincode,name='logincode'),
    path('addedstaff',views.addedstaff,name='addedstaff'),
    path('addedexpert',views.addedexpert,name='addedexpert'),
    path('addedparent',views.addedparent,name='addedparent'),
    path('addedDA',views.addedDA,name='addedDA'),
    path('addedattendence',views.addedattendence,name='addedattendence'),
    path('addedques',views.addedques,name='addedques'),


    path('updateexpert',views.updateexpert,name='updateexpert'),
    path('updatestaff',views.updatestaff,name='updatestaff'),
    path('updateda',views.updateda,name='updateda'),
    path('updateparent',views.updateparent,name='updateparent'),
    path('updatesm',views.updatesm,name='updatesm'),

    path('searchparent',views.searchparent,name='searchparent'),
    path('searchexpert',views.searchexpert,name='searchexpert'),
    path('searchstaff',views.searchstaff,name='searchstaff'),
    path('parentsearch',views.parentsearch,name='parentsearch'),
    path('search_DA',views.search_DA,name='search_DA'),
    path('seach_leave',views.seach_leave,name='seach_leave'),
    path('searchDA',views.searchDA,name='searchDA'),
    path('search_doubt',views.search_doubt,name='search_doubt'),
    path('searchSM',views.searchSM,name='searchSM'),
    path('search_SM',views.search_SM,name='search_SM'),
    path('searchdoubt',views.searchdoubt,name='searchdoubt'),
    path('s_mng_attendence',views.s_mng_attendence,name='s_mng_attendence'),
    path('search_attendance',views.search_attendance,name='search_attendance'),
    path('searchresult', views.searchresult, name='searchresult'),
    path('searchresult_par', views.searchresult_par, name='searchresult_par'),



    path('deleteda/<int:id>',views.deleteda,name='deleteda'),
    path('deleteparent/<int:id>',views.deleteparent,name='deleteparent'),
    path('deletestaff/<int:id>',views.deletestaff,name='deletestaff'),
    path('deleteexpert/<int:id>',views.deleteexpert,name='deleteexpert'),
    path('deleteSM/<int:id>',views.deleteSM,name='deleteSM'),
    path('deleteQA/<int:id>',views.deleteQA,name='deleteQA'),
    path('deletesug/<int:id>',views.deletesug,name='deletesug'),
    path('view_sugges/<str:id>',views.view_sugges,name='view_sugges'),

    path('editexpert/<int:id>',views.editexpert,name='editexpert'),
    path('editstaff/<int:id>',views.editstaff,name='editstaff'),
    path('editda/<int:id>',views.editda,name='editda'),
    path('editparent/<int:id>',views.editparent,name='editparent'),
    path('editsm/<int:id>',views.editsm,name='editsm'),

    path('upgradepost/<int:id>',views.upgradepost,name='upgradepost'),


path('chatwithparent', views.chatwithparent, name='chatwithparent'),
path('chatview', views.chatview, name='chatview'),
path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),

path('chatwithstaff', views.chatwithstaff, name='chatwithstaff'),
path('chatviews', views.chatviews, name='chatviews'),
path('coun_msgs/<int:id>', views.coun_msgs, name='coun_msgs'),
path('coun_insert_chats/<str:msg>/<int:id>', views.coun_insert_chats, name='coun_insert_chats'),


]