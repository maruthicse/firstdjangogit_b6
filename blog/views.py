from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
# Create your views here.
def post_list(request):
	# pull data base 
	# send to the template
	#posts = Post.objects.filter(published_date__lte=timezone.now())
	#posts = Post.objects.all()
	return render(request,'blog\post_list.html',{})
def post_details(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog\post_details.html',{'post':post})
def post_new(request):
	if request.method =='POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_details',pk=post.pk)
	else:
		form = PostForm()
		return render(request,'blog\post_edit.html',{'form':form})