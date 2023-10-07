#1.valid checking parantheses
def Is_balanced(expression):
    stack=[]
    for char in expression:
        if char in ["(","{","["]:
            stack.append(char)
        elif char in [")","}","]"]:
            if not stack:
                return False
            top =stack.pop()
            if (char==")" and top!="(") or \
                (char=="}" and top!="{") or \
                (char=="]" and top!="["):
                return False
    return len(stack)==0 # or True 
expression=input()
print(Is_balanced(expression))

#2.order checking parantheses
def printParenthesis(str, pos, n,open, close):
#print(str,pos,n,open,close)
    if(close == n):
        for i in str:
            print(i, end="")
        print()
    else:
        if(open > close):
            str[pos] = ')'
            printParenthesis(str, pos + 1, n,open, close + 1)
        if(open < n):
            str[pos] = '('
            printParenthesis(str, pos + 1, n,open + 1, close)


n =int(input())
str =[""] * 2 * n
printParenthesis(str, 0,n,0,0)