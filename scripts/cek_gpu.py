"""Cek cepat GPU + torch. Jalankan sebagai cell pertama di Kaggle/Colab.

Harapan di Kaggle T4 x2: 2 GPU Tesla T4, torch.cuda.is_available() == True.
Kalau False, Accelerator masih None — cek Settings notebook.
"""
import torch

print("torch:", torch.__version__)
print("cuda available:", torch.cuda.is_available())
print("device count:", torch.cuda.device_count())
for i in range(torch.cuda.device_count()):
    print(f"GPU {i}:", torch.cuda.get_device_name(i))
    print("  memory:", round(torch.cuda.get_device_properties(i).total_memory / 1e9, 1), "GB")
