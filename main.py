# ==============================================================================
# STUDI KASUS: SISTEM PENGGAJIAN KARYAWAN (OOP PYTHON)
# ==============================================================================

# 1. SUPERCLASS
class Karyawan:
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.__gaji_pokok = gaji_pokok  # Private attribute (Encapsulation)

    # Getter: membaca gaji pokok
    @property # lock gaji_pokok menjadi read only
    def gaji_pokok(self) -> float:
        return self.__gaji_pokok

    # Setter: mengubah gaji pokok dengan validasi
    @gaji_pokok.setter 
    def gaji_pokok(self, nilai: float):
        if nilai <= 0:
            print(f"[Peringatan] Gaji pokok harus > 0, Nilai '{nilai}' ditolak.")
        else:
            self.__gaji_pokok = nilai
            print(f"[Sukses] Gaji pokok {self.nama} diubah menjadi Rp {nilai:,.2f}")

    def hitung_gaji_total(self) -> float:
        return self.__gaji_pokok

    def tampilkan_info(self):
        print(f"[{self.id_karyawan}] {self.nama} | Gaji Pokok: Rp {self.__gaji_pokok:,.2f} | Total: Rp {self.hitung_gaji_total():,.2f}")


# 2. SUBCLASS: KaryawanTetap (Inheritance)
class KaryawanTetap(Karyawan):
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float, tunjangan: float):
        super().__init__(nama, id_karyawan, gaji_pokok)  # Panggil constructor superclass
        self.tunjangan = tunjangan

    # Overriding: Gaji Pokok + Tunjangan
    def hitung_gaji_total(self) -> float:
        return self.gaji_pokok + self.tunjangan

    # Overriding: Menampilkan rincian karyawan tetap
    def tampilkan_info(self):
        print(f"[Tetap] {self.nama} ({self.id_karyawan}) | Gaji Pokok: Rp {self.gaji_pokok:,.2f} | Tunjangan: Rp {self.tunjangan:,.2f} | Total: Rp {self.hitung_gaji_total():,.2f}")


# 3. SUBCLASS: KaryawanKontrak (Inheritance)
class KaryawanKontrak(Karyawan):
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float, jam_lembur: int, tarif_lembur: float):
        super().__init__(nama, id_karyawan, gaji_pokok)  # Panggil constructor superclass
        self.jam_lembur = jam_lembur
        self.tarif_lembur = tarif_lembur

    # Overriding: Gaji Pokok + (Jam Lembur * Tarif Lembur)
    def hitung_gaji_total(self) -> float:
        return self.gaji_pokok + (self.jam_lembur * self.tarif_lembur)

    # Overriding: Menampilkan rincian karyawan kontrak
    def tampilkan_info(self):
        total_lembur = self.jam_lembur * self.tarif_lembur
        print(f"[Kontrak] {self.nama} ({self.id_karyawan}) | Gaji Pokok: Rp {self.gaji_pokok:,.2f} | Lembur ({self.jam_lembur} jam): Rp {total_lembur:,.2f} | Total: Rp {self.hitung_gaji_total():,.2f}")


# ==============================================================================
# MAIN PROGRAM (PENGUJIAN KODE)
# ==============================================================================
if __name__ == "__main__":
    # 1. Instansiasi objek
    karyawan1 = KaryawanTetap("Budi Santoso", "KT-001", 5_000_000, 1_500_000)
    karyawan2 = KaryawanKontrak("Siti Rahma", "KK-002", 4_000_000, 20, 50_000)

    # 2. Simpan ke dalam list
    daftar_karyawan = [karyawan1, karyawan2]

    # 3. Demonstrasi Polymorphism: panggil tampilkan_info() pada tiap objek di dalam list
    print("--- DEMONSTRASI POLYMORPHISM ---")
    for k in daftar_karyawan:
        k.tampilkan_info()

    # 4. Demonstrasi Encapsulation: coba set nilai tidak valid lalu nilai valid
    print("\n--- DEMONSTRASI ENCAPSULATION ---")
    karyawan1.gaji_pokok = -500_000   # Tidak valid (muncul peringatan)
    karyawan1.gaji_pokok = 6_000_000  # Valid (berhasil diubah)
    
    print("\nData setelah pembaruan:")
    karyawan1.tampilkan_info()
