import os

def rename_files():
    #1 stes - get files from the folder
    file_list = os.listdir(r"/Users/ione/Downloads/prank")
    print(file_list)

    saved_path = os.getcwd()
    os.chdir(r"/Users/ione/Downloads/prank")
    print ("Current directory is"+ saved_path)
    #2 step - for each file rename the filename
    for filename in file_list:
        os.rename(filename, filename.translate(None, "1234567890"))
        print("Old names"+filename)
    os.chdir(saved_path)

rename_files()
