from requests import get
from urllib.parse import urlencode


# in results field this are the ones that we a re gon to extract
#   - artistName
#   - trackName
#   - artworkUrl100
#   - primaryGenreName

def extract_data(result, media='music'):
    if media == 'music':
        data = {
                'artist': result['artistName'],
                'title': result['trackName'],
                'artwork': result['artworkUrl100'],
                'genre': result['primaryGenreName']
                }
    elif media == 'movie':
        data = {}
    elif media == 'podcast':
        data = {}
    else:
        raise ValueError('cannot extrac ' + str(media) + ' media type')
    return data

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
