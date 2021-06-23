import json

from django.http import JsonResponse
from django.views import View
from .models import Owner, Dog

class OwnerListView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name=data['name'],
                            email=data['email'],
                            age=data['age'])
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        result = []

        for owner in owners:
            dogs = owner.dog_set.all()
            dog_list = []
            for dog in dogs:
                dog_info = (
                    {
                        'name': dog.name,
                        'age': dog.age
                    }
                )
                dog_list.append(dog_info)

            result.append(
                {
				'email' : owner.email,
				'name'  : owner.name,
				'age'   : owner.age,
				'my_dogs': dog_list
                }
            )

            

        return JsonResponse({'result': result}, status=200)   

class DogListView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(email=data['owner'])
        Dog.objects.create(name=data['name'],
                           age=data['age'],
                           owner=owner
        )  
        return JsonResponse({'message':'SUCCESS'}, status=201)

    
    def get(self, request):
        dogs = Dog.objects.all()
        
        result = []
        for dog in dogs:
            result.append(
            {
              'name': dog.name,
              'age': dog.age,
              'owner': dog.owner.name
            }
          )
        return JsonResponse({'MESSAGE': result}, status=200)    
                          



	



        