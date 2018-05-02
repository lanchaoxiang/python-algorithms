from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue =deque()#创建列队
search_queue +=graph['you']


def person_is_seller(person):
    return name[-1] == 'm'
    while search_queue:#当列队不为空
        person = search_queue.popleft()#列队中取出一个人
        if person_is_seller(person):
            print(person+'is a seller')
            return True
        else:
            search_queue += graph[person]
    return False