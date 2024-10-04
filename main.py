def calculate(s: str) -> int:
    # using stack for the parenthesis
    stack = []
    current_result = 0
    current_number = 0
    # 1 - positive, -1 - negative
    sign = 1  

    i = 0
    while i < len(s):
        ch = s[i]

        if ch.isdigit():
            # making the integer from string characters
            current_number = current_number * 10 + int(ch)
        
        elif ch == '+':
            # Apply the last number with the current sign
            current_result += sign * current_number
            current_number = 0
            # Set the new sign for the next number
            sign = 1
        
        elif ch == '-':
            # Apply the last number with the current sign
            current_result += sign * current_number
            current_number = 0
            # Set the new sign for the next number
            sign = -1
        
        elif ch == '(':
            # Push the current result and sign onto the stack
            stack.append(current_result)
            stack.append(sign)
            # Reset the result and sign for the new sub-expression
            current_result = 0
            sign = 1
        
        elif ch == ')':
            # Apply the last number in the current sub-expression
            current_result += sign * current_number
            current_number = 0
            # Pop the sign and previous result from the stack and apply
            current_result *= stack.pop() 
            current_result += stack.pop() 

        i += 1

    # Add the last number outside of parentheses (if any)
    current_result += sign * current_number
    
    return current_result


# Taking input from the user and calling the calculate function
if __name__ == "__main__":
    expression = input("Enter the mathematical expression: ")
    result = calculate(expression)
    print(f"The result is: {result}")
