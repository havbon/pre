import compiler_win

def main():
  import pre
  with open("first.pre") as file:
    pre = pre.pre(50)
    for line in file.readlines():
      pre.feed(line)

    pre.launch()

compiler_win.compile(main)