from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
import redis
import time

MAX_ATTEMPTS = 5
LOCK_TIME = 60  # seconds (1 minute)


def get_redis_client():

    try:
        client = redis.StrictRedis(host="localhost", port=6379, db=1)
        client.ping()
        print("Redis connected successfully")
    except redis.RedisError as e:
        print("Redis connection failed:", e)


def login_view(request):

    attempts = request.session.get('login_attempts', 0)
    lock_until = request.session.get('lock_until')


    if lock_until and time.time() < lock_until:
        remaining = int(lock_until - time.time())
        messages.error(request, f"Account locked. Try again in {remaining} seconds.")
        return render(request, "accounts/login.html")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            request.session['login_attempts'] = 0
            request.session.pop('lock_until', None)

            if user.role == "ADMIN":
                return redirect("admin_dashboard")
            elif user.role == "AGENT":
                return redirect("agent_dashboard")
            else:
                return redirect("customer_dashboard")

        else:
            attempts += 1
            request.session['login_attempts'] = attempts

            if attempts >= MAX_ATTEMPTS:
                request.session['lock_until'] = time.time() + LOCK_TIME
                messages.error(request, "Too many failed attempts. Account locked for 1 minute.")
            else:
                messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


        

def logout_view(request):
    logout(request)
    return redirect("login")



