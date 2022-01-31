import os
from builtins import filter

src_schema = 'Vehicle'
dest_schema = 'Auth'
src_path = 'c:/GIT/MLFF/' + src_schema
dest_path = 'c:/GIT/MLFF/' + dest_schema
repl_from = 'vehicle'
repl_to ='auth'


def create_dest_file(old_name, new_name):
    with open(old_name, 'r', encoding='utf-8') as oldf:
        with open(new_name, 'w', encoding='utf-8') as newf:
            for line in oldf:
                newline = line.replace(repl_from, repl_to).\
                     replace(repl_from.upper(), repl_to.upper())
                newf.write(newline)

def listdir(path, level):
    #if level < 40:
        for filename in [f for f in os.listdir(path) if f != '.git']:
            f = os.path.join(path, filename)
            print('  ' * level, end='')
            print(f)
            new_name = f.replace(src_schema, dest_schema).replace(repl_from, repl_to)
            if os.path.isdir(f):
                os.mkdir(new_name)
                listdir(os.path.join(path, filename), level + 1)
            else:
                create_dest_file(f, new_name)


def replace_file_names():
    listdir(src_path,0)

if __name__ == '__main__':
    replace_file_names()
