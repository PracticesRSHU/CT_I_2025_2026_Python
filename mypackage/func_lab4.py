def suma_number(*numbers):
    s=0
    for number in numbers:
        s+=number
    return s

def info_user(login, email, age): #параметри
    print(f"Info user:\nlogin: {login}\nemail: {email}\nage: {age}")


def  hello():
    print("Hello, my friend!!!")

if __name__=="__main__":
    print("Tets")
    hello()