# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
  def __init__(self):
    # Initialize the trie with an root node and a handler, this is the root path or home page node
    self.root = RouteTrieNode("/", "root handler")

  def insert(self, path, handler):
    # Similar to our previous example you will want to recursively add nodes
    # Make sure you assign the handler to only the leaf (deepest) node of this path
    path  = path.split("/")
    curr_node = self.root
    last_url  = path[-1]

    for url in path:
      if url != "":
        if not url in curr_node.children:
          curr_node.insert(url, "not found handler")
        curr_node = curr_node.children[url]

    curr_node.handler = handler
    curr_node.is_path = True


  def find(self, suffix=""):
    # Starting at the root, navigate the Trie to find a match for this path
    # Return the handler for a match, or None for no match
    curr_node = self.root
    
    #-->basic condation
    if suffix == "/":
      return curr_node.handler
    
    suffix  = suffix.split("/")

    for sufix in suffix:
      if sufix != "":
        if not sufix in curr_node.children:
          return "not found handler"
        curr_node = curr_node.children[sufix]
    
    return curr_node.handler

    

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
  def __init__(self, val=None, handler=None):
    # Initialize the node with children as before, plus a handler
    self.val      = val
    self.children = {}
    self.handler  = handler
    self.is_path  = False

  def insert(self, val, handler):
    # Insert the node as before
    self.children[val]  = RouteTrieNode(val, handler)



# The Router class will wrap the Trie and handle 
class Router:
  def __init__(self, root_handler, no_found_handler):
    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!
    self.root               = RouteTrieNode("/", root_handler)
    self.handler            = root_handler
    self.not_found_handler  = no_found_handler

  def add_handler(self, path, handler):
    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie
    #-->defense function
    assert(isinstance(path, str)), "AssertionError"

    path  = self.split_path(path)
    curr_node = self.root

    for url in path:
      if url != "":
        if not url in curr_node.children:
          curr_node.insert(url, self.not_found_handler)
        curr_node = curr_node.children[url]
    
    curr_node.handler = handler
    curr_node.is_path = True


  def lookup(self, suffix):
    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler

    #-->defense fuction
    assert(isinstance(suffix, str)), "AssertionError"
    if suffix == "":
      return suffix

    curr_node = self.root
    if suffix == "/":
      curr_node.handler
    
    suffix  = self.split_path(suffix)

    for sufix in suffix:
      if sufix != "":
        if not sufix in curr_node.children:
          return self.not_found_handler
        curr_node = curr_node.children[sufix]
    
    return curr_node.handler


  def split_path(self, path):
    # you need to split the path into parts for 
    # both the add_handler and loopup functions,
    # so it should be placed in a function here
    return path.split("/")
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this

paths = [
    ("/home/about", "about handler"),
    ("/home/about/udacity", "udacity handler"),
]

for args in paths:
  router.add_handler(*args)  # add a route


def router_test():
  test_cases  = [#-->Edge cases
                  (None, "AssertionError"),#-->'root handler'
                  ("", ""),#-->''

                  ("/", 'root handler'),#-->'root handler'
                  ("/home", 'not found handler'),#-->'not found handler'
                  ("/home/about", 'about handler'),#-->'about handler'
                  ("/home/about/", 'about handler'),#-->'about handler'
                  ("/home/about/me", 'not found handler'),#-->'not found handler'
                  ("/home/about/udacity", "udacity handler"),#-->'udacity'
                  ("/home/about/udacity/", "udacity handler"),#-->'udacity'
                ]
  for arg , answer in test_cases:
    try:
      result = router.lookup(arg)
      if result == answer and answer != "AssertionError":
        print("Test Case is Passed !")
      else:
        print("Test case", arg, "Failed")
    except AssertionError:
      if answer == "AssertionError":
        print("Nice job! Test case {0} correctly raises AssertionError!".format(arg))
      else:
        print("Check your work! Test case {0} should not raise AssertionError!".format(arg))

router_test()
