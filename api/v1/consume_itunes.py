from requests import get
from urllib.parse import urlencode
from datetime import timedelta
import os
import redis
import json
import sys



def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host=os.getenv('HOST'),
            port=6379,
            db=0,
            socket_timeout=5,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("Authentication Error")
        sys.exit(1)
        
client = redis_connect()


def get_response(query=None, media='all', limit=50):
    """
    Get response given the query and media type requested by user.
    """

    if query is None:
        return False, []

    request_data = {
        'url': 'https://itunes.apple.com/search?',
        'payload': {
            'term': query,
            'media': media,
            'limit': limit
        }
    }

    request_str = request_data['url'] +\
        urlencode(request_data['payload'])
    response = get(request_str)

    if not response.ok:
        return None

    data = response.json()

    if len(data['results']) == 0:
        return None

    return data



def get_data_cache(query):
    val = client.get(query)
    return val


def send_data_cache(query, data):
    state = client.setex(query, timedelta(seconds=86400), data,)
    return state

def check_cache(query):
    data = get_data_cache(query)
    if data is not None:
        data = json.loads(data)
        data["cache"] = True
        return data
    
    else:
        data = get_response(query)
        data["cache"] = False
        data = json.dumps(data)
        state = send_data_cache(query, data)
            
        if state is True:
            return json.loads(data)
    return data


        
        
        