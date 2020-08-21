from tolorslist import tolorslist

def keyword_handler(selected):
  if selected in ["broadcast recieved"]:
    return tolorslist["1.1"]
  elif selected in ["when stop sign clicked", "stop sign clicked"]:
    return tolorslist["1.2"]
  elif selected in ["pointing to sprite", "pointing towards sprite"]:
    return tolorslist["1.3"]
  elif selected in ["money blocks"]:
    return tolorslist["1.4"]
  elif selected in ["social action blocks", "project stats blocks"]:
    return tolorslist["1.5"]
  elif selected in ["cloud lists"]:
    return tolorslist["1.6"]
  elif selected in ["2d lists"]:
    return tolorslist["1.7"]
  elif selected in ["3d", "3d scratch"]:
    return tolorslist["1.8"]
  elif selected in ["pi", "pi block"]:
    return tolorslist["1.9"]
  else:
    return "Nothing matched what you searched. Rerun the program to try again"