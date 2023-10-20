emails = ["oogo001@gmail.com", "clarissa002@gmail.com", "geehena003@hmail.co", "jay004@gmail.com", "jek005@gmail.com"]
email_test = []
symbols = "@"
domains = ["gmail.com", "yahoo.com", "hotmail.com", "yahoo.co.za"]

# METHOD 1 - Using this method, you will only use "symbols" and "domains" from the global variable so you can comment
# on the other global variables while using this. Manually type in the email you need to confirm
# def checkMail (email):
#     if symbols in email: 
#         print("True") 
#         for domain in domains: 
#             if domain in email: 
#                 print("True")
#                 break
#         else:
#             print("False")

# checkMail("ava@gmail.co")


# METHOD 2 - Using this method, you will use all the global variables list. The list can be edited to list to your 
# preference
def ok():
    for email in emails: 
        if symbols in email: 
            for domain in domains:
                if domain in email: 
                    email_test.append(email)
                    print ("True")
                    break
            else: 
                print("False")  
    print ("Valid Emails:", email_test)
ok()

