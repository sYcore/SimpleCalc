def addition(x, y):
    result = x + y
    return result

def subtraction(x, y):
    result = x - y
    return result
    
def multiplication(x, y):
    result = x * y
    return result
    
def division(x, y):
    result = x / y
    return result

def isFloat(x):
    try:
        float(x)
    except ValueError:
        return False
    else:
        return True

def isSet(var):
    if var == None:
        return False
    else:
        return True

while True:

    var_num1 = input('Enter first number: ')
    var_num2 = input('Enter second number: ')
    operation = input('Shall I "add", "subtract", "multiply" or "divide" your numbers: ').lower()

   

    if isFloat(var_num1) == True:
        first_number = float(var_num1)
    else:
        print('INPUT ERROR in first number! Only digits allowed!')

    if isFloat(var_num2) == True:
        second_number = float(var_num2)
    else:
        print('INPUT ERROR in second number! Only digits allowed!')

    if isFloat(operation) == False:
        operator = str(operation)
    else:
        print('INPUT ERROR! Numbers are not allowed as operators.')

    if isSet(first_number) == True:
        if isSet(second_number) == True:
            if isSet(operator) == True:
        
                if operator == 'add':
                    result = addition(first_number, second_number)
                    print('Your result is:\n', result, '\n')
                    first_number = second_number = result = operator = None
                                
                elif operator == 'subtract':
                    result = subtraction(first_number, second_number)
                    print('Your result is:\n', result)
                    first_number = second_number = result = operator = None
                
                elif operator == 'multiply':
                    result = multiplication(first_number, second_number)
                    print('Your result is:\n', result)
                    first_number = second_number = result = operator = None
                
                elif operator == 'divide':
                    result = division(first_number, second_number)
                    print('Your result is:\n', result)
                    first_number = second_number = result = operator = None
                
                else:
                    print('INPUT ERROR! Unknown operator. Please check for spelling.') 
                    print('Only "add", "subtract", "multiply" and "divide" allowed!')
            else:
                print('INPUT ERROR! You forgot the operator')
        else:
            print('INPUT ERROR! You forgot to enter the second number.')
    else:
        print('INPUT ERROR! You forgot to enter the first number.')
    
   
