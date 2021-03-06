from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super



@api_view(['GET','POST'])
def get_super_list(request):
    super_type_param= request.query_params.get('super_types')
    type_param = request.query_params.get('type')
    supers = Super.objects.all()
    super_heros=supers.filter(super_type__type='hero')
    super_villains=supers.filter(super_type__type='villain')
    # 1.Accepts a value from the request's URL (The id of the super to retrieve).
    # 2.Returns a 200 status code.
    # 3.Responds with the super in the database that has the id that was sent through the URL
    
    if request.method == 'GET':
        
        if type_param == 'hero':
              
            serializer = SuperSerializer(super_heros,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
            
        elif type_param=='villain':
            serializer = SuperSerializer(super_villains,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

        else:
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        
    
    # Adds the new super to the database.
    # Returns a 201 status code.
    # Responds with the newly created super object.
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def change_super(request,pk):
    
    supers = get_object_or_404(Super,pk=pk)
    # Accepts a value from the request's URL (The id of the super to be updated).
    # Accepts a body object from the request in the form of a Super model.
    # Finds the super in the Super table and updates that super with the properties that were sent in the request's body.
    # Returns a 200 status code.
    # Responds with the newly updated super object
    if request.method == 'GET':
        serializer = SuperSerializer(supers)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = SuperSerializer(supers,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

