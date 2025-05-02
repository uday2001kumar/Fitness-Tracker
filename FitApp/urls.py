from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='index'),
    path('signup',signup,name='signup'),
    path('login',login,name='login'),
    path('about',about,name='about'),
    path('signupview',signupview,name='sview'),
    path('logout',logout,name='logout'),
    path('home',home,name='home'),
    path('adminlogin',adminlogin,name='adminlogin'),
    path('forget_Password',forget_Password,name="forget_Password"),

    # Profile
    path('profileview',profile_view,name='profileview'),
    path('profile',profile,name='profile'),
    path('update_profile',update_profile,name='update_profile'),

    # Workout
    path('workouthome',workouthome,name='workouthome'),
    path('workout',workout,name='workout'),
    path('add_workout',add_workout,name='add_workout'),
    path('view_past_workouts',view_past_workouts,name='view_past_workouts'),
    path('weight_loss',weight_loss,name='weight_loss'),
    path('weight_gain',weight_gain,name='weight_gain'),
    path('delete_workout/<int:pk>/',delete_workout, name='delete_workout'),
    path('show_weekly_chart',show_weekly_chart,name='show_weekly_chart'),
    path('suggession',suggession,name='suggession'),
    path('generate_monthly_report',generate_monthly_report,name='generate_monthly_report'),
    path('generate_monthly_chart',generate_monthly_chart,name='generate_monthly_chart'),
    path('compare',compare,name='compare'),

    # -------------------------------------------------
    # Nutrition App
    path('nutrition_home',nutrition_home,name='nutrition_home'),
    path('nutritions',nutritions,name='nutritions'),
    path('add_nutrition/',add_nutrition,name='add_nutrition'),
    path('food_weight_loss',food_weight_loss,name="food_weight_loss"),
    path('food_weight_gain',food_weight_gain,name='food_weight_gain'),
    path('view_nutrition',view_nutrition,name='view_nutrition'),
    path('delete_nutrition/<int:pk>/',delete_nutrition, name='delete_nutrition'),
    path('weekly-progress/', weekly_progress_chart, name='weekly_progress'),
    path('suggesionsn',suggesionsn,name='suggesionsn'),
    path('nutrition_comparison',nutrition_comparison,name='nutrition_comparison'),


    # Admin
    path('admin_dashboard',admin_dashboard,name='admin_dashboard'),
    path('admin_users',admin_users,name='admin_users'),
    path('admin_delete_user<int:pk>',admin_delete_user,name='admin_delete_user'),
    path('Admin_add_workout',Admin_add_workout,name="Admin_add_workout"),
    path('Admin_View_Workouts',Admin_View_Workouts,name='Admin_View_Workouts'),
    path('Admin_Delete_Workout',Admin_Delete_Workout,name='Admin_Delete_Workout'),
    path('Admin_Delete_Workout_List<int:pk>',Admin_Delete_Workout_List,name='Admin_Delete_Workout_List'),
    path('delete_workout<int:pk>',delete_workout,name="Admin_Delete_Workout"),
    path('admin_add_nutrition',admin_add_nutrition,name='admin_add_nutrition'),
    path('Admin_View_Nutrition',Admin_View_Nutrition,name="Admin_View_Nutrition"),
    path('Admin_Delete_Nutrition_List',Admin_Delete_Nutrition_List,name='Admin_Delete_Nutrition_List'),
    path('Admin_Delete_Nutrition<int:pk>',Admin_Delete_Nutrition,name='Admin_Delete_Nutrition'),
]