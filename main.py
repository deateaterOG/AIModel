import math


class Model:

  def __init__(self, X, y):
    self.X = X
    self.y = y

  def constraint(self, x):
    return (math.exp(2 * x) - 1) / (math.exp(2 * x) + 1)

  def evaluate(self, Xpr, abstraction):
    distances = []

    for i in self.X:
      distVal = self.distance(Xpr, i)
      distances.append(distVal)

    distancesSorted = sorted(distances)

    distancesUsed = distancesSorted[0:abstraction + 1]
    known_values = []

    indexes = []

    for i in distancesUsed:
      index = distances.index(i)

      if index in indexes:
        index = distances.index(i, index + 1)

      val = self.y[index]

      known_values.append(val)

    return self.calculate_weighted_average(known_values, distancesUsed)

  def distance(self, X1, X2):

    distsqr = 0

    for i, j in zip(X1, X2):
      valunsqr = i - j
      distsqr += pow(valunsqr, 2)

    return math.sqrt(distsqr)

  def calculate_weighted_average(self, known_values, distances):

    weights = []

    for d in distances:
      if not d == 0:
        weights.append(self.constraint(1 / (d**2)))
        continue

      weights.append(self.constraint(1 / ((0.1)**2)))

    weighted_sum = sum(w * m for w, m in zip(weights, known_values))
    total_weight = sum(weights)

    weighted_average = weighted_sum / total_weight

    return weighted_average


model = Model([[1000], [900], [700], [600], [500], [300], [210], [200]],
              [100, 90, 70, 60, 50, 30, 21, 20])

print(model.evaluate([500], 6))
