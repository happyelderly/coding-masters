#########################################  Python #################################################
#중급-31. 예쁜수
n=input()
tmp=False
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if int(n)%int(n[i:j])==0:
            tmp=True
    if tmp: break
print('YES' if tmp else 'NO')
#중급-32. 
#중급-33. 
#중급-34. 
#중급-35. 
#중급-36. 
#중급-37. 
#중급-38. 
#중급-39. 
#중급-40. 