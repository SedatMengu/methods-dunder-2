# __str__ ve __repr__ metotları

# class dan üretine bir nesnenin stringe nasıl döndürüleceğini belirleyen fonksiyonlardır.
# her ikisi de string üretir. print __repr__  olarak ayrıca belirtilmediği sürece 1.tercih her daim __str__ dir.
# birbirlerine çok benzeselerde aynı fonksiyon değildirler.
# __str__ fonksiyonu kullanıcının görmesini istediğimiz şekle sokar.
# __repr__ fonksiyonu geliştiricinin görmesini istediğimiz şekle sokar.
# __repr__ nin mantıklı kullanımı : print edileni bir değişkene kopyalayıp yapıştırınca baştan üretilebilir olması

#__str__ magic method

a = "python"

print(str(a))                # / python             # str fonksiyonu kullanıcının görmesini istediğimiz şekle sokar.
print(repr(a))               # / 'python'           # repr fonksiyonu geliştiricinin görmesini istediğimiz şekle sokar.


b = 2/8

print(str(b))               # / 0.25                # str fonksiyonu kullanıcının görmesini istediğimiz şekle sokar.
print(repr(b))              # / 0.25                # repr fonksiyonu geliştiricinin görmesini istediğimiz şekle sokar.


from datetime import date

bugun = date.today()
print(bugun)                # / 2023-04-19
print(str(bugun))           # / 2023-04-19                      # str fonksiyonu kullanıcının görmesini istediğimiz şekle sokar.
print(repr(bugun))          # / datetime.date(2023, 4, 19)      # repr fonksiyonu geliştiricinin görmesini istediğimiz şekle sokar.

class futbolcu:
    def __init__(self,isim,soyisim,yas):
        self.isim=isim
        self.soyisim=soyisim
        self.yas=yas
    
futbolcu1 = futbolcu("şamil","kaçar",25)

print(futbolcu1)                            # / <__main__.futbolcu object at 0x000001A1ABD1DF40>

# python print ederken print edeceği ifadenin class ına gider ve oradaki __str__ metotuna göre print eder , (str.int,list vs)
# futbolcu klasının içinde __str__ yok ise hangi sınıfa göre print edeceğini bilemez ve hatavari bir uyarı gönderir.
# __str__ yok, yerine __repr__ var ise __repr__ çalışır. eğer her ikisi de varsa __str__ çalışır.
# bu hatavari olayın önüne geçmek için şu şekilde bir yol izlememiz gerekir.

class futbolcu1:
    def __init__(self,isim,soyisim,yas):
        self.isim=isim
        self.soyisim=soyisim
        self.yas=yas

    def __str__(self):
        return "ad : {} , soyad : {} , yas : {}".format(self.isim,self.soyisim,self.yas)
    
    def __repr__(self):
        return "__repr__ çalışıyor"
    
futbolcu11 = futbolcu1("şamil","kaçar",25)

print(futbolcu11)                                # / ad : şamil , soyad : kaçar , yas : 25
print(str(futbolcu11))                           # / ad : şamil , soyad : kaçar , yas : 25
print(futbolcu11.__str__())                      # / ad : şamil , soyad : kaçar , yas : 25   # nesne üzerinden çağırma
print(repr(futbolcu11))                          # / __repr__ çalışıyor
print(futbolcu11.__repr__())                     # / __repr__ çalışıyor                      # nesne üzerinden çağırma

# __repr__ fonksiyonunun asıl kullanım mantığına örnek : 

class futbolcu2:
    def __init__(self,isim,soyisim,yas):
        self.isim=isim
        self.soyisim=soyisim
        self.yas=yas

    def __str__(self):
        return "ad : {} , soyad : {} , yas : {}".format(self.isim,self.soyisim,self.yas)
    
    def __repr__(self):
        return 'futbolcu("{}","{}",{})'.format(self.isim,self.soyisim,self.yas)
    
futbolcu21 = futbolcu2("şamil","kaçar",25)
print(futbolcu21.__repr__())

futbolcu22 = futbolcu2("şamil","kaçar",25)      # / futbolcu22 değişkenini terminalden kopyala yapıştır yaptık.
print(futbolcu22.__str__())