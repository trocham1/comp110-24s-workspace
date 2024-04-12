"""Pratice writing a class."""

class Profile:

    #  Attributes below.
    username: str
    private: bool

    #  This is the constructor.
    def __init__(self, username_input: str):
        """Creat a new Profile class."""
        self.username = username_input
        self.private = True

    #  This is a method. It belong to the class.
    def tweet(self, msg:str) -> None:
        """If profile is public, print msg."""
        if self.private is False:  # not self.private
            print(msg)
    
#  Instantiation
user1: Profile = Profile("110_rulez")  # this calls the __init__
user1.private = False
user1.tweet("OOP is cool!")
