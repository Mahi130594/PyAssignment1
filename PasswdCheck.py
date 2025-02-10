
def Contain_Special_Char(Password):
    Specilal_Characters = "!@#$%^&*"
    for char in password:
        if char in Specilal_Characters:
            return True
    return False

def check_passwd_strength(Password):
    if len(Password) < 8:
        return False, "Passwd Must 8 Characters"
    if not any(char.islower() for char in Password) or not any(char.isupper() for char in Password):
        return False, "Passwd Must contain upper and lower Characters"
    if not any(char.isdigit() for char in Password):
        return False, "Passwd Must contain one Digit"
    if not Contain_Special_Char(password):
        return False, " Passwd Must contain Special Character"
    return True, "Passwd is Strong"
password = input("Enter the Password: ")
strongpwd, message = check_passwd_strength(password)
if strongpwd:
    print(message)
else:
    print("Error", message)
