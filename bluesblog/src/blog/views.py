# from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponseForbidden
from django.utils.text import slugify
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from blog.forms import BlogForm
from blog.models import Blog

class NewBlogView(CreateView):
	form_class = BlogForm
	template_name = 'blog_settings.html'

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		user = request.user
		if Blog.objects.filter(owner=user).exists():
			return HttpResponseForbidden('You can not create more than one blog per person')
		else:
			return super(NewBlogView, self).dispatch(request,*args, **kwargs)

	def form_valid(self, form):
		blog_obj = form.save(commit=False)
		blog_obj.owner = self.request.user
		blog_obj.slug = slugify(blog_obj.title)

		blog_obj.save()
		return HttpResponseRedirect(reverse('home'))

class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		ctx = super(HomeView, self).get_context_data(**kwargs)

		if self.request.user.is_authenticated():
			ctx['has_blog'] = Blog.objects.filter(owner=self.request.user).exists()

		return ctx
