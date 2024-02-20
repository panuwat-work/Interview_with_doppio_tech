from locust import HttpUser, task, between

# Thank for free API from Swagger

class MyUser1(HttpUser):
    wait_time = between(1, 2)
    host = 'https://reqres.in'

    @task
    def call_api(self):
        self.get_api_endpoint() #get api endpoint
        self.create_use_api()   #post api endpoint
        self.update_user()  #put api endpoint
        self.patch_user()   #patch api endpoint
        self.delete_user()  #delete api endpoint

    def get_api_endpoint(self):
        self.client.get('/api/users?page=2', name='LIST USERS (get)')

    def create_use_api(self):
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        self.client.post('/api/users', json=payload, name='CREATE USER (post)')

    def update_user(self):
        payload = {
            "name": "morpheus",
            "job": "zion resident"
        }
        self.client.put('/api/users/2', json=payload, name='UPDATE USER (put)')

    def patch_user(self):
        payload = {
            "name": "morpheus",
            "job": "zion resident"
        }
        self.client.patch('/api/users/2', json=payload, name='PATCH USER (patch)')

    def delete_user(self):
        self.client.delete('/api/users/2', name='DELETE USER (delete)')
