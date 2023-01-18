import sqlite3
import getpass


con = sqlite3.connect('data.db')
cur = con.cursor()

#Table
cur.execute("""CREATE TABLE IF NOT EXISTS data
                (nim integer not null, nama text, prodi text)""")
cur.execute("""CREATE TABLE IF NOT EXISTS rapor
                (nim integer, matakuliah text, nilai text)""")

#Table data
def tambah_data():
    nim_mahasiswa = int(input('Masukan NIM Mahasiswa: '))
    nama_mahasiswa = (input('Masukan Nama Mahasiswa: '))
    prodi_mahasiswa = (input('Masukan Jurusan Mahasiswa: '))
    cur.execute(f"""INSERT INTO data (nim,nama,prodi) 
                VALUES ('{nim_mahasiswa}','{nama_mahasiswa}','{prodi_mahasiswa}')""")
    con.commit()

def lihat_data():
    cur.execute("SELECT * FROM data")
    num = 1
    for i in cur.fetchall():
        print(num, f'NIM = {i[0]}\nNama = {i[1]}\nJurusan = {i[2]}', '\n')
        num += 1
def rename_data():
    c = con.cursor()
    print('''
    1.NIM
    2.Nama
    3.Jurusan
    ''')
    user_input = int(input('Masukan Opsi: '))
    if user_input == 1: 
        nim_lama = int(input('Masukan NIM lama = '))
        nim_baru = int(input('Masukan NIM baru = '))
        c.execute(f"UPDATE data SET nim='{nim_baru}' WHERE nim='{nim_lama}'")
        print(f"NIM sudah di ubah menjadi '{nim_baru}'")
    elif user_input == 2: 
        nama_lama = str(input('Masukan Nama lama = '))
        nama_baru = str(input('Masukan Nama baru = '))
        c.execute(f"UPDATE data SET nama='{nama_baru}' WHERE nama='{nama_lama}'")
        print(f"Nama sudah di ubah menjadi '{nama_baru}'")
    elif user_input == 3: 
        prodi_lama = str(input('Masukan Jurusan lama = '))
        prodi_baru = str(input('Masukan Jurusan baru = '))
        c.execute(f"UPDATE data SET prodi='{prodi_baru}' WHERE prodi='{prodi_lama}'")
        print(f"'Mata Kuliah sudah di ubah menjadi '{prodi_baru}'")
    con.commit()

def delete_data():
    c = con.cursor()
    user_input = int(input('Masukan NIM: '))
    c.execute(f"DELETE FROM data WHERE nim='{user_input}'")
    con.commit()

#Table Rapor
def tambah_nilai():
    nim_mahasiswa = int(input('Masukan NIM Mahasiswa: '))
    judul_mahasiswa = str(input('Masukan Mata Kuliah Mahasiswa: '))
    nilai_mahasiswa = int(input('Masukan Nilai Mahasiswa: '))
    nilai_input = nim_mahasiswa, judul_mahasiswa, nilai_mahasiswa
    cur.execute(""" INSERT INTO rapor (nim, matakuliah, nilai) VALUES (?, ?, ?)""", nilai_input)
    con.commit()

def lihat_rapor():
    nim = int(input('Masukan NIM: '))
    cur.execute(f"""SELECT * FROM rapor where nim='{nim}'""")
    num = 1
    for i in cur.fetchmany():
        nama = i
    print(f'Nilai Mahasiswa {nim}')

    for x in cur.fetchall():
        z = x[2]
        if z >= '80':
            z = 'A'
        elif z >= '70' or z < '80':
            z = 'B'
        elif z >= '60' or z < '70':
            z = 'C'
        elif z >= '50' or z < '60':
            z = 'D'
        elif z < '50':
            z = 'E'
        print(num,".", x[1], x[2],"=", z)
        num += 1
        
def update_rapor():
    c = con.cursor()
    print('''
    1. NIM
    2. Mata Kuliah
    3. Nilai
    ''')
    user_input = int(input('Masukan Opsi: '))
    if user_input == 1: 
        nim_lama = int(input('Masukan NIM lama = '))
        nim_baru = int(input('Masukan NIM baru = '))
        c.execute(f"UPDATE rapor SET nim={nim_baru} WHERE nim={nim_lama}")
        print(f'NIM sudah di ubah menjadi {nim_baru}')
    elif user_input == 2: 
        matkul_lama = str(input('Masukan Mata Kuliah lama = '))
        matkul_baru = str(input('Masukan Mata Kuliah baru = '))
        c.execute(f"UPDATE rapor SET matakuliah='{matkul_baru}' WHERE matakuliah='{matkul_lama}'")
        print(f'Mata Kuliah sudah di ubah menjadi {matkul_baru}')
    elif user_input == 3: 
        nilai_lama = int(input('Masukan Nilai lama: '))
        nilai_baru = int(input('Masukan Nilai baru: '))
        c.execute(f"UPDATE rapor SET nilai='{nilai_baru}' WHERE nilai='{nilai_lama}'")
        print(f"'Mata Kuliah sudah di ubah menjadi '{nilai_baru}'")
    con.commit()


def detele_nilai():
    c = con.cursor()
    user_input = int(input('Masukan NIM: '))
    c.execute(f"DELETE FROM rapor WHERE nim={user_input}")
    con.commit()

#Menu
def login_page():
    print("Student Center E-Learning")
    usr_profile = {'admin' : 'admin1'}

    #login usr pass
    while True:
        login_user = input('Login = ')
        if login_user in usr_profile.keys():
            login_pass = getpass.getpass('Password = ')
            if login_pass in usr_profile.values():
                landing_page()
            else:
                print('Wrong Password!!')
        else:
            print(f'{login_user} does not exists')

def landing_page():
    print("""
    Student Center E-Learning
    Select Menu:
    1. Data Mahasiswa
    2. Nilai
    3. Exit
    """)
    user_input = int(input("Masukan Opsi: "))
    if user_input == 1:
        menu1()
    elif user_input == 2:
        menu2
    elif user_input == 3:
        exit

    
    #action for user
def menu1():
    print('''
        1. Tambah data Mahasiswa dan Mata Kuliah
        2. Lihat data Mahasiswa dan Mata kuliah
        3. Rename data Mahasiswa dan Mata Kuliah
        4. Hapus data Mahasiswa dan Mata Kuliah
        5. Kembali
        ''')
    user_input = int(input('Masukan Opsi = '))
    if user_input == 1:
        tambah_data()
        landing_page()
    elif user_input == 2:
        lihat_data()
        landing_page()
    elif user_input == 3:
        rename_data()
        landing_page()
    elif user_input == 4:
        delete_data()
        landing_page()
    elif user_input == 5:
        return landing_page()
            
def menu2():
    print("""
        1. Tambah nilai Mahasiswa
        2. Lihat nilai Mahasiswa
        3. Update nilai Mahasiswa
        4. Delete nilai Mahasiswa
        5. Kembali
        """)
    user_input = int(input("Masukan Opsi: "))
    if user_input == 1:
        tambah_nilai()
        landing_page()
    elif user_input == 2:
        lihat_rapor()
        landing_page()
    elif user_input == 3:
        update_rapor()
        landing_page()
    elif user_input == 4:
        detele_nilai()
        landing_page()
    elif user_input == 5:
        return landing_page()
    else:
        print('Error!')

login_page()


