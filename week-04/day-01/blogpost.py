# Create a BlogPost class that has
# an author_name
# a title
# a text
# a publication_date
# Create a few blog post objects:
# "Lorem Ipsum" titled by John Doe posted at "2000.05.04."
# Lorem ipsum dolor sit amet.
# "Wait but why" titled by Tim Urban posted at "2010.10.10."
# A popular long-form, stick-figure-illustrated blog about almost everything.
# "One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
# Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. 
# When I asked to take his picture outside one of IBM’s New York City offices, 
# he told me that he wasn’t really into the whole organizer profile thing.

class BlogPost(object):
    
    def __init__(self, author_name, title, text, publication_date):
        self.author_name = author_name
        self.title = title
        self.text = text
        self.publication_date = publication_date

blogpost1 = BlogPost("John Doe", "Lorem Ipsum", "Lorem ipsum dolor sit amet.","2000.05.04.")
blogpost2 = BlogPost("John Doe", "Wait but why", "A popular long-form, \
                     stick-figure-illustrated blog about almost everything.", "2010.10.10.")
blogpost3 = BlogPost("William Turton", "One Engineer Is Trying to Get IBM to Reckon With Trump", \
                     "When I asked to take his picture outside one of IBM’s New York City offices, \
                     he told me that he wasn’t really into the whole organizer profile thing.","2017.03.28.")



print(blogpost1.title, blogpost1.text)

