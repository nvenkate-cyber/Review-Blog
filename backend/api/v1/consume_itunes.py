from requests import get
from urllib.parse import urlencode
from datetime import timedelta
import os
import redis
import sys
import pickle
import codecs


# in results field this are the ones that we a re gon to extract
#   - artistName
#   - trackName
#   - artworkUrl100
#   - primaryGenreName

def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host=os.getenv("HOST"),
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

def get_data_cache(key: str) -> str:
    val = client.get(key)
    return val


def send_data_cache(key: str, value:str) -> bool:
    state = client.setex(key, timedelta(seconds=86400), value=value,)
    return state

def check_data_cache(query):
    data = get_data_cache(key=query)
    if data is not None:
       return data
    
    else:
        data = get_response(query)
        data = codecs.encode(pickle.dumps(data), "base64").decode()
        state = send_data_cache(key=query, value=data)
        
        if state is True:
            result = pickle.loads(codecs.decode(data.encode(), "base64"))
        
        return result
        
        
        
        