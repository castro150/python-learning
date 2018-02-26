import glob2
import datetime


file_names = glob2.glob("*.txt")
print(file_names)

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in file_names:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")
