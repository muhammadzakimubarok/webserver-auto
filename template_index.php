<?php
date_default_timezone_set("Asia/Jakarta"); // Set zona waktu ke WIB

// Data biodata siswa
$nama = "Nama Lengkap Siswa";
$kelas = "XII TKJ 1";
$jurusan = "Teknik Komputer dan Jaringan";
$waktu = date("d-m-Y H:i:s");
?>

<!DOCTYPE html>
<html>
<head>
    <title>Website Siswa TKJ</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f0f0; padding: 20px; }
        h1 { color: #2c3e50; }
        table { border-collapse: collapse; width: 50%; background: #fff; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #3498db; color: white; }
    </style>
</head>
<body>
    <h1>Selamat Datang di Website Siswa TKJ</h1>
    <p>Website ini dibuat otomatis menggunakan Python dan PHP di Debian 11.</p>
    <p><strong>Waktu Server:</strong> <?= $waktu ?></p>

    <h2>Biodata Siswa</h2>
    <table>
        <tr><th>Nama</th><td><?= $nama ?></td></tr>
        <tr><th>Kelas</th><td><?= $kelas ?></td></tr>
        <tr><th>Jurusan</th><td><?= $jurusan ?></td></tr>
    </table>
</body>
</html>
