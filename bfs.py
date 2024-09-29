'''Breadth-first search algorithm to find a mango seller in a graph.'''

from collections import deque
graph = {}
graph['me'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tho', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['tho'] = []
graph['jonny'] = ['mango seller']


def person_is_seller(name):
    '''Check if a person is a mango seller.'''
    return name == 'mango seller'


def search(name):
    '''Search for a mango seller in the graph using breadth-first search.'''
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                return True

            search_queue += graph[person]
            searched.append(person)
    return False


print('Mango seller found' if search('me') else 'Mango seller not found')
