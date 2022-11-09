# print(ord(''))
# print(ord('i'))

# char = 'list'
# for alpahbet in char:
#     print(ord(alpahbet))

# def is_power_of_two(n):

#     if n <= 0:
#         return False
#   # Check if the number can be divided by two without a remainder
#     while n % 2 == 0:
#         n = n / 2
#   # If after dividing by two the number is 1, it's a power of two
#     if n == 1:
#         return True
#     return False


# print(is_power_of_two(0))  # Should be False
# print(is_power_of_two(1))  # Should be True
# print(is_power_of_two(8))  # Should be True
# print(is_power_of_two(9))  # Should be False

# # Not quite. Remember that the goal of the function is to
# # check if a number is a power of 2. You need to fix the
# # infinite loop and still return the correct result.

# def sum(x, y):
#     return (x+y)


# print(sum(sum(1, 2), sum(3, 4)))

# def retry(operation, attempts):
#     for n in range(attempts):
#         if operation():
#             print("Attempt " + str(n) + " succeeded")
#             break
#         else:
#             print("Attempt " + str(n) + " failed")


# retry(create_user, 3)
# retry(stop_service, 5)

# def counter(start, stop):
#     x = start
#     if start > stop:
#         return_string = "Counting down: "
#         while x >= stop:
#             return_string += str(x)
#             if x != stop:
#                 return_string += ","
#             x -= 1
#     else:
#         return_string = "Counting up: "
#         while x <= stop:
#             return_string += str(x)
#             if x != stop:
#                 return_string += ","
#             x += 1
#     print(return_string)
#     return return_string


# print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1))  # Should be "Counting down: 2,1"
# print(counter(5, 5))  # Should be "Counting up: 5"

# def is_palindrome(input_string):
#     # We'll create two strings, to compare them
#     new_string = ""
#     reverse_string = ""
#     # Traverse through each letter of the input string
#     for index in range(len(input_string)):
#         print(input_string[index])
#         # Add any non-blank letters to the
#         # end of one string, and to the front
#         # of the other string.
#         if str(input_string[index]) != " ":
#             new_string = new_string + input_string[index]
#             reverse_string = input_string[index] + reverse_string
#     # Compare the strings
#     new_string = new_string.lower()
#     reverse_string = reverse_string.lower()

#     print(new_string, reverse_string)
#     if new_string == reverse_string:
#         return True
#     return False


# print(is_palindrome("Never Odd or Even"))  # Should be True
# print(is_palindrome("abc"))  # Should be False
# print(is_palindrome("kayak"))  # Should be True

# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4, "r"), (2, "w"), (1, "x")]
#     # Iterate over each of the digits in octal
#     for x in [int(n) for n in str(octal)]:
#         print(x)
#         # Check for each of the permissions values
#         for value, letter in value_letters:
#             if ___ >= value:
#                 result += ___
#                 ___ -= value
#             else:
#                 ___
#     return result


# print(octal_to_string(755))  # Should be rwxr-xr-x
# print(octal_to_string(644))  # Should be rw-r--r--
# print(octal_to_string(750))  # Should be rwxr-x---
# print(octal_to_string(600))  # Should be rw-------

def combine_lists(list1, list2):
    combined_lst = []
    # Generate a new list containing the elements of list2
    combined_lst.extend(list2)
    # Followed by the elements of list1 in reverse order
    list1.reverse()

    print(list1)
    combined_lst.extend(list1)
    return combined_lst


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
