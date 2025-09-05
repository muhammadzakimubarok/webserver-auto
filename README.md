# 🔧 Web Server Otomatis untuk Siswa TKJ

Proyek ini berisi script Python yang dapat menginstal web server Apache dan PHP secara otomatis di Debian 11, serta membuat halaman web dinamis menggunakan virtual host. Cocok untuk pembelajaran produktif TKJ dan integrasi dengan Modul 3 Koding dan Kecerdasan Artifisial.

## 📦 Isi Proyek

- `web_sederhana.py`  
  Script versi minimal: langsung install Apache + PHP dan membuat file `index.php` di `/var/www/html`.

- `web_virtualhost.py`  
  Script versi lengkap: membuat virtual host `siswa.local`, konfigurasi Apache, dan halaman web dinamis.

- `template_index.php`  
  Contoh isi file PHP yang bisa dimodifikasi siswa.

- `tugas_siswa.md`  
  Instruksi tugas praktik untuk siswa TKJ.

## 🚀 Cara Menjalankan

1. Clone repositori ini:
   ```bash
   git clone https://github.com/zaki-smkn4/webserver-auto.git
   cd webserver-auto
