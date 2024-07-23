class Article:
#initializing article and an empty array for all articles
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    #proptery of artile title

    def get_title(self):
        return self._title
    def set_title(self,value):
        if type(value) is str and 5 <= len(value) <=50 and not hasattr(self,"name"):
            self._title = value
        else:
            print("Not valid title")
    title = property(get_title,set_title)

    #getting the author of the artilcle

    def get_author(self):
        return self._author
    def set_author(self,value):
        if type(value) is Author:
            self._author = value
        else:
            print("Not valid author")
    author = property(get_author,set_author)
    
    #getting magazine of article

    def get_magazine(self):
        return self._magazine
    def set_magazine(self,value):
        if type(value) is Magazine:
            self._magazine = value
        else:
            print("Not valid magazine")
    magazine = property(get_magazine,set_magazine)
        
class Author:
#initializing author and an empty array for all authors
    all= []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

#property of name of author
    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 0 < len(value) and not hasattr(self,"name"):
            self._name = value
        else:
            print("Not valid name")
    name = property(get_name,set_name)
#getting all articles
    def articles(self):
        my_articles = []
        for article in Article.all:
            if article.author == self:
                my_articles.append(article)
        return my_articles

#returing unique list of magazines for author

    def magazines(self):
        my_magazines= []
        for article in Article.all:
            if article.author == self and article.magazine not in my_magazines:
                my_magazines.append(article.magazine)
        return my_magazines
#creaeting a magzine instance and using it's title as the argyment
    def add_article(self, magazine, title):
        return Article(
            author=self,
            magazine=magazine,
            title=title
        )      
#returning a unique list of categroies of magazines the author has written for
    def topic_areas(self):
        my_categories = []

        for article in Article.all:
            if article.author == self and article.magazine.category not in my_categories:
                my_categories.append(article.magazine.category)
        print(my_categories)
        return my_categories if my_categories else None 

        
class Magazine:
#initializing magazine and an empty array for all magazines
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    #setting property for name    

    def get_name(self):
        return self._name
    def set_name(self,value):
        if type(value) is str and 2 <= len(value) <=16:
            self._name = value
        else:
            print("Not valid name")
    name = property(get_name,set_name)

    # setting property for catogory

    def get_category(self):
        return self._category
    def set_category(self,value):
        if type(value) is str and 0 < len(value):
            self._category = value
        else:
            print("Not valid category")
    category = property(get_category,set_category)

#returning the list of all articles magazine has published
    def articles(self):
        my_articles = []
        for article in Article.all:
            if article.magazine == self:
                my_articles.append(article)
        return my_articles


    def contributors(self):
        my_contributors=[]
        for article in Article.all:
            if article.magazine == self and article.author not in my_contributors:
                my_contributors.append(article.author)
        return my_contributors

    def article_titles(self):
        titles = []

        for article in Article.all:
            if article.magazine == self:
                titles.append(article.title)

        return titles if titles else None

    def contributing_authors(self):
        author_count = {}
        for article in Article.all:
            if article.magazine == self:
                if article.author not in author_count:
                    author_count[article.author] = 0
                author_count[article.author] += 1
    
        my_contributors = [author for author, count in author_count.items() if count > 2]

        return my_contributors if my_contributors else None
#this is counting all the articles in a magazine
    def count_articles(self):
        count = 0
        for article in Article.all:
            if article.magazine == self:
                count += 1
        return count
#this is finding the magazine that has the moist articles
    @classmethod
    def top_publisher(cls):
      
        curr_max = 0
        curr_max_mag = None
        for magazine in cls.all:
            magazine_count = magazine.count_articles()
            if magazine_count > curr_max:
                curr_max = magazine_count
                curr_max_mag = magazine
        return curr_max_mag

    def __repr__(self):
        return self.name
    
