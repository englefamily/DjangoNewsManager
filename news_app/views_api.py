from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import NewsPost
from .serializers import PostSerializer


# @api_view(['GET', 'POST']) # using our serialiser
# def list_post(req):
#     # posts = NewsPost.objects.all()
#     if req.method == "GET":
#         return Response({'msg': 'You requested a GET request'})
#     else:
#         return Response({'You requested': req.data})


@api_view(['GET', 'POST', 'PUT']) # using the REST framework serializer
def list_post(req):

    if req.method == "GET":
        post_id = req.query_params.get("post_id")
        posts = NewsPost.objects.get(pk=post_id)
        ps = PostSerializer(posts)
        return Response(ps.data)
    elif req.method == 'POST':
        ps = PostSerializer(data=req.data)
        if ps.is_valid():
            ps.save()
            # return Response({'You sent': req.data}) # temporary
            return Response("Objected Created")
        else:
            return Response({"Error": ps.errors})
    else:
        # update
        post_id = req.query_params.get("post_id")
        post_instance = NewsPost.objects.get(pk=post_id)
        ps = ps = PostSerializer(data=req.data)
        if ps.is_valid():
            ps.save()
            return Response("Objected Created")
        else:
            return Response({"Error": ps.errors})
