#Start by defining helper function that we'll use to
#sort the list
def get_event_date(event):
    return event.date
#We'll use this function as the parameter to the sort
#function to sort the list

#Now we start coding our processing function
def current_users(events):
    #Inside function we sort events by using sort
    #method and passing function just created as key
  events.sort(key=get_event_date)
  #dictionary where we store names and users of machine
  machines = {}
  #iterate through list of events
  for event in events:
      #check if machine affected by event in dict.
    #if not, add it with an empty set as the value
    if event.machine not in machines:
      machines[event.machine] = set()
      #for login events, we want to add users to
    #list and for logout we remove from list and if they have logged out and not logged in
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout" and not "login": #important otherwise we get error
      machines[event.machine].remove(event.user)
  return machines

#dictionary will contain all machines we've seen as keys with a set
#containing the current users as the values

#Printing report
def generate_report(machines):
    for machine, users in machines.items():
        #want to ensure we don't print any machines where nobody
        #is currently logged in 
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)
