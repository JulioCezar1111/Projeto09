# let`s create a class for netflix client
class Client:
    def __init__(self, name, email, plan):
        self.name = name
        self.email = email
        self.plans = ['basic', 'premium']

        if plan in self.plans:
            self.plan = plan
        else:
            raise Exception('Plan  invalid') # condicionamento de erro

    def change_plan(self, new_plan):
        if new_plan in self.plans:
            self.plan = new_plan
        else:
            print('Plan invalid')

    def movie(self, movie, plan_movie):
        if self.plan == plan_movie:
           print(f'Watch movie {movie}')
        elif self.plan == 'premium':
            print(f'Watch movie{movie}')
        elif self.plan == 'basic' and plan_movie == 'premium':
            print('Upgrade to premium to see this movie')
        else:
            print('Plan invalid')


client = Client('julio', 'julio.com', 'basic')
print(client.plan)
client.movie('Harry Potter', 'premium')
client.change_plan('premium')
print(client.plan)
client.movie('Harry Potter', 'premium')