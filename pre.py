import readchar

class pre:
  def __init__(self, allocate = 10):
    self.objLines = []
    self.cursor = None
    self.memory = []

    for _ in range(allocate):
      self.memory.append(binary(0))

  def feed(self, line):
    self.line = line.strip()
    if self.line != "":
      id, args = self.line.split(" ")

      obj = cmd(id, args)
      self.objLines.append(obj)

  def launch(self):
    self.count = 0
    while self.count != len(self.objLines):
      self.cmdObj = self.objLines[self.count]

      self.count += self.objLines[self.count].countIncrease

      _ = self.cmdObj.execute(self, self.count)

      if _ == "EXIT":
        break

      if _ != None:
        self.count = _-1

class cmd:
  def __init__(self, id, arg):
    self.id = id
    self.arg = arg
    self.countIncrease = 1

  def execute(self, root, cmdCount):
    if self.id == "goto":
      if self.arg.isdigit():
        root.cursor = int(self.arg)

      if self.arg == "+":
        root.cursor += 1

      if self.arg == "-":
        root.cursor -= 1

    if self.id == "set":
      if self.arg.isdigit():
        root.memory[root.cursor] = binary(int(self.arg))

      elif not self.arg.isdigit():
        if "+" in self.arg:
          _ = self.arg.split("+")

          if _[0] == "":
            val = integer(root.memory[root.cursor]) + int(_[1])

            root.memory[root.cursor] = binary(val)

          elif _[0] != "":
            val = eval(_[0] + "+" + _[1])
            root.memory[root.cursor] = binary(val)

        if "-" in self.arg:
          _ = self.arg.split("-")

          if _[0] == "":
            val = integer(root.memory[root.cursor]) - int(_[1])

            root.memory[root.cursor] = binary(val)

          elif _[0] != ":":
            val = eval(_[0] + "-" + _[1])

            root.memory[root.cursor] = binary(val)

    if self.id == "write":
      if self.arg == "ascii":
        print(chr(integer(root.memory[root.cursor])), end="")

      if self.arg == "dec":
        print(integer(root.memory[root.cursor]))

      if self.arg == "pos":
        print(root.cursor)

    if self.id == "line":
      if self.arg.isdigit():
        return int(self.arg)

      elif not self.arg.isdigit():
        if "+" in self.arg:
          _ = self.arg.count("+")
          return int(root.count) + _

        if "-" in self.arg:
          _ = self.arg.count("-")
          return int(root.count) - _

    if self.id == "get":
      if self.arg == "input":
        _ = binary(ord(readchar.readchar()))
        root.memory[root.cursor] = _

      if self.arg == "pos":
        _ = binary(int(root.cursor))
        root.memory[root.cursor] = _

    if self.id == "move":
      from_ = int(self.arg)
      
      root.memory[root.cursor] = root.memory[from_]

      root.memory[from_] = 0

    if self.id == "if":
      cell1, oper, cell2, line = self.arg.split("_")

      cell1 = str(integer(root.memory[int(cell1)]))
      cell2 = str(integer(root.memory[int(cell2)]))

      _ = str(cell1 + oper + cell2)

      if eval(_): #if condition is true
        if not line.isdigit():
          if "+" in line:
            _ = line.count("+")
            return root.count + _

          if "-" in line:
            _ = line.count("-")
            return root.count - _

        if line.isdigit():
          return int(line)

    if self.id == "end":
      return "EXIT"

class errors:
  argErr = "error, line {}. the id ({}) requires {} arguments"

def binary(num):
  return int(format(num, "b"))

def integer(num):
  return int(str(num), 2)