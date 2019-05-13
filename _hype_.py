#setting hyperparameter
class Hyperparameter():
    
    def __init__(self):
        self.number_steps = 1000
        self.episode_lenght = 1000
        self.learning_rate = 0.02
        self.number_directions = 16
        self.number_best_directions = 16
        assert self.number_best_directions <= self.number_directions
        self.noise = 0.03
        self.seed = 1
        self.enviroment_name = ''
