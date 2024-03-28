from validators.emailValidator import validate_email


def main():
    email = input("Enter an email address: ")
    if validate_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")


if __name__ == "__main__":
    main()
