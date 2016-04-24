import datetime
from haystack import indexes
from vtr.models import QueryS


class QuerySIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #author = indexes.CharField(model_attr='user')
    created_at = indexes.DateTimeField(model_attr='created_at')
    content = indexes.CharField(model_attr='content')
    tags = indexes.MultiValueField()

    def get_model(self):
        return QueryS

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())