# SiniBeli 🛍️

<h5> 🧑‍💻 Nama : Muhammad Radhiya Arshq  </h5>
<h5> 🆔 NPM : 2306275885 </h5>
<h5> 🏛️ Kelas : PBP D </h5>

## 🔗 Link Deployment 
Akses SiniBeli di link berikut : [http://muhammad-radhiya-sinibeli.pbp.cs.ui.ac.id/](http://muhammad-radhiya-sinibeli.pbp.cs.ui.ac.id/)

## 📃 Tugas 5

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

## ✅ Checklist Tugas 4
- [ ] Implementasikan fungsi untuk menghapus dan mengedit product.
- [ ] Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
	- [ ] Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
 	- [ ] Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
  	- [ ] Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
  	- [ ] Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
  	- [ ] Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
  	- [ ] Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
- [ ] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
	- Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
  	- Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
  	- Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
  	- Jelaskan konsep flex box dan grid layout beserta kegunaannya!
  	- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
 - [ ] Melakukan add-commit-push ke GitHub.

## 📃 Tugas 4

### 1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
Kedua hal tersebut memiliki fungsi yang sama yaitu untuk me-redirect user ke halaman atau URL tertentu, namun terdapat perbedaan antara `HttpResponseRedirect()` dan `redirect()` yaitu dalam menggunakan `HttpResponseRedirect()` isi dari argumen yang dapat diterima fungsi hanya bisa berupa url yang dapat digunakan, namun dalam penggunaan `redirect()` isi argumen yang dapat diterima bisa berupa `model`, `view`, atau url. Dengan itu banyak orang lebih sering menggunakan `redirect()` dibanding `HttpResponseRedirect()` karena sifatnya yang lebih fleksibel

### 2. Jelaskan cara kerja penghubungan model `Product` dengan `User`!
Dalam pembuatan proyek ini, cara menghubungkan model Product dengan user adalah dengan menambahkan field user pada model Product, field ini menggunakan sesuatu yang bernama `ForeignKey`. Ini berfungsi untuk menghubungkan data di model dengan user yang telah login sehingga setiap kali user membuat product, product tersebut akan dikaitkan dengan user tersebut. Implementasi sebagai berikut :
 ```python
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(default='')
 ```
### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication dan authorization keduanya digunakan dalam keamanan data. Authentication merupakan method yang meverifikasi identitas user dengan cek username, password dan informasi lainnya. Authorization merupakan method yang menentukan apakah user yang telah masuk diizinkan melakukan tindakan tertentu dengan menspesifikasi hal-hal yang dapat diakses dan dapat dilakukan. Dalam Django kedua hal tersebut diimplementasikan dengan menggunakan middleware `SessionMiddleware` dan `AuthenticationMiddleware` yang melacak pengguna yang login. Ketika user login dilakukan authentication untuk memastikan user, ini dilakukan dengan mengisi username dan password, dan jika belum ada maka bisa register dulu. Setelah melakukan itu Django memberikan authorization dengan memeriksa apa yang diizinkan atau yang tidak diizinkan bagi user yang telah login.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan mengimplementasikan session dan cookies. Jadi tiap kali user login, Django akan membuat sebuah session untuk user tersebut yang akan menyimpan informasi terkait status login user tersebut dan tiap session memiliki ID unik yang disimpan dalam cookies browser. Cookies ini nanti disimpan ke server dengan setiap request berikutnya. Beberapa kegunaan lain dari cookies adalah dapat digunakan untuk menyimpan preferensi user seperti bahasa, tema, dan pengaturan lainnya sehingga ketika user kembali maka aplikasi atau website dapat menampilkan informasi yang relevan dengan preferensi user. Pada umumnya cookies aman untuk digunakan dalam aktivitas online dan berkemungkinan kecil untuk menghasilkan malware pada perangkat yang digunakan.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Untuk pengimplementasian fungsi registerasi, login dan logout user terdapat beberapa hal yang saya tambahkan pada proyek Django yaitu dengan membuat beberapa fungsi dalam `views.py` seperti
	 ```python
	 def register(request): 
	    form = UserCreationForm() 
	
	    if request.method == "POST":
	        form = UserCreationForm(request.POST) 
	        if form.is_valid(): 
	            form.save() 
	            messages.success(request, 'Your account has been successfully created!')
	            return redirect('main:login')
	    context = {'form':form}
	    return render(request, 'register.html', context) 
	 ```
  	Fungsi `register()` dibuat untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.
  
  	```python
	def login_user(request):
	    if request.method == 'POST':
	        form = AuthenticationForm(data=request.POST)
	
	        if form.is_valid():
	                user = form.get_user()
	                login(request, user) 
	                response = HttpResponseRedirect(reverse("main:show_main")) 
	                response.set_cookie('last_login', str(datetime.datetime.now())) 
	                return response
	    else:
	        form = AuthenticationForm(request)
	    context = {'form': form}
	    return render(request, 'login.html', context)
	```
   	Fungsi `login_user()` dibuat untuk untuk mengautentikasi pengguna yang ingin login.
  
   	```python
	def logout_user(request):
	    logout(request) 
	    response = HttpResponseRedirect(reverse('main:login')) 
	    response.delete_cookie('last_login')
	    return response 
	```
	Fungsi `logout_user()` dibuat untuk melakukan mekanisme logout.
- Setelah melakukan hal tersebut saya berhasil membuat dua akun pengguna yang berbeda dan masing-masing pengguna memiliki product-product yang berbeda berdasarkan apa yang dilakukan pada kedua akun user tersebut
- Untuk menghubungkan model Product dengan User yang saya lakukan adalah dengan menambahkan field baru pada model `Product` pada `models.py` berupa user yang menggunakan `ForeignKey`
	```python
 	class Product(models.Model):
	    user = models.ForeignKey(User, on_delete=models.CASCADE) 
	    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	    name = models.CharField(max_length=100)
	    price = models.IntegerField()
	    description = models.TextField()
	    image = models.ImageField(default='')
 	```
 - Untuk menampilkan user yang sedang login dan menerapkan cookies terdapat beberapa hal yang saya modifikasi pada `views.py` yaitu dengan mengisi data `nama` dengan `request.user.username` dan menambahkan data `last_login` untuk melihat kapan terakhir kali user melakukan login.
	```python
 	def show_main(request): 
	    products = Product.objects.filter(user=request.user) 
	
	    context = {
	        'nama' : request.user.username, 
	        'npm' : '2306275885',
	        'kelas' : 'PBP D',
	
	        'app_intro' : 'Welcome to SiniBeli',
	        'products' : products,
	        'last_login': request.COOKIES['last_login'], 
	    }
	    
	    return render(request, "main.html", context)
 	```
    
## ✅ Checklist Tugas 4
  - [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
  - [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
  - [x] Menghubungkan model Product dengan User.
  - [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
  - [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
	- Apa perbedaan antara HttpResponseRedirect() dan redirect()
 	- Jelaskan cara kerja penghubungan model Product dengan User!
  	- Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
  	- Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
   	- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  - [x] Melakukan add-commit-push ke GitHub.

## 📃 Tugas 3

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
	- Untuk membuat input form untuk menambahkan objek model pada app sebelumnya yang saya lakukan adalah membuat berkas baru yaitu forms.py pada direktori main. Ini merupakan struktur form yang dapat menerima data Product baru. isi dari `forms.py` sebagai berikut
		```python
		from django.forms import ModelForm
		from main.models import Product
		
		class ProductEntryForm(ModelForm):
		    class Meta:
			model = Product
			fields = ['name', 'price', 'description', 'image']
		```
		`model = Product` menunjukkan model yang akan digunakan untuk form adalah Product yang dibuat dalam berkas `models.py`. Sedangkan `fields = ['name', 'price', 'description']` menunjukkan field dari model yang digunakan untuk form.
	
 		Setelah itu, saya membuat fungsi baru pada `views.py` dengan nama `create_product` yang akan menghasilkan form yang dapat menambahkan data product secara otomatis ketika data di-submit.
		```python
		def create_product(request):
		    form = ProductEntryForm()
		
		    if request.method == "POST":
		        form = ProductEntryForm(request.POST, request.FILES) 
		        if form.is_valid():
		            form.save()
		            return redirect('main:show_main')
		
		    context = {'form': form}
		    return render(request, "create_product.html", context)
	 	```
		Berdasarkan fungsi diatas, form akan dirender ke file HTML `create_product.html`. Dalam fungsi tersebut, jika isi input form valid (menggunakan `form.is_valid()`) , maka akan disimpan data tersebut dan akan di redirect ke fungsi `show_main` pada views aplikasi `main` setelah disubmit, alias data product akan ditampilkan setelah disubmit (menggunakan `return redirect('main:show_main')`).
	
		Kemudian, saya ubah fungsi show_main pada views.py menjadi seperti berikut.
		```python
	 	def show_main(request):
		    products = Product.objects.all()
		
		    context = {
		        'nama' : 'Muhammad Radhiya Arshq',
		        'npm' : '2306275885',
		        'kelas' : 'PBP D',
		
		        'app_intro' : 'Welcome to SiniBeli',
		        'products' : products,
		    }
		    
		    return render(request, "main.html", context)
	 	```
		`Product.objects.all()` digunakan untuk mengambil semua objek `Product` yang tersimpan dalam `database`
	
		Lalu saya mengubah isi urls.py dengan menambah import fungsi `create_product` dari `main` lalu menambahkan path URL ke dalam `urlpatterns` supaya dapat mengakses fungsi yang di import.
		```python
	 	urlpatterns = [
		    path('', show_main, name='show_main'),
		    path('create-product', create_product, name='create_product'),
		]
	 	```
	
	 	Terakhir saya membuat file HTML baru dengan nama `create_product.html` pada `main/templates` yang berisi struktur HTML untuk membuat form, dan melakukan modifikasi pada kedua file HTML pada `templates` untuk menyesuaikan pembuatan form dan penampilan product.
		- Untuk dapat melihat data product yang telah dibuat dalam format XML, JSON, XML by ID, dan JSON by ID, saya membuat 4 fungsi baru pada file `views.py` seperti berikut
	
			* XML
			```python
	  		def show_xml(request):
			    data = Product.objects.all()
			    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
	  		```
			* JSON
			```python
	  		def show_json(request):
			    data = Product.objects.all()
			    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
	  		```
			* XML by ID
			```python
	  		def show_xml_by_id(request, id):
			    data = Product.objects.filter(pk=id)
			    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
	  		```
			* JSON by ID
			```python
	  		def show_json_by_id(request, id):
			    data = Product.objects.filter(pk=id)
			    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
	  		```
	  	- Untuk masing-masing fungsi yang dibuat untuk menampilkan data dalam bentuk XML ataupun JSON, dilakukan routing URL pada file `urls.py` dengan mengimport setiap fungsi tersebut dan menambahkan path URL ke dalam `urlpatterns` supaya dapat mengakses fungsi yang di import seperti berikut. Isi `urlpatterns` menjadi seperti berikut.
		  	```python
		   	urlpatterns = [
			    path('', show_main, name='show_main'),
			    path('create-product', create_product, name='create_product'),
			    path('xml/', show_xml, name='show_xml'),
			    path('json/', show_json, name='show_json'),
			    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
			    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
			]
		   	```
2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
	
 	Dalam pengimplementasian sebuah platform, sangat diperlukan data delivery, ini karena akan ada waktu dimana kita perlu mengirimkan data dari satu stack ke stack lainnya. Data delivery juga menghubungkan antara beberapa komponen dalam sebuah platform dan memastikan data dapat dikirim dengan cepat dan efisien sehingga dapat diakses oleh pengguna dengan cepat. Dengan data delivery yang baik, sebuah platform dapat berfungsi dengan baik untuk pengembangnya dan penggunanya.

3. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

	Menurut saya, JSON lebih baik dibanding XML, beberapa alasan mengapa JSON lebih populer dibanding XML adalah :
	- Data ditampilkan dalam bentuk yang lebih readable dibanding xml yang bentuknya mirip dengan struktur file HTML,
 	- Parsing/pemrosesan data pada JSON lebih cepat dan ringan dibanding XML,
 	-  JSON cenderung lebih aman dibanding XML yang rentan terhadap modifikasi tidak sah sehingga dapat menciptakan risiko keamanan yang dikenal sebagai injeksi entitas eksternal XML (XXE).
 
4. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

	Kita membutuhkan method `is_valid()` pada form Django untuk mengetahui jika terjadi error pada form yang kita buat. ini dilakukan dengan memeriksa jika data atau file yang dikirim bukan variable None dan di cek jika data atau file tersebut memiliki error atau tidak. Jika hasilnya True untuk keduanya maka form valid dan akan di process dalam tahap selanjutnya. Sesuai dengan dokumentasinya dalam library Django, berikut potongan code method `is_valid()` :
	```python
 	def is_valid(self):
        """Return True if the form has no errors, or False otherwise."""
        return self.is_bound and not self.errors
 	```

5. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

	Kita membutuhkan `csrf_token` saat membuat form di Django untuk menambah keamanan data yang ada pada platform Django. `csrf_token` sendiri adalah token yang berfungsi sebagai security dan di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya seperti serangan csrf (cross-site request forgery). Dalam jenis serangan ini, penyerang mengirimkan tautan berupa SMS, email, atau chat sehingga penyerang dapat menipu pengguna yang sudah terautentikasi di situs web untuk melakukan berbagai tindakan. Menggunakan `csrf_token` berupa best practice dalam pembuatan form di Django karena dapat membantu mencegah serangan csrf yang dapat membuat perubahan yang tidak diinginkan dalam form yang kita buat.

* Screenshot dari hasil akses URL (format XML, JSON, XML by ID, dan JSON by ID) pada Postman
  	- XML
  	![WhatsApp Image 2024-09-16 at 06 42 57_dde6382a](https://github.com/user-attachments/assets/03dc7479-eefa-464c-8cc9-c38ddec6d65f)
  	- JSON
  	![WhatsApp Image 2024-09-16 at 06 42 13_d7249822](https://github.com/user-attachments/assets/15faf452-92a9-4dea-ba0d-0449757932ab)
	- XML by ID
	![WhatsApp Image 2024-09-16 at 06 42 13_accfdde7](https://github.com/user-attachments/assets/40873068-20c5-463f-b30d-89347dff7cd6)
	- JSON by ID
	![WhatsApp Image 2024-09-16 at 06 42 14_07164f6d](https://github.com/user-attachments/assets/510c73a1-f796-4207-9e11-3ee34c31dc49)

## ✅ Checklist Tugas 3
- [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.
- [x] Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
   - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   - Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
   - Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
   - Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
- [x] Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
- [x] Melakukan add-commit-push ke GitHub.
---
## 📃 Tugas 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Pertama saya membuat direktori lokal di perangkat saya, lalu saya membuat proyek Django didalamnya dengan perintah `django-admin startproject {nama proyek} .`
      Setelah menjalankan perintah ini, akan terbuat di direktori tersebut struktur direktori yang dibutuhkan dalam pembuatan proyek Django
    - Untuk membuat aplikasi dengan nama main pada proyek tersebut, saya jalankan perintah `python manage.py startapp main` di terminal. Setelah perintah dijalankan,
      direktori baru dengan nama main akan terbentuk yang berisi struktur awal untuk aplikasi Django.
    - Supaya dapat menjalankan aplikasi main, saya melakukan routing pada proyek dengan membuat file urls.py di dalam direktori main. File tersebut lalu diisi dengan kode berikut
      ```python
    	from django.urls import path
        from main.views import show_main
        
        app_name = 'main'
        
        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
      ```
	    `urls.py` bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main.
    - Lalu saya membuat model baru yang dilakukan dalam file `models.py` yang terdapat di dalam direktori aplikasi main. File tersebut lalu diisi dengan kode berikut:
      ```python
          class Product(models.Model):
            name = models.CharField(max_length=100)
            price = models.IntegerField()
            description = models.TextField()
      ```
        Model yang dibuat dalam `models.py` bernama `Product` dengan atribut `name`, `price`, dan `description`. Setiap atribut memiliki tipe data yang sesuai seperti `CharField`, `IntegerField`,         dan `TextField`.

    - Supaya dapat menghubung komponen view dan template pada proyek Django, dibuat fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta
      nama dan kelas. Kode yang saya tulis adalah sebagai berikut :
      ```python
        from django.shortcuts import render

        def show_main(request):
            context = {
                'nama' : 'Muhammad Radhiya Arshq',
                'npm' : '2306275885',
                'kelas' : 'PBP D',
                'app_intro' : 'Welcome to SiniBeli',
            }
            return render(request, "main.html", context)
      ```
      Fungsi `show_main` diatas menerima parameter `request` dan akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai. Lalu `context` didalam fungsi tersebut berupa dictionary
      yang berisi data yang akan dikirimkan ke tampilan. Dan `return render(request, "main.html", context)` berguna untuk me-render tampilan `main.html` yang ada di folder `templates`.
    - Kemudian saya membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`. Ini dilakukan dalam file `urls.py` yang berada dalam direktori
      proyek, bukan `main`. Perubahan yang saya buat adalah sebagai berikut :
      ```python
        from django.contrib import admin
        from django.urls import path, include
        
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('main.urls')),
        ]
      ```
    - Terakhir, setelah aplikasi selesai, saya lakukan deployment ke PWS (`https://pbp.cs.ui.ac.id.`) terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses melalui Internet.
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
 	![image](https://github.com/user-attachments/assets/60a620c8-80b7-4d72-91ef-6d65b73a0fc7)
	
	Penjelasan :
	- Pertama User mengirim request kepada Django
	- Request lalu di forward oleh `urls.py` dan diarahkan ke `views.py`
	- Lalu dari `views.py` diarahkan ke `models.py` untuk mengambil data model yang ada di database
	- Data models di proses di `views.py`
	- `main.html` yang ada berada dalam folder `templates` dirender dan dikembalikan ke User

4. Jelaskan fungsi git dalam pengembangan perangkat lunak!

	Git memiliki fungsi sebagai sistem kontrol versi untuk menyimpan, mengelola, dan berbagi source code secara efisien dan kolaboratif. Git memungkinkan pengembangan dengan kemampuannya untuk melacak perubahan kode sepanjang waktu. Git juga mendukung kolaborasi antar developer dengan memungkinkan beberapa orang bekerja pada proyek yang sama. Hal-hal tersebut membuat git memungkinkan pengelolaan perangkat lunak yang lebih terstruktur dan kolaboratif
 
5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
	
 	Framework Django dijadikan sebagai permulaan pembelajaran pengembangan perangkat lunak karena Django mendukung perkembangan pesat dan desain yang bersih dan pragmatis. Django mengikuti struktur Model-Template-View (MVT) yang terorganisasi dengan baik dan mudah untuk diinstal dan belajar. Ini memudahkan pemula dalam memahami pengembangan perangkat lunak dan pentingnya arsitektur yang terstruktur dalam pengembangannya. Django juga mendukung keamanan web dengan baik dengan menyediakan berbagai pencegahan dari serangan seperti Cross Site Request Forgery dan SQL Injection.

6. Mengapa model pada Django disebut sebagai ORM?
	
 	Model pada Django disebut sebagai ORM atau Object-Relational Mapper karena fungsinya dalam menghubungi objek atau model yang dibuat dengan database. Ini memungkinkan developer untuk berinteraksi dengan database menggunakan model objek python tanpa perlu menulis QuerySQL sehingga mempercepat proses pengembangan perangkat lunak. 

## ✅ Checklist Tugas 2

- [x] Membuat sebuah proyek Django baru.
- [x] Membuat aplikasi dengan nama main pada proyek tersebut.
- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- [x] Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
    - name
    - price
    - description
- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- [x] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [x] Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut
    - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    - Jelaskan fungsi git dalam pengembangan perangkat lunak!
    - Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Mengapa model pada Django disebut sebagai ORM?
