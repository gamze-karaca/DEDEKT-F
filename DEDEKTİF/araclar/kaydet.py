# araclar/kaydet.py — Dosya Kaydetme Yardımcısı

import os


def dosya_kaydet(oyun):
    """Mevcut bölüm notlarını .txt dosyasına kaydeder."""
    from veri import BOLUMLER
    bolum = BOLUMLER[oyun.bolum_idx]

    icerik = (
        f"=== Criminal Case: İstanbul Dosyaları ===\n"
        f"Bölüm {bolum['num']}: {bolum['title']}\n"
        f"Konum: {bolum['location']}\n\n"
        f"--- Toplanan Deliller ({len(oyun.envanter)}) ---\n"
        + "\n".join(f"  • {d}" for d in oyun.envanter)
        + f"\n\n--- Analiz Edilenler ({len(oyun.analiz_edilenler)}) ---\n"
        + "\n".join(f"  ✓ {a}" for a in oyun.analiz_edilenler)
        + f"\n\n--- Skor: {oyun.skor} puan ---\n"
    )

    klasor = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    yol = os.path.join(klasor, f"dosya_bolum{bolum['num']}.txt")
    with open(yol, "w", encoding="utf-8") as f:
        f.write(icerik)

    return yol
