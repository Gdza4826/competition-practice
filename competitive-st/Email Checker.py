email_input = input("E-Mail : ")
pass_input = input("Password : ")
debug_checker_sym = 0
for i in email_input:
    if i == "@":
        debug_checker_sym += 1

if debug_checker_sym == 1:
    list_email_out = []
    list_check_email_code = email_input.split("@")
    for i in email_input:
        list_email_out.append(i)
    if list_email_out[0] == "6" and list_email_out[1] == "6":
        if len(list_check_email_code[0]) < 5:
            print("This email cannot be registered")
        elif not list_check_email_code[0].isdigit():
            print("This email cannot be registered")
        elif pass_input == email_input:
            print("Password must not be the same as email")
        else:
            if list_check_email_code[1] == 'preecha.ac.th' or list_check_email_code[1] == "kengdee.ac.th" or list_check_email_code[1] == 'samart.ac.th' and len(list_check_email_code[0]) == 5:
                if len(pass_input) >= 10:
                    print("Complete")
                else:
                    print("Password must be at least 10 characters")
            else:
                if len(pass_input) >= 10:
                    print("This email cannot be registered")
                else:
                    print("Password must be at least 10 characters")
    else:
        print("This email cannot be registered")
else:
    print("This email cannot be registered")


