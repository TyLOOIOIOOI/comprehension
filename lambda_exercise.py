''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''



numbered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_list_even = list(filter(lambda num:num % 2 == 0, numbered_list))

print(filtered_list_even)

filtered_list_odd = list(filter(lambda num:num % 2 != 0, numbered_list))

print(filtered_list_odd)


''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


sixletterday = list(filter(lambda num: (len(num)==6) , weekdays))
print(sixletterday)






''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''


original_list= ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_list = ['orange', 'black']
final_list = list(filter(lambda word: word not in remove_list, original_list))

print(final_list)







''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

removed_list = list(filter(lambda n : n not in list2, list1))
print(removed_list)





''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search: (find words has ack and abc in them)
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
original_list3 = ['red', 'black', 'white', 'green', 'orange']
list5 = list(filter(lambda num:("ack" in num), original_list3))
list6 = list(filter(lambda num:("abc" in num), original_list3))


print(list5)
print(list6)


''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''
Password= input("What is your password? ")

R = [lambda x: any(x.isupper()for x in Password),
        lambda x: any(x.islower()for x in Password),
        lambda x: any(x.isdigit()for x in Password),
        lambda x: len(Password) >= 8]

if all(rule(Password)for rule in R):
    print("Valid Password")
else:
    print('Invalid Password')


'''
if any(
    (
        lambda x:x is Password.islower(), Password.isdigit(), len(Password)>=8, Password,
        
    )
):

    print("Valid Password")

else: 
    print("Invalid Password")

'''



''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst.sort(key=lambda x:x[1])
print(lst)