num1=int(input("enter num1 "))
num2=int(input("enter num2 "))
operator=input("choose operator: ")

def sums(num1,num2):
  sum=num1+num2
  print(sum)
def sub(num1,num2):
  sub=num1-num2
  print(sub)



def multiple(num1,num2):
   multiple=num1*num2
   print(multiple)
def div(num1,num2):
    div=num1/num2
    print(f"div= {div}")

if operator == "+":
    sums(num1, num2)
elif operator == "*":
    multiple(num1, num2)
elif operator == "/":
    div(num1,num2)
elif operator == "-":
        sub(num1, num2)