from django.db.models import Q
from django.shortcuts import render
from rest_framework import filters, viewsets
from rest_framework.response import Response

from productReviewSearch.models import Product
from productReviewSearch.serializers import ProductSerializer
from django_filters.rest_framework.backends import DjangoFilterBackend
from django.views.generic import TemplateView,ListView
from .models import *
from rest_framework.decorators import api_view
# Create you views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def home(request):
    return render(request, 'home.html', {})


def search_results(request):
    if request.method == "POST":
        return render(request, 'search_results.html', {})
    else:
        return render(request, 'search_results.html', {})


@api_view(['POST'])
def search_product(request):
    products = Product.objects.filter(score=request.data['score'], helpfulness=request.data['helpfulness'])
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


'''@api_view(['POST'])
def search_product(request):
    """Search function"""

    if request.method == "POST":
        query_name = request.POST.get('reviewText', None)
        if query_name:
            results = Product.objects.filter(
                Q(reviewText__contains=query_name) |
                Q(score__icontains=query_name) |
                Q(helpfulness__icontains=query_name)
            )
            return render(request, 'search_results.html', {"results": results})

    return render(request, 'search_results')'''
