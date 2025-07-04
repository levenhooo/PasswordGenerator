import pyperclip
import secrets
import sys

LowerCase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UpperCase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
SpecialSymbols = ["!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "", "{", "|", "}", "~"]
Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
PasswordLength = 0
SpecialSymbols_Decision = "y"
Password_Is_Generated = False
Questions_List = []
Character_List = []
Password = []
FinalPassword = []

def Ask_Questions():
    PasswordLengthCorrect = False
    SpecialSymbols_Decision_Answer = False

    while not PasswordLengthCorrect:
        PasswordLength = input("Please enter a password length: ")
        try:
            PasswordLength = int(PasswordLength)
            if PasswordLength > 0:
                PasswordLengthCorrect = True
            else:
                continue
        except ValueError:
            continue

    while not SpecialSymbols_Decision_Answer:
        SpecialSymbols_Decision = input("Do you want to have special characters in your password? (y/n): ")
        if SpecialSymbols_Decision == "y" or SpecialSymbols_Decision == "Y" or SpecialSymbols_Decision == "n" or SpecialSymbols_Decision == "N":
            SpecialSymbols_Decision_Answer = True
        else:
            continue

    return PasswordLength, SpecialSymbols_Decision

def Generate_Password_With_SpecialChars(PW_Length):
    PasswordLength = PW_Length
    output_string = ""
    Password.clear()
    FinalPassword.clear()
    for i in range(0, int(PasswordLength)):
        LowerCase_Symbol = secrets.choice(LowerCase)
        Password.append(LowerCase_Symbol)
        UpperCase_Symbol = secrets.choice(UpperCase)
        Password.append(UpperCase_Symbol)
        SpecialSymbols_Symbol = secrets.choice(SpecialSymbols)
        Password.append(SpecialSymbols_Symbol)
        Numbers_Symbol = secrets.choice(Numbers)
        Password.append(Numbers_Symbol)

    for b in range(0, int(PasswordLength)):
        FinalPasswordChars = secrets.choice(Password)
        FinalPassword.append(FinalPasswordChars)

        if b >= 1:
            RepeatingCharacters = False
            if FinalPassword[b - 1] == FinalPassword[b]:
                RepeatingCharacters = True
                while RepeatingCharacters:
                    NewChar = secrets.choice(Password)
                    FinalPassword[b] = NewChar
                    if FinalPassword[b - 1] == FinalPassword[b]:
                        continue
                    else:
                        RepeatingCharacters = False
                        break

    output_string = ''.join(str(element) for element in FinalPassword)
    print("Your new password is: ", output_string)
    clipboard = input("Do you want to copy your password to your clipboard? (y/n)")
    if clipboard == "y" or clipboard == "Y":
        pyperclip.copy(output_string)
    return True

def Generate_Password_Without_SpecialChars(PW_Length):
    PasswordLength = PW_Length
    output_string = ""
    Password.clear()
    FinalPassword.clear()
    for i in range(0, int(PasswordLength)):
        LowerCase_Symbol = secrets.choice(LowerCase)
        Password.append(LowerCase_Symbol)
        UpperCase_Symbol = secrets.choice(UpperCase)
        Password.append(UpperCase_Symbol)
        Numbers_Symbol = secrets.choice(Numbers)
        Password.append(Numbers_Symbol)

    for b in range(0, int(PasswordLength)):
        FinalPasswordChars = secrets.choice(Password)
        FinalPassword.append(FinalPasswordChars)
        if b >= 1:
            RepeatingCharacters = False
            if FinalPassword[b - 1] == FinalPassword[b]:
                RepeatingCharacters = True
                while RepeatingCharacters:
                    NewChar = secrets.choice(Password)
                    FinalPassword[b] = NewChar
                    if FinalPassword[b - 1] == FinalPassword[b]:
                        continue
                    else:
                        RepeatingCharacters = False
                        break

    output_string = ''.join(str(element) for element in FinalPassword)
    print("Your new password is: ", output_string)
    clipboard = input("Do you want to copy your password to your clipboard? (y/n)")
    if clipboard == "y" or clipboard == "Y":
        pyperclip.copy(output_string)
    return True


while not Password_Is_Generated:
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
    decision_has_been_made = False
    while decision_has_been_made != True:
        decision = input("Do you want to generate another password? (y/n)")
        if decision == "y" or decision == "Y":
            
            decision_has_been_made = True
            Password_Is_Generated = False
        elif decision == "n" or decision == "N":
            Password_Is_Generated = True
            sys.exit(0)
        else:
            continue
        
