######################################################
# helps
# Python Get the last element of a list
# https://sparkbyexamples.com/python/python-get-the-last-element-of-a-list/#:~:text=In%20Python%2C%20you%20can%20get,of%201%2C%20and%20so%20on.
# Python Print Without Newline
# https://blog.enterprisedna.co/python-print-without-newline-easy-step-by-step-guide/#:~:text=To%20print%20without%20a%20new,%22)
# Python List index() & How to Find Index of an Item in a List?
# https://favtutor.com/blogs/get-list-index-python#:~:text=The%20index()%20method%20returns,index('item_name').
# Count Occurrences of Item in Python List
# https://sparkbyexamples.com/python/count-occurrences-of-element-in-python-list/#:~:text=To%20count%20the%20occurrences%20of%20an%20element%20in%20a%20list,of%20elements%20in%20a%20list.
# Python List pop()
# https://www.programiz.com/python-programming/methods/list/pop
# Python | Removing Initial word from string
# https://www.geeksforgeeks.org/python-removing-initial-word-from-string/
# How to get the first word in the string
# https://stackoverflow.com/questions/13750265/how-to-get-the-first-word-in-the-string
# How to get the substring between two markers in Python
# https://www.adamsmith.haus/python/answers/how-to-get-the-substring-between-two-markers-in-python
# Syntax of Ternary Operator
# https://www.scaler.com/topics/ternary-operator-in-python/
# Python String split() Method
# https://www.w3schools.com/python/ref_string_split.asp#:~:text=The%20split()%20method%20splits,number%20of%20elements%20plus%20one.
# Ternary Operator in Python
# https://www.geeksforgeeks.org/ternary-operator-in-python/
######################################################

def simple_evaluate_ternary_operator(ternary_string):
    assignment_varaible = ternary_string.split(' ', 1)[0]

    ternary_string = ternary_string.replace(" = ", " if ")
    removed_assignment_varaible = ternary_string.split(' ', 1)[1]
    removed_assignment_varaible = removed_assignment_varaible.replace(" ? ", f": \n \t {assignment_varaible} = ")
    removed_assignment_varaible = removed_assignment_varaible.replace(" : ", f"\n else: \n \t {assignment_varaible} = ")

    return removed_assignment_varaible

def evaluate_ternary_operator(ternary_string):
    question_marks = ternary_string.count("?")
    if question_marks == 1:
        print(simple_evaluate_ternary_operator(ternary_string))
    else:
        ternary_string_list = ternary_string.split(' ')
        assignment_varaible = ternary_string_list[0]
        ternary_string_list.pop(0)
        ternary_string_list.pop(0)
        for i in range(len(ternary_string_list)):
            if ternary_string_list[i] == "==":
                ternary_string_list[i-1] = "if " + ternary_string_list[i-1]
                if ternary_string_list[i-2] == "\n \telse: \n \t":
                    ternary_string_list[i-2] = "\nelse: \n \t"
            elif ternary_string_list[i] == "!=":
                ternary_string_list[i-1] = "if " + ternary_string_list[i-1]
                if ternary_string_list[i-2] == "\n \telse: \n \t":
                    ternary_string_list[i-2] = "\nelse: \n \t"
            elif ternary_string_list[i] == "?":
                ternary_string_list[i] = ": \n \t"
            elif ternary_string_list[i] == ":":
                ternary_string_list[i- 1] = "\t" + assignment_varaible + " = " + ternary_string_list[i- 1]
                ternary_string_list[i] = "\n \telse: \n \t"
        ternary_string_list[-1] = "\t" + assignment_varaible + " = " + ternary_string_list[-1]


        for i in range(len(ternary_string_list)):
            print(ternary_string_list[i], end="")


if __name__ == '__main__':
    ternary_user_input = input('Which Ternary operator do you want to evaluate?')
    evaluate_ternary_operator(ternary_user_input)