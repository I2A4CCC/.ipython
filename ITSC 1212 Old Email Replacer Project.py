# defining an email replacer function that takes three parameters (users email, old web-based emal, old web-based email replacer (new_email)).  
def replace_email(email, old_email, new_email):
    # creating if/else statement 
    # if the email ends with old email, assign a new variable the lenght of old email
    if email.endswith(old_email):
        lenght = len(old_email)
        # assign another variable to create the new account replacing the old email
        new_account = email[:-lenght] + email[-lenght:].replace(old_email, new_email)
        # return the new account
        return new_account
    # else dont make no changes
    return email


print(replace_email('Thebest@yahoo.com', '@yahoo.com', '@gmail.com' ))
print(replace_email('Ilovecookies@gmail.com', '@gmail.com', '@gmx.com'))
print(replace_email('Gamelover24@outlook.com', '@yandex.mail', '@outlook.com'))


