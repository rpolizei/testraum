# an example script that does nothing except printing the location of the git repository
import os

repoDir = os.cwd()
user = os.getlogin()
print("hi {}!".format(user))
print("repository is located in {}".format(repoDir))
