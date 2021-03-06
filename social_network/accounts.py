
class User(object):
    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
        self.posts = []
        self.following=[]
    def add_post(self, post):
        self.posts.append(post)
        post.user = self

    def get_timeline(self):
        timeline = []
        for followed_user in self.following:
            timeline += followed_user.posts
        return timeline

    def follow(self, other):
        self.following.append(other)

    def __str__(self):
        pass

    def __repr__(self):
        return '<User: "'+self.first_name+" "+self.last_name+'">'
