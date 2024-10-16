def pesan_makanan():
    print("Selamat datang di layanan pesan makanan!")
    print("Silakan pilih makanan yang ingin Anda pesan:")
    print("1. Nasi Goreng - Rp 30.000")
    print("2. Ayam Bakar - Rp 40.000")
    print("3. Sate - Rp 25.000")
    print("4. Mie Goreng - Rp 20.000")

    # Mengambil input dari pengguna
    pilihan = int(input("Masukkan nomor pilihan Anda (1-4): "))

    # Menggunakan if-else untuk menentukan pesanan
    if pilihan == 1:
        print("Anda memilih Nasi Goreng. Total: Rp 30.000")
    elif pilihan == 2:
        print("Anda memilih Ayam Bakar. Total: Rp 40.000")
    elif pilihan == 3:
        print("Anda memilih Sate. Total: Rp 25.000")
    elif pilihan == 4:
        print("Anda memilih Mie Goreng. Total: Rp 20.000")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Memanggil fungsi untuk menjalankan program
pesan_makanan()