class Source:
    """
    Source class for defining source objects
    """
    def __init__(self, id, name, description, url, category):

        """
        instantiating object properties
        """
        self.id = id
        self.name=name
        self.description=description
        self.url=url
        self.category = category



class Articles:
    '''
    Articles class to define articles objects
    '''
    def __init__(self,id,author,title,description,url,image,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.date = date     