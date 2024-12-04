from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Angkatan, Prodi, Mahasiswa

def home(request):
    return render(request, 'index.html')

def angkatan(request):
    # Ambil semua data dari model Angkatan
    data_angkatan = Angkatan.objects.all()
    return render(request, 'angkatan.html', {'data_angkatan': data_angkatan})

def tambah_angkatan(request):
    if request.method == 'POST':
        tahun_angkatan = request.POST.get('tahun_angkatan')

        if not tahun_angkatan:
            messages.error(request, "Tahun angkatan tidak boleh kosong.")
            return redirect('angkatan')

        try:
            tahun_angkatan = int(tahun_angkatan)
        except ValueError:
            messages.error(request, "Tahun angkatan harus berupa angka.")
            return redirect('angkatan')

        if tahun_angkatan < 1900 or tahun_angkatan > 2100:  # Validasi rentang tahun
            messages.error(request, "Tahun angkatan harus antara 1900 dan 2100.")
            return redirect('angkatan')

        # Cek apakah tahun angkatan sudah ada
        if Angkatan.objects.filter(angkatan=tahun_angkatan).exists():
            messages.error(request, f"Tahun angkatan {tahun_angkatan} sudah ada.")
            return redirect('angkatan')
        else:
            # Simpan data ke database
            Angkatan.objects.create(angkatan=tahun_angkatan)
            messages.success(request, f"Tahun angkatan {tahun_angkatan} berhasil ditambahkan.")
            return redirect('angkatan')  # Redirect setelah berhasil menambahkan

    return render(request, 'tambah_angkatan.html')

def edit_angkatan(request, id):
    # Ambil data angkatan berdasarkan ID
    angkatan = get_object_or_404(Angkatan, id=id)

    if request.method == 'POST':
        tahun_angkatan = request.POST.get('tahun_angkatan')

        if not tahun_angkatan:
            messages.error(request, "Tahun angkatan tidak boleh kosong.")
            return render(request, 'edit_angkatan.html', {'angkatan': angkatan})

        try:
            tahun_angkatan = int(tahun_angkatan)
        except ValueError:
            messages.error(request, "Tahun angkatan harus berupa angka.")
            return render(request, 'edit_angkatan.html', {'angkatan': angkatan})

        if tahun_angkatan < 1900 or tahun_angkatan > 2100:  # Validasi rentang tahun
            messages.error(request, "Tahun angkatan harus antara 1900 dan 2100.")
            return render(request, 'edit_angkatan.html', {'angkatan': angkatan})

        # Cek apakah tahun angkatan sudah ada dan bukan data yang sedang diedit
        if Angkatan.objects.filter(angkatan=tahun_angkatan).exclude(id=id).exists():
            messages.error(request, f"Tahun angkatan {tahun_angkatan} sudah ada.")
        else:
            # Update data angkatan
            angkatan.angkatan = tahun_angkatan
            angkatan.save()
            messages.success(request, "Data angkatan berhasil diperbarui.")
            return redirect('angkatan')  # Redirect kembali ke halaman edit

    return render(request, 'edit_angkatan.html', {'angkatan': angkatan})

def delete_angkatan(request, id):
    angkatan = get_object_or_404(Angkatan, id=id)
    if request.method == 'POST':
        angkatan.delete()
        messages.success(request, 'Data Angkatan berhasil dihapus!')
        return redirect('angkatan')  # Kembali ke halaman tabel
    
def prodi(request):
    # Ambil semua data dari model Prodi
    data_prodi = Prodi.objects.all()
    return render(request, 'prodi.html', {'data_prodi': data_prodi})

def tambah_prodi(request):
    if request.method == 'POST':
        prodi_name = request.POST.get('prodi')

        if not prodi_name:
            messages.error(request, "Nama program studi tidak boleh kosong.")
            return render(request, 'tambah_prodi.html')

        if len(prodi_name) > 25:  # Validasi panjang nama prodi
            messages.error(request, "Nama program studi tidak boleh lebih dari 25 karakter.")
            return render(request, 'tambah_prodi.html')

        # Cek apakah program studi sudah ada
        if Prodi.objects.filter(prodi__iexact=prodi_name).exists():
            messages.error(request, f"Program studi '{prodi_name}' sudah ada.")
        else:
            # Simpan data ke database
            Prodi.objects.create(prodi=prodi_name)
            messages.success(request, f"Program studi '{prodi_name}' berhasil ditambahkan.")
            return redirect('prodi')  # Redirect setelah berhasil menambahkan

    return render(request, 'tambah_prodi.html')

def edit_prodi(request, id):
    # Ambil data prodi berdasarkan ID
    prodi = get_object_or_404(Prodi, id=id)

    if request.method == 'POST':
        prodi_name = request.POST.get('prodi')

        if not prodi_name:
            messages.error(request, "Nama program studi tidak boleh kosong.")
            return render(request, 'edit_prodi.html', {'prodi': prodi})

        if len(prodi_name) > 25:
            messages.error(request, "Nama program studi tidak boleh lebih dari 25 karakter.")
            return render(request, 'edit_prodi.html', {'prodi': prodi})

        # Cek apakah nama program studi sudah ada dan bukan data yang sedang diedit
        if Prodi.objects.filter(prodi__iexact=prodi_name).exclude(id=id).exists():
            messages.error(request, f"Program studi '{prodi_name}' sudah ada.")
        else:
            # Update data
            prodi.prodi = prodi_name
            prodi.save()
            messages.success(request, "Data program studi berhasil diperbarui.")
            return redirect('prodi')  # Redirect ke halaman daftar prodi

    return render(request, 'edit_prodi.html', {'prodi': prodi})

def hapus_prodi(request, id):
    # Ambil data prodi berdasarkan ID
    prodi = get_object_or_404(Prodi, id=id)

    if request.method == 'POST':  # Pastikan penghapusan dilakukan melalui metode POST
        prodi.delete()
        messages.success(request, f"Program studi '{prodi.prodi}' berhasil dihapus.")
        return redirect('prodi')  # Redirect ke halaman daftar prodi

    return render(request, 'hapus_prodi.html', {'prodi': prodi})

def mahasiswa(request):
    # Ambil semua data mahasiswa
    mahasiswa_list = Mahasiswa.objects.select_related('prodi', 'angkatan').all()

    context = {
        'mahasiswa_list': mahasiswa_list,
    }
    return render(request, 'mahasiswa.html', context)

def tambah_mahasiswa(request):
    if request.method == "POST":
        nim = request.POST.get("nim")
        nama = request.POST.get("nama")
        prodi_id = request.POST.get("prodi")
        angkatan_id = request.POST.get("angkatan")

        # Validasi input
        if not nim or not nama or not prodi_id or not angkatan_id:
            messages.error(request, "Semua field harus diisi.")
            return redirect("tambah_mahasiswa")

        try:
            # Ambil instance Prodi dan Angkatan berdasarkan ID
            prodi = Prodi.objects.get(id=prodi_id)
            angkatan = Angkatan.objects.get(id=angkatan_id)

            # Simpan data mahasiswa
            mahasiswa = Mahasiswa(nim=nim, nama=nama, prodi=prodi, angkatan=angkatan)
            mahasiswa.save()

            messages.success(request, "Mahasiswa berhasil ditambahkan.")
            return redirect("mahasiswa")  # Ganti dengan nama URL yang sesuai
        except Prodi.DoesNotExist:
            messages.error(request, "Program Studi tidak ditemukan.")
        except Angkatan.DoesNotExist:
            messages.error(request, "Tahun Angkatan tidak ditemukan.")
        except Exception as e:
            messages.error(request, f"Terjadi kesalahan: {e}")
    
    # Handle GET request
    angkatan_list = Angkatan.objects.all()  # Ambil semua data Angkatan
    prodi_list = Prodi.objects.all()  # Ambil semua data Prodi

    context = {
        'angkatan_list': angkatan_list,
        'prodi_list': prodi_list,
    }
    return render(request, 'tambah_mahasiswa.html', context)

def edit_mahasiswa(request, id):
    # Ambil data mahasiswa berdasarkan ID, atau kembalikan 404 jika tidak ditemukan
    mahasiswa = get_object_or_404(Mahasiswa, id=id)

    if request.method == "POST":
        nim = request.POST.get("nim")
        nama = request.POST.get("nama")
        prodi_id = request.POST.get("prodi")
        angkatan_id = request.POST.get("angkatan")

        # Validasi input
        if not nim or not nama or not prodi_id or not angkatan_id:
            messages.error(request, "Semua field harus diisi.")
            return redirect("edit_mahasiswa", id=id)
        
        if len(nim) > 8:
            messages.error(request, "NIM tidak boleh lebih dari 8 karakter.")
            return redirect("edit_mahasiswa", id=id)

        try:
            # Update data mahasiswa
            mahasiswa.nim = nim
            mahasiswa.nama = nama
            mahasiswa.prodi = Prodi.objects.get(id=prodi_id)
            mahasiswa.angkatan = Angkatan.objects.get(id=angkatan_id)
            mahasiswa.save()

            messages.success(request, "Data mahasiswa berhasil diperbarui.")
            return redirect("mahasiswa")  # Ganti dengan nama URL daftar mahasiswa
        except Prodi.DoesNotExist:
            messages.error(request, "Program Studi tidak ditemukan.")
        except Angkatan.DoesNotExist:
            messages.error(request, "Tahun Angkatan tidak ditemukan.")
        except Exception as e:
            messages.error(request, f"Terjadi kesalahan: {e}")

    # Ambil data Prodi dan Angkatan untuk select option
    prodi_list = Prodi.objects.all()
    angkatan_list = Angkatan.objects.all()

    context = {
        'mahasiswa': mahasiswa,
        'prodi_list': prodi_list,
        'angkatan_list': angkatan_list,
    }
    return render(request, 'edit_mahasiswa.html', context)

def hapus_mahasiswa(request, id):
    # Ambil data mahasiswa berdasarkan ID atau kembalikan 404 jika tidak ditemukan
    mahasiswa = get_object_or_404(Mahasiswa, id=id)

    try:
        # Hapus data mahasiswa
        mahasiswa.delete()
        messages.success(request, "Data mahasiswa berhasil dihapus.")
    except Exception as e:
        messages.error(request, f"Terjadi kesalahan: {e}")
    
    # Redirect ke halaman daftar mahasiswa
    return redirect("mahasiswa")  # Ganti dengan nama URL daftar mahasiswa