import os  # Modul untuk menjalankan perintah sistem Linux

# 1. Update daftar paket dan install Apache + PHP
# Apache = web server, PHP = bahasa pemrograman web
os.system("apt update && apt install apache2 php libapache2-mod-php -y")

# 2. Buat file index.php di folder web default
# Folder /var/www/html adalah tempat file web disimpan
konten_php = """
<?php
echo "<h1>Website Siswa TKJ</h1>";
echo "<p>Server aktif dan PHP berjalan!</p>";
echo "<p>Waktu server: " . date("d-m-Y H:i:s") . "</p>";
?>
"""
# Menulis file PHP ke folder web agar bisa diakses lewat browser
with open("/var/www/html/index.php", "w") as file:
    file.write(konten_php)

# 3. Restart Apache agar perubahan langsung aktif
os.system("systemctl restart apache2")

# 4. Tampilkan pesan sukses di terminal
print("✅ Web server aktif!")
print("🌐 Buka browser dan akses: http://localhost atau IP server")
