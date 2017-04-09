import os
def rename_files():
    #get all file name
    file_list = os.listdir(r"C:\Users\android\Desktop\python\prank")    
    #print(file_list)

    save_path = os.getcwd()
    #print("current dir "+save_path)
    os.chdir(r"C:\Users\android\Desktop\python\prank")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
        os.chdir(save_path)
        
rename_files()
