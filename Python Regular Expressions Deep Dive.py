# Objective: The aim of this assignment is to deepen your practical skills in Python's regular expressions, enhancing your ability to process and manipulate text data. 
# You will tackle a variety of real-world scenarios, applying regex to extract, validate, and transform text effectively.
# Task 1: Email Extraction Enhancement
# Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g., '[exclude.com](http://exclude.com/)').
# Modify the script to extract all email addresses except those from the specified domain.
# Code Example:
# import re
# text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
# emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
# print(emails)
# Adapt the regex pattern to exclude email addresses from '[exclude.com](http://exclude.com/)'.
# Ensure the script still extracts all other valid email addresses. 

welcome = " welcome to the email extraction program"
print(welcome.upper())
continue_or_not = input("Do you want to continue? Enter 'yes' or 'no': ").lower()
if continue_or_not == 'no':
    print("Goodbye!")
    exit()
else:
    print("Let's continue!")
to_do = " using an example, we will extract email addresses from a text but exclude certain domains"
print(to_do.upper())
this_is_the_text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
print(this_is_the_text)
print("The email addresses extracted are:")
def email_extraction():
    import re
    text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
    emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
    print(emails)
    for email in emails:
        if 'exclude.com' in email:
            emails.remove(email)
email_extraction()
keep_extracting = input("Do you want to extract more email addresses? Enter 'yes' or 'no': ").lower()
if keep_extracting == 'no':
    print("Goodbye!")
    exit()
else:
    print("Let's continue!")

def email_extraction():
    import re
    text = "Emails: [exclude.com](http://exclude.com/)"
    emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
    print(emails)
    for email in emails:
        if 'exclude.com' in email:
            emails.remove(email)
email_extraction()


