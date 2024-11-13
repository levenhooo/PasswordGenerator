import random

LowerCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UpperCase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
SpecialSymbols = ["!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "", "{", "|", "}", "~"]
Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
PasswordLength = 0
SpecialSymbols_Decision = "y"
Password = []
FinalPassword = []
Password_Is_Generated = False
Questions_List = []

def Ask_Questions():
    PasswordLength = input("Please enter a password length: ")
    SpecialSymbols_Decision = input("Do you want to have special characters in your password? (y/n): ")
    return PasswordLength, SpecialSymbols_Decision

def Generate_Password_With_SpecialChars(PW_Length):
    PasswordLength = PW_Length
    for i in range(0, int(PasswordLength)):
        LowerCase_Symbol = random.choice(LowerCase)
        Password.append(LowerCase_Symbol)
        UpperCase_Symbol = random.choice(UpperCase)
        Password.append(UpperCase_Symbol)
        SpecialSymbols_Symbol = random.choice(SpecialSymbols)
        Password.append(SpecialSymbols_Symbol)
        Numbers_Symbol = random.choice(Numbers)
        Password.append(Numbers_Symbol)
    for b in range(0, int(PasswordLength)):
        FinalPasswordChars = random.choice(Password)
        FinalPassword.append(FinalPasswordChars)
    output_string = ''.join(str(element) for element in FinalPassword)
    print("Your new password is: ", output_string)
    return True

def Generate_Password_Without_SpecialChars(PW_Length):
    PasswordLength = PW_Length
    #print("Passwordlength: ", PasswordLength)
    for i in range(0, int(PasswordLength)):
        LowerCase_Symbol = random.choice(LowerCase)
        Password.append(LowerCase_Symbol)
        UpperCase_Symbol = random.choice(UpperCase)
        Password.append(UpperCase_Symbol)
        Numbers_Symbol = random.choice(Numbers)
        Password.append(Numbers_Symbol)
    for b in range(0, int(PasswordLength)):
        FinalPasswordChars = random.choice(Password)
        FinalPassword.append(FinalPasswordChars)
    output_string = ''.join(str(element) for element in FinalPassword)
    print("Your new password is: ", output_string)
    return True
        

while Password_Is_Generated == False:
    Questions_List = Ask_Questions()
    PW_Length = Questions_List[0]
    SpecialSymbols_Decision_Dummy = Questions_List[1]
    if SpecialSymbols_Decision_Dummy == "y" or SpecialSymbols_Decision_Dummy == "Y":
        bool_generate_pw_with_specialchars = Generate_Password_With_SpecialChars(PW_Length)
        if bool_generate_pw_with_specialchars == True:
            Password_Is_Generated = True
    else:
        if SpecialSymbols_Decision_Dummy == "n" or SpecialSymbols_Decision_Dummy == "N":
            bool_generate_pw_without_specialchars = Generate_Password_Without_SpecialChars(PW_Length)
            if bool_generate_pw_without_specialchars == True:
                Password_Is_Generated = True
        else:
            continue
            # Ask_Questions()