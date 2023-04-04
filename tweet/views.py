from django.shortcuts import render, redirect
from .models import TweetModel, TweetComment
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')


def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html', {'tweet':all_tweet})
        else:
            return redirect('/sign-in')
    elif request.method == "POST":
        user = request.user
        my_tweet = TweetModel()
        my_tweet.author = user
        my_tweet.content = request.POST.get('my-content', '')
        my_tweet.save()
        return redirect('/tweet')


@login_required
def delete_view(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')

@login_required
def tweet_detail(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    all_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    return render(request, 'tweet/tweet_detail.html', {'tweet': my_tweet, 'comment': all_comment})

@login_required
def save_comment(request, id):
    if request.method == "POST":
        comment = request.POST.get('comment', '')
        current_tweet = TweetModel.objects.get(id=id)

        tweet_comment = TweetComment()
        tweet_comment.comment = comment
        tweet_comment.tweet = current_tweet
        tweet_comment.author = request.user
        tweet_comment.save()

        return redirect('/tweet/'+str(id))


@login_required
def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/tweet/'+str(current_tweet))

