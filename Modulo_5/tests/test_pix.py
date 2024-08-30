import sys
sys.path.append("../")

import pytest
import os
from payments.pix import Pix


def test_pix_create_payment():
    pix_instance = Pix()

    # Create payment
    data_payment_pix = pix_instance.create_payment(base_dir="../")

    assert "bank_payment_id" in data_payment_pix
    assert "qr_code_path" in data_payment_pix

    qr_code_path = data_payment_pix["qr_code_path"]
    assert os.path.isfile(f"../static/img/{qr_code_path}.png")
    
    