"""Imports for haustack search for protune."""
import datetime
from haystack import indexes
from hostel.models import QueryH


class QueryHIndex(indexes.SearchIndex, indexes.Indexable):
    """Index the students query for search."""

    text = indexes.CharField(document=True, use_template=True)
    created_at = indexes.DateTimeField(model_attr='created_at')
    content = indexes.CharField(model_attr='content')
    tags = indexes.MultiValueField()

    def get_model(self):
        """Method to get model for index."""
        return QueryH

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())

    def prepare_tags(self, obj):
        """Index query tags for search."""
        return [tag.name for tag in obj.tags.all()]
