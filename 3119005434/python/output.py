import os
def output(repetition, destination):
    REPETITION=str(repetition)
    filename = destination+"/output.txt"
    HERE_IS_YOUR_REPETITION="查重率为："+REPETITION
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(HERE_IS_YOUR_REPETITION)
        f.close()



