# Resep Render Drama — Love Is A Dangerous Game (Kaggle + WanGP)

Ditulis 15 Nov 2026 malam, sesudah 3 jam coba-coba di sesi Kaggle pertama.
Tujuannya: sesi berikut tinggal jalan, tanpa trial-and-error lagi.

## 1. Server WanGP

- Notebook Kaggle "Drama Ai", GPU 2x Tesla T4.
- Launch dari cell notebook: `python wgp.py --share --profile 4`
- **Profile 4 = benar untuk 2xT4** (default, recommended, dokumen resmi WanGP).
  **Profile 5 JANGAN dipakai** — fail-safe PALING LAMBAT.
- Link Gradio publik muncul di output cell launch (berubah tiap relaunch).
- Model Wan 2.2 TI2V-5B ~10 GB di `/kaggle/tmp/ckpts` — sesi baru harus unduh ulang
  kecuali dataset model sudah dibuat (lihat §5).

## 2. Setting render (per scene, lewat UI Gradio LANGSUNG — bukan CLI/headless)

- Mode: TI2V (Start with Image), model TI2V-5B
- Resolusi 832x480, 121 frames (5 detik), 50 steps
- Start image: upload guide image scene itu
  (`prompts/love-is-a-dangerous-game/episode-0X/scenes/scene-0Y-*.webp`)
- Prompt: dari `episode-0X.md` (teks scene + dialog)
- Negative prompt: `blurry, low quality, distorted face, extra fingers, deformed hands, watermark, text, logo`
- Seed: scene 1 = 1101 (scene berikut naik berurutan)
- Klik Generate, tunggu sampai selesai, verifikasi sebelum lanjut.

## 3. Verifikasi (WAJIB tiap scene)

- Frame pertama video HARUS cocok dengan guide image.
- Kalau frame pertama tidak cocok = start image tidak kepakai (text-only) → render ulang.
- Pelajaran 15 Nov: antrean headless dengan `image_mode=0` menghasilkan text-only
  (2 scene kebuang). Jangan pakai jalur headless/queue.zip lagi — UI langsung saja.

## 4. Kecepatan & anggaran waktu

- Profile 4: ~19 menit/scene → 1 episode (6 scene) ≈ 2 jam.
- Sesi Kaggle 15 Nov: mulai 18:37, berakhir ~01:20 WIB (±6 jam 45 menit).
- Urutan kerja (keputusan king): Ep 1–5 render → mix + upload YouTube → baru Ep 6–15.
- Cap serial Love: Ep 15 (prompt 16–43 ada, jangan render kecuali king minta).

## 5. Sesudah render

- Gabung per episode (ffmpeg concat) → `love-episode-01.mp4` … `love-episode-05.mp4`.
- Unduh ke PC, salin ke `~/workspace/goals/auto-youtube-shorts-tool/recap-episodes/`.
- Mix: dialog TTS di `recap-dubbing/love/` (30 file, urutan dari
  `recap-dubbing/love-dubbing-script.json`) + musik `recap-music/` di −18 s.d. −24 dB.
- Upload: `python3 upload-queue-recap.py` (antrean `hidden_files/upload-queue-recap.json`,
  thumbnail otomatis dari cover).
- Dataset model (hemat unduh sesi berikut): copy `/kaggle/tmp/ckpts` ke
  `/kaggle/working/wan22-model` → Quick Save → Output → New Dataset (privat).
