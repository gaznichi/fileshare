from django.http.response import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import File

@api_view(['GET'])
def View(requests):
    _files = File.objects.all()
    response = []

    for i in _files:
        response.append({
            "id" : i.id,
            "file" : i.file.name
        })
    return Response(response)

@api_view(['GET'])
def GetFile(request):
    _id = request.data.get('id', -1)
    if _id == -1:
        return Response({"msg" : "Missing Data"}, status=400)

    try:
        file = File.objects.get(id = _id)
    except:
        return Response({"msg" : 'Not Found'}, status=404)
    response = FileResponse(file.file)
    return response

@api_view(['POST'])
def AddFile(request):
    _file = request.FILES.get('file')

    if _file == -1:
        return Response({"msg" : "Missing Data"}, status=400)

    newfile = File(file = _file)
    newfile.save()
    return Response('Saved')

@api_view(['POST'])
def Delete(request):
    _id = request.data.get('id')

    if _id == -1:
        return Response({"msg" : "Missing Data"}, status=400)

    try:
        id = File.objects.get(id = _id)
    except:
        return Response({"msg" : "Not Found"})
    
    id.delete()
    return Response('Deleted')