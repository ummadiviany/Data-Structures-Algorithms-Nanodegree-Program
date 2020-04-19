import os

def find_files(suffix, path):

    if os.path.isdir(path):
        
        for file in os.listdir(path):

            filepath=os.path.join(path,file)
            
            if os.path.isfile(filepath):
                
                if filepath.endswith(suffix):

                    print(filepath)
            else:

                find_files(suffix,filepath)

    return None

suffix=".c"
dir="./testdir"

print("Files ending with <"+suffix +"> are:")

find_files(suffix,dir)

#Expected Output
#./testdir/subdir1/a.c
#./testdir/subdir3/subsubdir1/b.c
#./testdir/subdir5/a.c
#./testdir/t1.c
