# _*_ coding: utf-8 _*_
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.views import generic


# Create your views here.
class Index(generic.TemplateView):
	template_name = 'core/index.html'
        def get_context_data(self, **kwargs):
            context = super(Index, self).get_context_data(**kwargs)
            return context

class AboutView(generic.TemplateView):
	template_name = 'core/about.html'
        def get_context_data(self, **kwargs):
            context = super(AboutView, self).get_context_data(**kwargs)
            return context

class ProductView(generic.TemplateView):
	template_name = 'core/product.html'
        def get_context_data(self, **kwargs):
            context = super(ProductView, self).get_context_data(**kwargs)
            return context

class BlogDetailView(generic.TemplateView):
	template_name = 'core/blogdetail.html'
        def get_context_data(self, **kwargs):
            context = super(BlogDetailView, self).get_context_data(**kwargs)
            return context
