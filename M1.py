import os.path

def read_file(str):
    with open (str,'r')as f:
        for x in f:
            print(x)

def read_dir(str):
    if os.path.isdir(str):
       for file in os.listdir(str):
           if "nmea" in file:
               read_file(file)



read_dir("c:\\")