"""Imports for self Haystack Search."""
import datetime
from haystack import indexes
from vtr.models import QueryS


class QuerySIndex(indexes.SearchIndex, indexes.Indexable):
    """this class create index for student query."""

    text = indexes.CharField(document=True, use_template=True)
    created_at = indexes.DateTimeField(model_attr='created_at')
    content = indexes.CharField(model_attr='content')
    tags = indexes.MultiValueField()
    branch = indexes.CharField(model_attr='branch')

    def get_model(self):
        """Method is used for models."""
        return QueryS

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())

    def prepare_tags(self, obj):
        """Method to index tag reated to query."""
        return [tag.name for tag in obj.tags.all()]
