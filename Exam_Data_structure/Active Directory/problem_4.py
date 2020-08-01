#!/usr/bin/env python

# class Group
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

#create class Queue
class Queue:
  def __init__(self):
    self.storage = []
  
  def enqueue(self, value):
    self.storage.append(value)
  
  def dequeue(self):
    if self.size() >= 1:
      return self.storage.pop(0)

  def size(self):
    return len(self.storage)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    #basic variables
    q = Queue() 
    
    # defense function
    if user is None or user == "":
      return "No found user"
    

    if isinstance(group, Group):
      left = group.get_groups() 
      right = group.get_users() 

      if user in right:
        return True 

      for item in left:
        q.enqueue(item)
      
      while q.size() >= 1:
        first = q.dequeue()
        if user in first.get_users():
            return True
        x = first.get_groups()
        for i in range(len(x)):
          q.enqueue(x[i])
          
      return False
    else:
      return None


# Create class group
a = Group("A")
b = Group("B")
c = Group("C")
d = Group("D")
e = Group("E")
f = Group("F")

#add users
a.add_user("Muhamed")
a.add_user("Mona")
a.add_user("Anas")

c.add_user("Apple")
c.add_user("Banana")
c.add_user("Orange")

d.add_user("1")
d.add_user("2")
d.add_user("3")

f.add_user("Dog")
f.add_user("Cat")
f.add_user("Elephent")

#add group
e.add_group(f)
c.add_group(e)
b.add_group(d)
a.add_group(c)
a.add_group(b)


# function Test
def test_cases():
  test_cases = [#Edge case if group is None
                (("1", None), None),
                #Edge case if user is None
                ((None, "a"), "No found user"),
                #Edge case if user and group is None
                ((None, None), "No found user"),
                (("5", a), False),
                (("Dog", f), True),
                (("Dog", e), True),
                (("Dog", c), True),
                (("1", a), True),
                (("", a), "No found user"),
                (("1", "a"), None),
               ]
  
  for (args, answer) in test_cases:
    try:
      result = is_user_in_group(*args)
      if result == answer and answer != "AssertionError":
        print("Test case group passed!")
      else:
        print("Test with data:", args, "failed")
    
    except AssertionError:
          if answer == "AssertionError":
              print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
          else:
              print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))

  
test_cases()