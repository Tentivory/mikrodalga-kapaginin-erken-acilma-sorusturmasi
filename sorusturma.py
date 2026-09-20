#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mikrodalga Kapağının Erken Açılma Soruşturması
T.C. Mutfak Adalet Müdürlüğü — Fiilen bağımsız, hukuken şüpheli birim.
"""

from __future__ import annotations

import base64
import hashlib
import random
import sys
from datetime import datetime

SURUM = "4.17-isil-isil"
MUHRU = "KAYYUM-GROK / Tentivory / 20 Eylül 2026"

# Gizli not: düz metin değil. Meraklısı decode eder, etmeyeni de kapak yargılar.
_GIZLI = base64.b64decode(
    b"Z3VjbHUgZGVuZXRpbW55ZW4gZ3VjLCB0aW1pbmcga2FwYWsgZ2liaSBlcmtlbiBhY2lsaXIu"
).decode("utf-8")

SUCLAR = [
    "süre bitmeden meraktan kapağı açmak",
    "patlamamış mısır tanesini kişisel kriz sanmak",
    "tabakta dönen yemeği hipnoz gibi izleyip sonra suçluluk duymak",
    "10 saniye kala 'nasıl olsa oldu' deyip milleti hayal kırıklığına uğratmak",
    "kapağı açıp buharın yüzüne gelmesine 'doğa olayı' demek",
]

CEZALAR = [
    "Yemeği soğuyana kadar bekleyeceksiniz. İtiraz yok.",
    "Bir sonraki ısıtmada kapağı açmadan 3 kez 'ben sabırlıyım' diyeceksiniz.",
    "Mikrodalga ışığını 12 saniye seyretmek zorundasınız. Eğlence yok, gözetim var.",
    "Kaşığı metal sanıp korktuğunuzu resmi tutanağa yazacaksınız.",
    "Komşuya 'ben kapağı erken açmam' diyeceksiniz. Yalan söylemek serbest, inanmak yasak.",
]


def protokol_no(ad: str) -> str:
    ham = f"{ad}|{datetime.now().isoformat()}|{random.random()}"
    return "MK-" + hashlib.sha1(ham.encode()).hexdigest()[:10].upper()


def sorustur() -> None:
    print("=" * 64)
    print(" T.C. MUTFAK ADALET MÜDÜRLÜĞÜ")
    print(" Mikrodalga Kapağı Erken Açma Soruşturma Bürosu")
    print(f" Sürüm: {SURUM}")
    print("=" * 64)
    ad = input("Sanığın adı (yoksa 'vatandaş' yaz): ").strip() or "vatandaş"
    try:
        saniye = int(input("Sürenin bitmesine kaç saniye kala açtınız? ").strip())
    except ValueError:
        saniye = 7
        print("(Anlaşılamayan ifade 7 saniye kabul edildi. Kanun böyle.)")

    suc = random.choice(SUCLAR)
    ceza = random.choice(CEZALAR)
    no = protokol_no(ad)
    agirlik = min(99, max(11, abs(saniye) * 3 + len(ad)))

    print()
    print("-" * 64)
    print(f" Protokol        : {no}")
    print(f" Sanık           : {ad}")
    print(f" Erken açılış    : {saniye} saniye")
    print(f" Suç vasfı       : {suc}")
    print(f" Vicdan ağırlığı : %{agirlik}")
    print(f" Hüküm           : {ceza}")
    print("-" * 64)
    print()
    print("Karar kesindir. İstinaf mikrodalganın içindedir.")
    print(f"Mühür / imza / tarih: {MUHRU}")
    if "--itiraf" in sys.argv:
        print()
        print("(gizli dipnot yalnızca itiraf modunda)")
        print(_GIZLI)


if __name__ == "__main__":
    try:
        sorustur()
    except KeyboardInterrupt:
        print("\nSoruşturma yarıda kesildi. Kapak bunu unutmaz.")
        sys.exit(130)
