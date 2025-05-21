from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required, user_passes_test
from .models import Post, DateGeografice,DateHidrografice,DateBiodiversitate,DateForestiere,DateSpeologice,Discussion,Comment, Message, Petition,Signature
from .forms import DiscussionForm, CommentForm, SignatureForm
from django.contrib.auth.views import LoginView
from django.contrib.sessions.models import Session
from .models import ArieNaturala
from .models import Post

def posts_list(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'eenvironmentblog/posts_list.html', {'posts': posts})

def index(request):
   # posts = Post.objects.all().order_by('-created_on')
    return render(request, 'eenvironmentblog/index.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'eenvironmentblog/post_detail.html', {'post': post})

def date_geografice_detail(request, pk):
    date_geografice = get_object_or_404(DateGeografice, arie_naturala__pk=pk)
    return render(request, 'eenvironmentblog/dategeografice_detail.html', {'date_geografice': date_geografice, 'arie_naturala': date_geografice.arie_naturala})
def date_hidrografice_detail(request, pk):
    date_hidrografice = get_object_or_404(DateHidrografice, arie_naturala__pk=pk)
    return render(request, 'eenvironmentblog/datehidrografice_detail.html', {'date_hidrografice': date_hidrografice, 'arie_naturala': date_hidrografice.arie_naturala})
def date_speologice_detail(request, pk):
    date_speologice = get_object_or_404(DateSpeologice, arie_naturala__pk=pk)
    return render(request, 'eenvironmentblog/datespeologice_detail.html', {'date_speologice': date_speologice, 'arie_naturala': date_speologice.arie_naturala})
def date_forestiere_detail(request, pk):
    date_forestiere = get_object_or_404(DateForestiere, arie_naturala__pk=pk)
    return render(request, 'eenvironmentblog/dateforestiere_detail.html', {'date_forestiere': date_forestiere, 'arie_naturala': date_forestiere.arie_naturala})
def date_biodiversitate_detail(request, pk):
    date_biodiversitate = get_object_or_404(DateBiodiversitate, arie_naturala__pk=pk)
    return render(request, 'eenvironmentblog/datebiodiversitate_detail.html', {'date_biodiversitate': date_biodiversitate, 'arie_naturala': date_biodiversitate.arie_naturala})

def discussion_list(request):
    discussions = Discussion.objects.all()
    return render(request, 'eenvironmentblog/discussion_list.html', {'discussions': discussions})

def discussion_detail(request, discussion_id):
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    return render(request, 'eenvironmentblog/discussion_detail.html', {'discussion': discussion})

@login_required
def new_discussion(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.created_by = request.user
            discussion.save()
            return redirect('discussion_detail', discussion_id=discussion.pk)
    else:
        form = DiscussionForm()
    return render(request, 'eenvironmentblog/new_discussion.html', {'form': form})

@login_required
def add_comment(request, discussion_id):
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.discussion = discussion
            comment.created_by = request.user
            comment.save()
            return redirect('discussion_detail', discussion_id=discussion.pk)
    else:
        form = CommentForm()
    return render(request, 'eenvironmentblog/add_comment.html', {'form': form})


class CustomLoginView(LoginView):
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url and next_url != self.request.path_info:
            self.request.session['login_redirect_url'] = next_url

        return super().get_success_url()

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user.is_superuser:
        comment.delete()
    return redirect('discussion_detail', discussion_id=comment.discussion.id)


@login_required
def delete_discussion(request, discussion_id):
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    if request.user.is_superuser:
        discussion.delete()
    return redirect('discussion_list')

def chat(request):
    messages = Message.objects.all()
    return render(request, 'eenvironmentblog/chat.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            message = Message(user=request.user, content=content)
            message.save()
    return redirect('chat')


@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.user.is_superuser:
        message.delete()
    return redirect('chat')

def petition_detail(request, petition_id):
    petition = get_object_or_404(Petition, pk=petition_id)
    signiatures = Signature.objects.filter(petition_id=petition_id)
    if request.method == 'POST':
        form = SignatureForm(request.POST)
        if form.is_valid():
            signature = form.save(commit=False)
            signature.petition = petition
            signature.save()
            return redirect('petition_detail', petition_id=petition_id)
    else:
        form = SignatureForm()
    return render(request, 'eenvironmentblog/petition_detail.html', {'petition': petition, 'form': form, 'signiatures':signiatures})

def petition_list(request):
    petitions = Petition.objects.all()
    return render(request, 'eenvironmentblog/petition_list.html', {'petitions': petitions})

def arii_naturale_list(request):
    arii = ArieNaturala.objects.filter(status=1)
    return render(request, 'eenvironmentblog/arii_list.html', {'arii': arii})
 
 