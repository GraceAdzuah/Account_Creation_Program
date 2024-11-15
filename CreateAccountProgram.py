#!/usr/bin/env python3

def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name

def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if not digit or not cap_letter or len(password) < 8:
            print("Password must be 8 characters or more with at least one digit and one uppercase letter.")
        else:
            return password

def get_email():
    while True:
        email = input("Enter email address:   ").strip()
        if "@" in email and email.endswith(".com"):
            return email
        else:
            print("Please enter a valid email address.")

def get_phone_number():
    while True:
        phone = input("Enter phone number:    ").strip()
        cleaned_phone = ''.join(filter(str.isdigit, phone))  # Remove non-numeric characters
        if len(cleaned_phone) == 10:
            formatted_phone = f"{cleaned_phone[:3]}.{cleaned_phone[3:6]}.{cleaned_phone[6:]}"
            return formatted_phone
        else:
            print("Please enter a 10-digit phone number.")

def main():
    #Display a welcome message
    print("Welcome! Kindly fill out your details to create an account.")
    print()

    full_name = get_full_name()
    print()
    
    password = get_password()
    print()
    
    email = get_email()
    print()
    
    phone_number = get_phone_number()
    print()
    
    first_name = get_first_name(full_name)   
    print(f"Hi {first_name}, thanks for creating an account.")
    print(f"We'll text your confirmation code to this number: {phone_number}")

if __name__ == "__main__":
    main()