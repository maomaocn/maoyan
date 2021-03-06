from haystack import indexes

from myapp.models import Book


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    """
    SKU索引数据模型类
    """
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.IntegerField(model_attr='id')
    book_type = indexes.CharField(model_attr='book_type')
    bookname = indexes.CharField(model_attr='bookname')
    def get_model(self):
        """返回建立索引的模型类"""
        return Book
    #
    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.filter(is_hot_sale=True)#这个位置加了一个筛选条件
