# Game Tebak Angka
# Secret number: 250

secret_number = 250

while True:
    guess = int(input("Tebak angka: "))
    
    if guess == secret_number:
        print("🎉 Selamat! Anda berhasil menebak angka yang benar!")
        break
    elif guess < secret_number:
        print("Angka terlalu kecil. Coba lagi!")
    else:
        print("Angka terlalu besar. Coba lagi!")