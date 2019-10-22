num=[]
num_len=0
for i in range(100):
       if i>1:
          t=0
          for j in num:
            if i%j==0:
             t+=1
           if t==0:
             num_len+=1
             num.insert(num_len,i)
print(num)
