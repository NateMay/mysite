from django.shortcuts import render
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from ads.models import Ad
# Create your views here.
class AdListView(OwnerListView):
  model = Ad

class AdDetailView(OwnerDetailView):
  model = Ad

class AdCreateView(OwnerCreateView):
  model = Ad
  fields = ['text', 'title', 'price']

class AdUpdateView(OwnerUpdateView):
  model = Ad
  fields = ['text', 'title', 'price']

class AdDeleteView(OwnerDeleteView):
  model = Ad
