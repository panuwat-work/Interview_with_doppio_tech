from locust import HttpUser, task, between

# Thank for free API from Swagger

class MyUser1(HttpUser):
    wait_time = between(1, 2)
    host = 'https://petstore.swagger.io/#/pet'

    @task
    def get_api1(self):
        self.get_api1_endpoint()

    def get_api1_endpoint(self):
        self.client.get('/findPetsByStatus', name='pet (post)')
        self.client.get('/findPetsByStatus', name='findPetsByStatus (get)')
        self.client.get('/store/placeOrder', name='placeOrder (post)')
        self.client.get('/store/getInventory', name='getInventory (get)')
        self.client.get('/user/createUsersWithArrayInput', name='createUsersWithArray (post)')


#locust -f locust_demo.py