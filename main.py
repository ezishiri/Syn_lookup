import os
import requests
import random 


my_secret = os.environ['API_KEY']


def get_synonyms(keyword):
    url = f'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{keyword}?key={my_secret}'
    response = requests.get(url)
    response_json = response.json()
    
    #parsing json output 
    if 'meta' in response_json and response_json['meta']['status'] == 404:
        print(f"No synonyms found for '{keyword}'")
        return []
    else:
        syns = response_json[0].get('meta', {}).get('syns', [])
        return [s for syn_list in syns for s in syn_list if s != keyword]

def get_random_synonym(keyword):
    synonyms = get_synonyms(keyword)
    if not synonyms:
        return None
    else:
        return random.choice(synonyms)


# synonyms = get_synonyms('happy')
# print(synonyms)

random_synonym = get_random_synonym("wild")
print(random_synonym)
