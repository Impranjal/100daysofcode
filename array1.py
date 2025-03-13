def new_prog(op):
    X=0
    for i in op:
        
        if i in ["++X","X++"]:
            X += 1
            
        elif i in ["X--","--X"]:
            X = X-1
            
    return X

op = ['--X','X++',"++X"]
print(new_prog(op))
