#Create a function student_info(**kwargs) that prints all key–value pairs in this format:
def student_info(**kwargs):
    for (key,value) in kwargs.items():
        print(key,"-",value)
student_info(India= "Delhi",Srilanka = "Colombo",Nepal = "Khatmandu")