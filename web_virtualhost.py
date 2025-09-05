import os  # Import modul os untuk menjalankan perintah sistem Linux

# 1. Update daftar paket dan install Apache + PHP
# Apache = web server, PHP = bahasa pemrograman web
os.system("apt update && apt install apache2 php libapache2-mod-php -y")

# 2. Buat folder untuk virtual host baru bernama siswa.local
# Folder ini akan menyimpan file web yang bisa diakses lewat domain lokal
os.system("mkdir -p /var/www/siswa.local")

# 3. Ubah kepemilikan folder agar bisa diakses oleh Apache
os.system("chown -R www-data:www-data /var/www/siswa.local")

# 4. Buat file index.php berisi konten dinamis
# File ini akan ditampilkan saat siswa mengakses http://siswa.local
konten_php = """
<?php
echo "<h1>Selamat Datang di Website Siswa TKJ</h1>";
echo "<p>Website ini dibuat otomatis menggunakan Python dan PHP di Debian 11.</p>";
echo "<p>Waktu server: " . date("d-m-Y H:i:s") . "</p>";
?>
"""
# Simpan file index.php ke folder siswa.local
with open("/var/www/siswa.local/index.php", "w") as file:
    file.write(konten_php)

# 5. Buat file konfigurasi virtual host Apache
# Konfigurasi ini memberitahu Apache bahwa siswa.local adalah domain lokal
vhost_config = """
<VirtualHost *:80>
    ServerAdmin admin@siswa.local
    ServerName siswa.local
    DocumentRoot /var/www/siswa.local

    <Directory /var/www/siswa.local>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/siswa_error.log
    CustomLog ${APACHE_LOG_DIR}/siswa_access.log combined
</VirtualHost>
"""
# Simpan konfigurasi ke folder sites-available
with open("/etc/apache2/sites-available/siswa.local.conf", "w") as file:
    file.write(vhost_config)

# 6. Aktifkan virtual host siswa.local
os.system("a2ensite siswa.local.conf")

# 7. Restart Apache agar konfigurasi baru langsung aktif
os.system("systemctl reload apache2")

# 8. Tambahkan domain siswa.local ke file /etc/hosts
# Agar bisa diakses dari browser lokal tanpa DNS
with open("/etc/hosts", "a") as file:
    file.write("\n127.0.0.1 siswa.local\n")

# 9. Tampilkan pesan sukses di terminal
print("✅ Instalasi dan konfigurasi selesai!")
print("🌐 Buka browser dan akses: http://siswa.local")
