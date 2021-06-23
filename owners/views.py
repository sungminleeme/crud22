# python 내장 라이브러리
import json

# 외부 라이브러리
from django.http  import JsonResponse
from django.views import View

# Custom 해서 만든 모듈 또는 페키지
from .models import Owner, Dog

class OwnerListView(View):
    def post(self, request):
        data = json.loads(request.body)

        Owner.objects.create(
            name  = data['name'],
            email = data['email'],
            age   = data['age']
        )

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        result = []

        for owner in owners:
            result.append(
                {
                    "owner" : {
                        "name"  : owner.name,
                        "email" : owner.email,
			"age"   : owner.age,
                        "dogs"  : [{
                            "name" : dog.name, 
                            "age" : dog.age
                        } for dog in owner.dog_set.all()]
                    }
                }
            )

        return JsonResponse({'result': result}, status=200)

##### 2nd list comphrehension

#        result = [
#            {
#                "owner" : {
#                    "name"  : owner.name,
#                    "email" : owner.email,
#                    "age"   : owner.age,
#                    "dogs"  : [{
#                        "name" : dog.name, 
#                        "age" : dog.age
#                    } for dog in owner.dog_set.all()]
#                }
#            }
#        ]
#


class DogListView(View):
    def post(self, request):
        """
        INPUT : owner_id, dog_name, dog_age
        """
        data  = json.loads(request.body)

        Dog.objects.create(
            name     = data['dog_name'],
            age      = data['dog_age'],
            owner_id = data['owner_id']
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
