#impoting re module
import re 
def validate_and_extract(text):
    #validation for each part of the email
    email_regex= r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,}'
    #same validations for phone numbers
    phone_regex= r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    print("\nAnalysing the text...\n")

    #search for emails
    email_match=re.search(email_regex, text)
    if email_match:
        print(f"Found email:{email_match.group()}")
    else:
        print("No valid email found")    

    #seacrch for phone numbers
    phone_match=re.search(phone_regex,text)
    if phone_match:
        print(f"Found phone number: {phone_match.group()}")
    else:
        print("No valid phone number found")   

    #more filtering fro emiasl and phone numbers
    print("\nAddtional details:")
    all_emails=re.findall(email_regex, text)
    all_phones=re.findall(phone_regex, text)
    print(f"All emails found: {all_emails if all_emails else 'None'}")
    print(f"All phone numbers found: {all_phones if all_phones else 'None'}")

#main function 
def main():
    print("Enter a text, and ill validate if it contains a valid email or number.\n")

    #user inputs email or phone number
    user_text=input("enter your text: ")

    validate_and_extract(user_text)

if __name__=="__main__":
    main()    
