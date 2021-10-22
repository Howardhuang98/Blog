import matplotlib.pyplot as plt
import numpy as  np

"""
旅行商问题类
"""
dico = dict()
dico['a'] = {'x': 0, 'y': 0}
dico['b'] = {'x': 1, 'y': 0}
dico['c'] = {'x': 2, 'y': 0}
dico['d'] = {'x': 3, 'y': 0}
dico['e'] = {'x': 4, 'y': 0}
dico['f'] = {'x': 5, 'y': 0}
dico['g'] = {'x': 6, 'y': 0}
dico['h'] = {'x': 6, 'y': 30.0}


class TSP:
    """
    旅行商问题类
    """

    def __init__(self, locations_data: dict = dico):
        self.locations_data = locations_data
        self.route = np.random.permutation(list(self.locations_data.keys()))

    def distance(self, route):
        """

        :param pair_list:
        :return:
        """
        distance = 0  # 初始化距离
        for i in range(len(route) - 1):
            distance_between_cities = (self.locations_data[route[i]]['x'] - self.locations_data[route[i + 1]][
                'x']) ** 2 + (self.locations_data[route[i]]['y'] - self.locations_data[route[i + 1]]['y']) ** 2
            distance += distance_between_cities
        return distance


class SA:
    def __init__(self, itermax=10e3, temperature=800, K=0.99):
        self.itermax = itermax
        self.temperature = temperature
        self.K = K
        self.history = []

    def probability_of_accept(self, loss, temp):
        return np.exp(-loss / temp)

    def run_TSP(self):
        tsp = TSP()
        it_num = 0
        while it_num < self.itermax and self.temperature > 1e-5:
            it_num += 1

            self.temperature = self.K * self.temperature
            current_value = tsp.distance(tsp.route)
            self.history.append(current_value)
            new_route = np.random.permutation(tsp.route)
            new_value = tsp.distance(new_route)

            loss = new_value - current_value

            if loss < 0:
                tsp.route = new_route
                print("第{}次迭代，距离为{},loss为{},此时温度为{}".format(it_num, current_value, loss, self.temperature))
            else:
                probability = self.probability_of_accept(loss, self.temperature)
                if np.random.rand() > probability:
                    continue
                else:
                    tsp.route = new_route
                    print("第{}次迭代，距离为{},loss为{},此时温度为{}".format(it_num, current_value, loss, self.temperature))

        print(tsp.route)

    def display(self):
        plt.figure()
        y = self.history
        x = np.arange(0, len(y))
        plt.plot(x, y)
        plt.ylabel("loss")
        plt.show()




if __name__ == '__main__':
    sa = SA()
    sa.run_TSP()
    sa.display()
