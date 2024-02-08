#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    list2=word[:]
    reversed_list=reversed(list2)

    joined_list1="".join(word)
    joined_list2="".join(reversed_list)
    
    if joined_list1==joined_list2:
        return True
    else:
        return False                 
if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE
    u_input=input()
    if u_input==" ":
        print("False")
    else:
        u_list=list(u_input)
        print(palindrome(u_list))
        
#take the u_input list, copy it and flip it in palindrome, then compare the two. If they are palindromes than they will equal True. 
#If not they will be false, whitespace should not count.