import copy
import random

class Hat:
    def __init__(self, **balls_input):
        self.contents = []
        for color, quantity in balls_input.items():
            for i in range(quantity):
                self.contents.append(color)

    def draw(self, quantity): #Devuelve lista con escogidos
        if quantity >= len(self.contents):
            return self.contents
        else:
            random_pick = []
            for i in range(quantity):
                random_pick.append(random.choice(self.contents))
                self.contents.remove(random_pick[i])
            return random_pick

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    i = 0
    M = 0
    while i < num_experiments:
        testing_hat = copy.deepcopy(hat)
        picked_list = testing_hat.draw(num_balls_drawn)
        picked_dict = dict()
        for j in picked_list:
            picked_dict[j] = picked_dict.get(j, 0) + 1

        inside = True
        for k_exp, v_exp in expected_balls.items():
            picked_value = picked_dict.get(k_exp)
            if picked_value == None or v_exp > picked_value:
                inside = False
                break

        if inside == True:
            M = M + 1

        i += 1

    return M / num_experiments






a1 = Hat(yellow=3, blue=2, green=6)
print(experiment(a1, {"yellow":2, "blue":1}, 4, 10000))
