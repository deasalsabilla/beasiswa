from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Angkatan

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
    
def mahasiswa(request):
    return render(request, 'mahasiswa.html')