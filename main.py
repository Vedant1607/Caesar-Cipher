import art
print(art.logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text, shift_amount, user_choice):
    cipher_text = ""
    
    if user_choice == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter in alphabet:
            shift_index = alphabet.index(letter) + shift_amount
            shift_index %= len(alphabet)
            cipher_text += alphabet[shift_index]
    print(f"Your {choice}d text is '{cipher_text}'")

game = True

while game:
    choice = input("encode or decode\n").lower()
    text = input(f"Enter text to {choice}\n").lower()
    shift = int(input("How much do you want to shift ?\n"))

    caesar(original_text=text, shift_amount=shift, user_choice=choice)
    
    redo = input("Do you want to rerun this program ? Type 'yes' or 'no'\n").lower()
    
    if redo == "no":
        game = False
        