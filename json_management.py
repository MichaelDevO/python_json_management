#https://jsonplaceholder.typicode.com/todos
#https://jsonplaceholder.typicode.com/users

import requests
import json

link = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task(link):
    completedTask = dict()
    for i in tasks:
        if(i["completed"] == True):
            try:
                completedTask[i["userId"]] += 1
            except KeyError:
                completedTask[i["userId"]] = 1
    return completedTask

def users_top_compl(completedTask):
    userWithMax = []
    maxNumberTasks = max(completedTask.values())
    for userId, numberTasks in completedTask.items():
        if(numberTasks == maxNumberTasks):
            userWithMax.append(userId)
    return userWithMax


try:
    tasks = link.json()
except json.decoder.JSONDecodeError:
    print("invalid format")
else:
    completedTask = count_task(link)
    full = users_top_compl(completedTask)
    print(full)


link = requests.get("https://jsonplaceholder.typicode.com/users")


users = link.json()

for user in users:
    if(user["id"] in full):
        print("the winner is: ", user["name"])