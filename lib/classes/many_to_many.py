
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class.")
        new_article = Article(self, magazine, title)
        if new_article not in self._articles:
         self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        
        
        author_count = {}
        for article in self._articles:
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1
        return [author for author, count in author_count.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles()))


class Article:
    all = []  # Class attribute to store all articles

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author class.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        self._title = title
        self._author = author
        self._magazine = magazine
        
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an instance of Author class.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class.")
        self._magazine = new_magazine