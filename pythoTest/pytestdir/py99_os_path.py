import os


def mkdirs(path):
    path = os.path.dirname(path)
    if not os.path.exists(path):
        os.makedirs(path)

print(os.path.dirname("/a/b/c.ctx"))    #/a/b
print(os.path.basename("/a/b/c.ctx"))   #c.ctx
print(os.path.splitext("c.ctx")[0])     #c


