# -*- coding:utf-8 -*-       # Türkçe karakter kullanımı için gerekli komut        
class Library:
    def __init__(self, dosya_adi):   
        self.dosya_adi = dosya_adi
        self.file = open(self.dosya_adi, "a+") # Dosyayı açtım. 
        self.file.seek(0)
    def close_file(self):
        self.file.close()
    def list_books(self):
        self.file.seek(0)
        bos_mu = self.file.read()
        self.file.seek(0)
        if bos_mu == "":
            print("Listelenecek kitap mevcut değil") 
        else:    
            lines = self.file.read().splitlines() # Splitlines komutu lines değişkenini liste haline getiriyor. 
            for line in lines:
                line = line.split(",")  # split methodu ","e göre ayırarak liste haline getirir. 
                print(line[0] , line[1])
    def add_book(self):
        self.file.seek(0)
        bos_mu = self.file.read()
        self.file.seek(0,2)
        if bos_mu != "":
            self.file.write("\n")
        Kitap_İsmi = input("Eklenecek kitap ismini girin :")
        Kitap_Yazari = input("Eklenecek kitap yazarının ismini girin :")
        Yayin_Tarihi = input("Eklenecek kitabın ilk yayın tarihini girin :")
        Sayfa_Sayisi = input("Eklenecek kitabın sayfa sayısını girin :")
        self.file.write(Kitap_İsmi +", "+ Kitap_Yazari +" , "+ Yayin_Tarihi +" , "+ Sayfa_Sayisi)
    def remove_book(self):
        count = 0
        self.file.seek(0)
        bos_mu = self.file.read()
        self.file.seek(0)
        if bos_mu == "":
            print("Silinecek kitap mevcut değil")
        else:
            self.file.seek(0)    
            lines = self.file.read().splitlines() # Splitlines komutu lines değişkenini liste haline getiriyor 
            Silinecek_Kitap = input("Silinecek kitabın adını girin :")
            for line in lines:
                line = line.split(",")  # split methodu ","e göre ayırarak liste haline getirir.
                if line[0] == Silinecek_Kitap:  
                    del lines[count]     # CONSTRUCTER
                    # Dosya içeriği silme ve tekrar yazma  
                    self.file.seek(0)
                    self.file.truncate() # dosyanın içeriğini sildim  
                    for line in lines:
                        self.file.write((line) + "\n") # tekrardan line değişkeni ile satırları yazdırdım he satırın sonuna /n koyarak alt satıra geçtim.
                    print("Kitap silindi.")
                else:
                    count = count + 1
                    if count == len(lines):
                        print("Silmek istediğiniz kitap ismi sistemde mevcut değil!")                   
while True:
    print("\033[1m\n*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Close\n\n\033[0m") # Terminale kalın yazma komutu 
    islem = input("\033[1mLütfen yapmak istediğiniz işlem numarasını  giriniz :\033[0m")
    lib = Library("books.txt")  # "lib" adında bir obje oluşturdum bu obje "books.txt" dosyasını veritabanı olarak kullanacaktır.
    if islem == "1":
        lib.list_books()
    elif islem == "2":
        lib.add_book()
    elif islem == "3":
        lib.remove_book()
    elif islem == "4":
        break
    else:
       print("Lütfen geçerli bir işlem numarası giriniz")    
lib.close_file()
