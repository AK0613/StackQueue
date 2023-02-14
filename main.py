# Given a string containing only parentheses, determine if it is valid. The string is valid if all parentheses close
# Test cases
# "{ ( [ ] ) }" All open and close properly
# " " Also valid
# " { [] () }" valid!
# "{ ( [] ) ]" Not valid
# "{ ( [ ) ] }" Still not valid
# "( [ ] " False
# " { [ ( ] ) } " Not valid since they are not contiguous
# Constraints - True if empty


def is_valid(string):
    stack = []
    valid = False
    if len(string) > 0:
        for char in string:
            if char == '{' or char == '[' or char == '(':
                stack.append(char)

            elif char == '}' or char == ']' or char == ')':
                if len(stack) > 0:
                    temp = stack.pop()
                    valid = compare(temp, char)
                    if not valid:
                        return valid
                    else:
                        valid = True
                else:
                    return False
        if len(stack) > 0:  # If there are elements in the stack after finding all the closing brackets
            valid = False
        return valid
    elif len(string) == 1:
        return False
    elif len(string) == 0:
        return True


def compare(opening, closing):
    if opening == '{' and closing == '}':
        return True
    elif opening == '[' and closing == ']':
        return True
    elif opening == '(' and closing == ')':
        return True
    else:
        return False


string = "[]}"
print(is_valid(string))
