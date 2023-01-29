def create_console(nama, nomor, hari):
    list_pekerja.append(nama)
    list_id.append(nomor)
    list_hari.append(hari)
    string_nama = ",".join(list_pekerja)
    string_id = ",".join(str(x) for x in list_id)
    string_hari = ",".join(list_hari)
    open_file = open("ListPekerja.txt", "w")
    open_file.write(string_nama + "\n")
    open_file.write(string_id + "\n")
    open_file.write(string_hari)
    open_file.close()

    open_file = open("ListPekerja.txt", "r")
count = 0

list_pekerja = []
list_id = []
list_hari = []

while True:
    count += 1
    data = open_file.readline()
    
    if not data:
        break
    
    if count == 1 :
        list_pekerja = data.rstrip().split(",")
    
    elif count == 2 :
        list_id = data.rstrip().split(",")

    elif count == 3 :
        list_hari = data.rstrip().split(",")

list_menu = ["1. create data pekerja", "2. read data pekerja", "3. update data pekerja", "4. delete data pekerja", "0. keluar program"]
while True :
    print ("=======================")
    print ("       menu utama      ")
    print ("=======================")
    for y in list_menu: 
        print(y) 
    print ("=======================")
    print (" pilih opsi : ")
    menu =int(input()) 
    if menu == 1 :
        print ("Masukkan Nama : ")
        nama = str(input())
        print ("Masukkan ID : ")
        nomor = int(input()) 
        print ("masukkan Hari : ")
        hari = str(input())
        create_console(nama, nomor, hari)

    elif menu == 0 :
        break

    else :
        print("opsi tidak ditemukan")
