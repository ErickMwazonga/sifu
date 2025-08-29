'''
You work for a company with more than a million employees when a pandemic hit.
The virus is likely spread when people are together in a room.
You need to create a system that can do contact tracing so that the company can
warn employees to stay home if they were exposed.

You have records of when someone entered and exit a room in the following format:
time (int), username (string), room (string), enter/exit

For example:
0, hyobyun, meetingRoomA, enter
5, jeff, meetingRoomA, enter
10, hyobyun, meetingRoomA, exit
15, jeff, meetingRoomA, exit

Given a username of someone who had the disease, 
list out the usernames of everyone who stayed in the same room with them.

logs = [
  "0, alice, meetingRoomA, enter",
  "3, hyobyun, meetingRoomA, enter",
  "5, hyobyun, meetingRoomA, exit",
  "8, alice, meetingRoomA, exit",
  "8, bob, meetingRoomB, enter",
  "9, dave, meetingRoomC, enter",
  "12, alice, meetingRoomB, exit",
  "14, carol, meetingRoomC, exit",
  "15, jeff, meetingRoomA, exit",
  "18, bob, meetingRoomB, exit",
  "20, dave, meetingRoomC, exit",
  "22, eric, meetingRoomA, enter",
  "26, frank, meetingRoomA, enter",
  "30, eric, meetingRoomA, exit",
  "35, frank, meetingRoomA, exit",
  "40, hyobyun, meetingRoomD, enter",
  "45, grace, meetingRoomD, enter",
  "50, grace, meetingRoomD, exit",
  "55, hyobyun, meetingRoomD, exit",
]

curr_infected_room = None
infected_persons = { jeff, grace }
'''

from collections import defaultdict

def get_infected_persons(logs: list[str], infected_user: str) -> list[str]:
    curr_infected_room = None
    curr_room_call = defaultdict(set)
    infected_persons = set()

    parsed_logs = list(sorted(logs, key=lambda x: int(x.split(', ')[0])))

    for log in parsed_logs:
        _time, username, room, action = log.split(', ')
        if action == 'enter':
            if username == infected_user:
                infected_persons |= curr_room_call[room]
                curr_infected_room = room
            else:
                if curr_infected_room == room:
                    infected_persons.add(username)
                curr_room_call[room].add(username)
        else:
            if username == infected_user:
                curr_infected_room = None
            else:
                curr_room_call[room].remove(username)
    
    return list(infected_persons)

logs = [
  "0, alice, meetingRoomA, enter",
  "3, hyobyun, meetingRoomA, enter", 
  "4, jeff, meetingRoomA, enter", 
  "5, hyobyun, meetingRoomA, exit",
  "6, alice, meetingRoomA, exit",
  "7, jeff, meetingRoomA, exit",
]

assert set(get_infected_persons(logs, 'hyobyun')) == set(['jeff', 'alice'])