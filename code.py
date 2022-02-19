menu_utama = '''
==============Data Penjualan Toko==============

1. Report Data Penjualan
2. Tambahkan Data Penjualan
3. Update Data Penjualan
4. Hapus Data Penjualan
5. Exit

Masukkan menu yang ingin dieksekusi (1-5): '''

menu_1 = '''
===========Record Data Penjualan Toko===========

1. Report Seluruh Data Penjualan
2. Report Data Penjualan Tertentu
3. Kembali Ke Menu Utama

Masukkan menu yang ingin dieksekusi (1-3): '''

menu_2 = '''
=========Penambahan Data Penjualan Toko=========

1. Tambahkan Data Penjualan
2. Kembali Ke Menu Utama

Masukkan menu yang ingin dieksekusi (1-2): '''

menu_3 = '''
============Ubah Data Penjualan Toko============

1. Ubah Data Penjualan
2. Kembali Ke Menu Utama

Masukkan menu yang ingin dieksekusi (1-2): '''

menu_4 = '''
==============Hapus Data Penjualan==============

1. Hapus Data Penjualan
2. Kembali Ke Menu Utama

Masukkan menu yang ingin dieksekusi (1-2): '''

stuffs_data = [
    {'Nama Barang': 'Buku', 'Harga': '8000', 'Jumlah': 20, 'Terjual': 10, 'Lokasi Rak': '3A'},
    {'Nama Barang': 'Pensil', 'Harga': '4000', 'Jumlah': 16, 'Terjual': 10, 'Lokasi Rak': '4A'},
    {'Nama Barang': 'Tas', 'Harga': '45000', 'Jumlah': 12, 'Terjual': 10, 'Lokasi Rak': '2B'},
    {'Nama Barang': 'Bulpen', 'Harga': '6000', 'Jumlah': 8, 'Terjual': 10, 'Lokasi Rak': '4A'}]

print_total = 'Nama Barang: {}\t| Harga: {}\t| Jumlah: {}\t| Terjual: {}\t| Lokasi Rak: {}'

def menu_1_func():  # show data
    while(True):
        menu_1_choice = input(menu_1)
        if menu_1_choice == '1':
            print()
            for nama_barang_for in stuffs_data:
                print(print_total.format(nama_barang_for['Nama Barang'], nama_barang_for['Harga'], nama_barang_for['Jumlah'], nama_barang_for['Terjual'], nama_barang_for['Lokasi Rak']))

        elif menu_1_choice == '2':
            menu_1_2_choice = input('\nMasukkan Nama Barang: ')
            for nama_barang_for in stuffs_data:
                menu_1_2_choice = menu_1_2_choice.capitalize()
                if menu_1_2_choice == nama_barang_for['Nama Barang']:
                    print(print_total.format(nama_barang_for['Nama Barang'], nama_barang_for['Harga'], nama_barang_for['Jumlah'], nama_barang_for['Terjual'], nama_barang_for['Lokasi Rak']))
                    break    
            else:
                print('\nTidak Ada Data Penjualan!')
        elif menu_1_choice == '3':
            break
        else:
            print('\nInvalid Input!')

def menu_2_func(): # create/add data
    while(True):
        menu_2_choice = input(menu_2)
        if menu_2_choice == '1':
            menu_2_prim_key = input('Nama Barang: ')
            menu_2_prim_key = menu_2_prim_key.capitalize()
            for nama_barang_for in stuffs_data:
                if menu_2_prim_key == nama_barang_for['Nama Barang']:
                    print('\nBarang sudah ada!')
                    break
            else:
                nama_barang = menu_2_prim_key
                try:
                    harga_barang = int(input('Harga: '))
                    jumlah_barang = int(input('Jumlah: '))
                    terjual_barang = int(input('Terjual: '))
                    lokasi_barang = input('Lokasi Rak: ')
                    lokasi_barang = lokasi_barang.upper()

                    while(True):
                        validation = input('\nApakah Anda Yakin? (Y/N): ')
                        validation = validation.upper()

                        if validation == 'Y':
                            addition_data = {
                                'Nama Barang': nama_barang,
                                'Harga': harga_barang,
                                'Jumlah': jumlah_barang,
                                'Terjual': terjual_barang,
                                'Lokasi Rak': lokasi_barang, }

                            stuffs_data.append(addition_data)
                            print('\nData Tersimpan!')
                            break
                        elif validation == 'N':
                            print('\nSiap!')
                            break
                except ValueError:
                    print('\nInvalid Input!')
                    break
        elif menu_2_choice == '2':
            break
        else:
            print('\nInvalid Input!')

def menu_3_func():  # update data
    while(True):
        menu_3_choice = input(menu_3)
        if menu_3_choice == '1':

            menu_3_prim_key = input('\nMasukkan Nama Barang: ')
            print()
            for nama_barang_for in stuffs_data:
                menu_3_prim_key = menu_3_prim_key.capitalize()
                if menu_3_prim_key == nama_barang_for['Nama Barang']:
                    print(print_total.format(nama_barang_for['Nama Barang'], nama_barang_for['Harga'], nama_barang_for['Jumlah'], nama_barang_for['Terjual'], nama_barang_for['Lokasi Rak']))

                    while(True):
                        validation = input('Apakah Anda Yakin? (Y/N): ')
                        validation = validation.upper()

                        if validation == 'Y':
                            nama_barang = menu_3_prim_key
                            try:
                                print('\nNama Barang: {}'.format(nama_barang))
                                harga_barang = int(input('Harga: '))
                                jumlah_barang = int(input('Jumlah: '))
                                terjual_barang = int(input('Terjual: '))
                                lokasi_barang = input('Lokasi Rak: ')
                                lokasi_barang = lokasi_barang.upper()

                                # update session
                                nama_barang_for['Harga'] = harga_barang
                                nama_barang_for['Jumlah'] = jumlah_barang
                                nama_barang_for['Terjual'] = terjual_barang
                                nama_barang_for['Lokasi Rak'] = lokasi_barang

                                print('\nData Berhasil Diubah!')
                                break
                            except ValueError:
                                print('\nInvalid Input!')
                                break
                        elif validation == 'N':
                            break
                    break
            else:
                print('\nTidak Ada Data Data Dengan Nama Barang {}!'.format(menu_3_prim_key))

        elif menu_3_choice == '2':
            break
        else:
            print('\nInvalid Input!')

def menu_4_func():
    while(True):
        menu_4_choice = input(menu_4)
        if menu_4_choice == '1':
            menu_4_2_choice = input('\nMasukkan Nama Barang: ')
            for nama_barang_for in stuffs_data:
                menu_4_2_choice = menu_4_2_choice.capitalize()
                if menu_4_2_choice == nama_barang_for['Nama Barang']:
                    print(print_total.format(nama_barang_for['Nama Barang'], nama_barang_for['Harga'], nama_barang_for['Jumlah'], nama_barang_for['Terjual'], nama_barang_for['Lokasi Rak']))
                    
                    while(True):
                        validation = input('Apakah Anda Yakin Ingin Menghapus Data Tersebut? (Y/N): ')
                        validation = validation.upper()

                        if validation == 'Y':
                            stuffs_data.remove(nama_barang_for)
                            print('Data Telah Dihapus!')
                            break
                        elif validation == 'N':
                            print('Data Tidak Dihapus!')
                            break
                    break
            else:
                print('\nTidak Ada Data Penjualan!')
                break

        elif menu_4_choice == '2':
            break
        else:
            print('\nInvalid Input!')

while(True):
    menu_choice = input(menu_utama)
    if menu_choice == '1':
        menu_1_func()
    elif menu_choice == '2':
        menu_2_func()
    elif menu_choice == '3':
        menu_3_func()
    elif menu_choice == '4':
        menu_4_func()
    elif menu_choice == '5':
        print('\nThanks!\n')
        break
    else:
        print('\nInvalid Input!')