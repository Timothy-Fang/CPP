import os
class GetPath:
    def get_path(self,path):
        r=os.path.abspath(path)
        return r
if __name__ == '__main__':
    a=GetPath().get_path('./Python')
    print(a)