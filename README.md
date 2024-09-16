# SiniBeli

<h5> Nama : Muhammad Radhiya Arshq </h5>
<h5> NPM : 2306275885 </h5>
<h5> Kelas : PBP D </h5>

## Link Deployment
Akses SiniBeli di link berikut : [http://muhammad-radhiya-sinibeli.pbp.cs.ui.ac.id/](http://muhammad-radhiya-sinibeli.pbp.cs.ui.ac.id/)

## Tugas 3

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

3. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

4. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

5. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

* Screenshot dari hasil akses URL (format XML, JSON, XML by ID, dan JSON by ID) pada Postman
  	- XML
  	![WhatsApp Image 2024-09-16 at 06 42 57_dde6382a](https://github.com/user-attachments/assets/03dc7479-eefa-464c-8cc9-c38ddec6d65f)
  	- JSON
  	![WhatsApp Image 2024-09-16 at 06 42 13_d7249822](https://github.com/user-attachments/assets/15faf452-92a9-4dea-ba0d-0449757932ab)
	- XML by ID
	![WhatsApp Image 2024-09-16 at 06 42 13_accfdde7](https://github.com/user-attachments/assets/40873068-20c5-463f-b30d-89347dff7cd6)
	- JSON by ID
	![WhatsApp Image 2024-09-16 at 06 42 14_07164f6d](https://github.com/user-attachments/assets/510c73a1-f796-4207-9e11-3ee34c31dc49)

## Checklist Tugas 3
- [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.
- [x] Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
- [ ] Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
   - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   - Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
   - Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
   - Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
- [x] Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
- [x] Melakukan add-commit-push ke GitHub.
---
## Tugas 2

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

## Checklist Tugas 2

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
