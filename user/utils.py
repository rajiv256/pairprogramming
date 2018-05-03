from .models import User, Topic
from github import Github
import string, random


def lower_bound(arr, prefix):
    lo = 0
    hi = len(arr)-1
    length = len(prefix)
    iter = 0
    while (lo < hi) & (iter<100):
        mid = int((lo + hi) / 2)

        if arr[mid][:length] > prefix:
            hi = mid-1
        elif arr[mid][:length] < prefix:
            lo = mid+1
        else:
            hi = mid
    iter += 1

    return lo


def upper_bound(arr, prefix):
    lo = 0
    hi = len(arr)-1
    length = len(prefix)
    iter = 0
    while (lo < hi) & (iter<100):

        mid = int((lo+hi)/2)
        if arr[mid][:length] > prefix:
            hi = mid - 1
        elif arr[mid][:length] < prefix:
            lo = mid + 1
        else:
            lo = mid
        iter += 1

    return hi


def range(arr, prefix):
    return lower_bound(arr, prefix), upper_bound(arr, prefix)

l = ['aacdef', 'abbcddn','absdjjdk', 'abskjfej','abfkjeifi']
l.sort()
st, en = range(l, 'ab')
print(st,en)


def user_exists(user_name):

    try:
        user = User.objects.get(user_name=user_name)
    except (KeyError, User.DoesNotExist):
        return False
    return True


def create_user(user_name, github_token):

    user = User.objects.create(user_name=user_name)
    user.save()
    return


def login_user(user_name, password):

    git = None
    if user_exists(user_name):
        user = User.objects.get(user_name=user_name)
        github_token = user.user_github_token
        git = Github(github_token)
    else:
        git = Github(user_name, password)
        print(git.oauth_scopes)
        create_user(user_name, "token")

    return


def add_all_topics():
    cnt = Topic.objects.all().count()
    if cnt>0:
        print('Already added topics to DB.')
        return

    f = open('all_tags', 'r')
    l = f.readlines()
    for topic in l :
        t = Topic.objects.create(topic_title=topic.strip())
        t.save()


def matches(arr, prefix):
    st,en = range(arr, prefix)
    return arr[st:en+1]
