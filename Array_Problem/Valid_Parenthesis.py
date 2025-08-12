#Example 1:Valid  Parenthesis Leet Code 20
def ValidParenthesis(s):
    Result=[]
    for bracket in s:
        if (bracket =="(" or bracket=="{" or bracket=="["):
            Result.append(bracket)
        else:
            if len(Result)==0:
                return False
            e=Result.pop()
            if ( bracket ==")" and e=="(") or (bracket =="}" and e=="{" ) or (bracket=="]" and e=="["):
                continue
            else:
                return False
    return len(Result)==0
print(ValidParenthesis("{[]}"))