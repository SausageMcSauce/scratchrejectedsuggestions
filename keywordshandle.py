from tolorslist import tolorslist

def keyword_handler(selected):
  if selected in ["broadcast recieved"]:
    return tolorslist["1.1"]
  elif selected in ["when stop sign clicked"]:
    return tolorslist["1.2"]
  elif selected in ["pointing to sprite", "pointing towards sprite"]:
    return tolorslist["1.3"]
  elif selected in ["money blocks"]:
    return tolorslist["1.4"]
  else:
    return "Nothing matched what you searched. Rerun the program to try again"