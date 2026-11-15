# Drama AI Gratis — Wan 2.2 di Kaggle (Wan2GP)

Bikin drama AI gaya Seedance / Higgsfield, tapi **gratis, tanpa watermark, dan boleh komersial**
(lisensi Apache-2.0). Modelnya Wan 2.2 open-source dari Alibaba.

Repo ini khusus **Kaggle** — GPU gratis T4 x2, ~30 jam/minggu.
Untuk Colab, lihat repo terpisah (akan dibuat menyusul).

> Status: template. Langkah-langkahnya disusun dari dokumentasi resmi Kaggle dan
> notebook komunitas Wan2GP. **Belum diuji live di T4 oleh penulis** (sandbox penulis
> tidak punya GPU). Kalau ada cell yang error, kirim screenshot error-nya.

## Kenapa Kaggle?

- Sandbox Muse: tanpa GPU, RAM 7,7 GB.
- InstaBox (`friday` / `jarvis` / `vision`): 4 vCPU / 8 GB RAM / 20 GB disk, tanpa GPU,
  plus auto-suspend 30 menit idle dan max-run 480 menit di Free.
- Wan 2.2 TI2V-5B butuh 6–8 GB VRAM, dan RAM sistem minimal 24 GB.
- Kaggle memberi **T4 x2 (~15–16 GB VRAM tiap kartu), RAM ~29 GB, sesi maks 12 jam,
  kuota ~30 jam GPU/minggu** — cukup untuk render batch drama.

Yang muat di T4:

- ✅ **Wan 2.2 TI2V-5B (Text+Image-to-Video), 480p, 5 detik** — ini yang dipakai di sini.
  Model ~10 GB, 1 klip 5 detik sekitar 15–25 menit di T4.
- ⚠️ Wan 2.2 14B — hanya GGUF Q4/Q5, kalau tidak VRAM habis.
- ❌ 14B FP16 720p — butuh 24 GB+ VRAM, bukan untuk free tier.

## Alur drama

1. **Naskah dulu.** 1 episode = 6 scene, tiap scene 5 detik.
   Contoh lengkap: [`prompts/mamang-ai/episode-01-balas-dendam.md`](prompts/mamang-ai/episode-01-balas-dendam.md).
2. **Kunci karakter.** Bikin 1 foto referensi karakter, lalu semua scene pakai
   **image-to-video** dari foto itu. Jangan text-to-video terus — mukanya ganti-ganti.
3. **Render per scene di Kaggle**, download sebelum sesi habis.
4. **Edit di CapCut desktop**: susun 6 klip, tambah subtitle bakar, musik, SFX.

## Langkah demi langkah

### 0. Siapkan akun
1. Buat akun di Kaggle, lalu **verifikasi nomor HP** di Settings. Wajib — GPU dan
   internet baru kebuka kalau HP sudah terverifikasi.
2. Cek sisa kuota GPU di Settings (~30 jam/minggu).

### 1. Import notebook
File: [`wan2gp_kaggle.ipynb`](wan2gp_kaggle.ipynb)

Di Kaggle: **Create > New Notebook > File > Import Notebook**, upload file itu.
Notebook ini mengarahkan model ke `/kaggle/tmp` supaya tidak memenuhi folder kerja 20 GB.

### 2. Nyalakan GPU + Internet
Panel kanan **Settings**:
- **Accelerator > GPU T4 x2**
- **Internet > On**

Sesi akan restart begitu accelerator diganti. Cek GPU di cell pertama:
```
!nvidia-smi
```
Harus muncul 2x Tesla T4.

### 3. Jalankan cell dari atas ke bawah
1. **Download Wan2GP** — clone `deepbeepmeep/Wan2GP` ke `/kaggle/working`.
2. **Install requirements** — `pip install -r requirements.txt` (5–10 menit).
3. **Pindah path model ke `/kaggle/tmp`** — symlink `ckpts` ke `/kaggle/tmp/ckpts`
   dan cache Hugging Face ke `/kaggle/tmp/hf`. Wajib jalan **sebelum** launch.
4. **Launch Wan2GP** — `python wgp.py --share --profile 5`, klik link Gradio publik.

### 4. Generate di Gradio
1. Pilih model **Wan 2.2 TI2V-5B / FastWan**, **480p**, **5 detik**.
2. Prompt + gambar referensi dari `prompts/mamang-ai/episode-01-balas-dendam.md`.
3. Render **1 scene dulu** untuk tes, baru batch 6 scene dalam sesi yang sama.
4. Download semua hasil dari `/kaggle/working` **sebelum sesi habis (maks 12 jam)**.

## File di repo ini

```
.
├── README.md
├── wan2gp_kaggle.ipynb           # notebook utama — import ke Kaggle
├── prompts/
│   ├── mamang-ai/
│   │   ├── episode-01-balas-dendam.md
│   │   └── episode-02-pernikahan-palsu.md
│   │       └── scenes/              # gambar awal scene Ep 02 (.webp)
│   └── love-is-a-dangerous-game/  # 43 episode, episode-01.md s.d. episode-43.md
├── scripts/
│   └── cek_gpu.py                 # cek GPU + torch
├── LICENSE                        # Apache-2.0
└── .gitignore
```

## Troubleshooting

| Gejala | Perbaiki |
|---|---|
| `nvidia-smi` tidak menemukan GPU | Settings → Accelerator → GPU T4 x2, tunggu restart |
| `pip install` gagal | Settings → Internet → On |
| Disk penuh saat download model | Pastikan cell symlink `/kaggle/tmp` jalan sebelum launch |
| `CUDA out of memory` | Ganti ke TI2V-5B, 480p, profile 5 — jangan 14B FP16 |
| Muka karakter beda tiap scene | Pakai image-to-video + foto referensi yang sama |

## Kredit

- Wan 2.2 — Alibaba, Apache-2.0.
- Wan2GP — `deepbeepmeep/Wan2GP`.
- Pola Kaggle `/kaggle/tmp` — terinspirasi notebook komunitas `jigs10/wan2gp-kaggle`.

Repo ini bukan afiliasi resmi Wan, Wan2GP, atau Kaggle.
Gunakan sesuai Terms of Service Kaggle (free tier untuk personal use).
