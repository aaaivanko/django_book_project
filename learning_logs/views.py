from django.shortcuts import render
from .models import Topic, Entry


def index(request):
    """Main page"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    all_topics = Topic.objects.order_by('date_added')
    context = {'all_topics': all_topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show single topic per page"""
    single_topic = Topic.objects.get(id=topic_id)
    entries = single_topic.entry_set.order_by('-date_added')
    context = {'single_topic': single_topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
