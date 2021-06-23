from random import randint

class Matrix:
  def __init__(self, rows, cols) -> None:
    self.rows = rows
    self.cols = cols
    self.matrix = []

    for i in range(self.rows):
      self.matrix.append([])
      for j in range(self.cols):
        self.matrix[i].append(0)
  
  def multiply(self, n):
    if isinstance(n, int):
      for i in range(self.rows):
        self.matrix[i]
        for j in range(self.cols):
          self.matrix[i][j] *= n
    elif isinstance(n, Matrix):
      if self.cols != n.rows:
        raise NameError("Columns of A must match rows of B.")
      result = Matrix(self.rows, n.cols)
      a = self
      b = n
      for i in range(result.rows):
        for j in range(result.cols):
          sum = 0
          for k in range(self.cols):
            sum += a.matrix[i][k] * b.matrix[k][j]
          result.matrix[i][j] = sum
      return result

  def add(self, n):
    for i in range(self.rows):
      for j in range(self.cols):
        if isinstance(n, int):
          self.matrix[i][j] += n
        elif isinstance(n, Matrix):
          self.matrix[i][j] += n[i][j]
  
  def randomize(self):
    for i in range(self.rows):
      for j in range(self.cols):
        self.matrix[i][j] += randint(0, 10)
  
  def __repr__(self):
      return str(self.__dict__)
