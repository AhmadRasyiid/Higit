# import code
import getpass
import time

start_time = time.time()
# DataBase 
database = {
    'datauser': {
        'Yona': {
            'nama': 'Yona Necana',
            'umur': '15',
            'status': 'siswa',
            'password': 'yonaaja'
        },
        'Joy': {
            'nama': 'Joy Ichimiro',
            'umur': '19',
            'status': 'mahasiswa',
            'passwor': 'joyaja'
        },
        'Rey': {
            'nama': 'Rey',
            'umur': '25',
            'status': 'pegawai kantoran',
            'passord': 'reyaja'
        }
    }
}
# login uotput syntax
def login():
    print ("===== LOGIN =====")
    for _ in range(5):
        username = input("Masukkan username : ")
        password = getpass("Masukkan password : ")

        if username in database['datauser']:
            if database['datauser'] == password:
                print("===== BERHASIL LOGIN =====")
                print("Hallo! selamat datang, {}".format(username))
                return True
            else:
                print("password salah! coba lagi")
        else:
            print("username tidak ditemukan! coba lagi")
    print("anda telah gagal loginsebanyak 5 kali")
    return False
login()

print("""
<======================>
|                      |
|    Selamat datang    |
|                      |
<======================>
      """)

print ("waktu login = ", time.time()- start_time, "detik")