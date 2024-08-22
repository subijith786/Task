#1
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)

#2
# lst1=[1,6,4,7,8,-2,5,-3]
# for i in lst1:
#     if i<0:
#         break
#     print(i)

#3
# a=0
# while a<10:
#     a+=1
#     if a%2!=0:
#         continue
#     print(a)

#4
# lst=[2,5,6,-2,4,-7]
# c=0
# for i in lst:
#     if i<0:
#         continue
#     else:
#         c+=i
# print(c)

#5
# for i in range(1,11):
#     if i%2==0:
#         pass
#     else:
#         print(i)

#6
#if greater than 10
# def greater(lst):
#
#     for i in lst:
#          if i>10:
#             print(i,"is greater than 10")
#             break
#          print(i)
# lst=[2,6,5,2,7,20,4,3]
# greater(lst)
# #

#7
# str1=['a','abc','defg','hi','jkl']
# for i in str1:
#     if len(i)<3:
#         continue
#     print(i)

#8
#
# def less_than_five(lst):
#     for i in lst:
#         if i<5:
#             continue
#         print(i)
# lst1=[2,3,10,14,3,7,9,5]
# less_than_five(lst1)

#9
# lst1=[2,5,6,4,7]
# lst2=[1,5,7,9]
# c=0
# for i in lst1:
#     for j in lst2:
#         if (i*j)>10:
#             print((i,j))
#             c+=1
#             break
#         else:
#             continue
#     if c==1:
#         break

#10
words=['apple','banana','cherry','date','elderberry']
skip_words=["banana",'date']
for i in words:
    if i in skip_words:
        continue
    print(i)