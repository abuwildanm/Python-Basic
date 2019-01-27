def tambah(a,b):
    print(a,'+',b,'=',a+b)

def kurang(a,b):
    print(a,'-',b,'=',a-b)

def main():
    print('ini adalah fungsi utama dari matematika')

if __name__ == '__main__':
    main()

#variabel __name__ jika dipanggil disini, maka akan memunculkan tulisan "__main__"
#tapi jika variabel __name__ dipanggil dari file yang berbeda (misal file main import matematika), maka dia akan memunculkan tulisan "matematika"