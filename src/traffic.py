from time import strftime
from functools import wraps
from flask import request, session
from objects import clean_tree
import json

def add_statistics(route_func):
    def app_route(rule, **options):
        def insert_func(func):
            @wraps(func)
            def website_func(*args, **kwargs):
                if new_period_arrived():
                    archive()

                if 'user_no' not in session:
                    session['user_no'] = get_new_session_user()
                
                log_to_today(strftime('[%Y-%b-%d %H:%M:%S] ') + ' User ' + session['user_no'] + ' : ' + request.method + ' ' + request.path)

                output = func(*args, **kwargs)
                clean_tree()
                
                return output

            route_func(rule, **options)(website_func)
        
        return insert_func

    return app_route

def log_to_today(info, filename='users.log'):
    """Add some more info to the logger"""
    with open('data/traffic.log', 'a') as logger_file:
        logger_file.write(info + '\n')

def archive():
    """Write the current logging file away."""
    with open('data/traffic.log', 'r') as logger_file:
        date = logger_file.readline().rstrip()

        with open(f"data/logs/{date}.txt", 'w') as storing_file:
            for line in logger_file:
                storing_file.write(line)
    
    with open('data/traffic.log', 'w') as logger_file:
        logger_file.write(f"{strftime('%Y-%b-%d')}\n")

def new_period_arrived():
    with open('data/traffic.log', 'r') as logger_file:
        date = logger_file.readline()

        now = strftime("%Y-%b-%d\n")

        return date != now

def get_new_session_user():
    i = json.load(open('data/logs/counter.json', 'r'))
    json.dump(i+1, open('data/logs/counter.json', 'w'))

    return f'#{i}'