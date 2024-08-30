import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self, base_dir=""):
        # criar o pagamento na instituição financeira
        bank_payment_id = str(uuid.uuid4())

        # codigo_copia_e_cola_123
        hash_payment = f'hash_payment_{bank_payment_id}'

        # qr code        
        img = qrcode.make(hash_payment)
        img.save(f"{base_dir}static/img/qr_code_payment_{bank_payment_id}.png")

        return {"bank_payment_id": bank_payment_id,
                "qr_code_path": f"qr_code_payment_{bank_payment_id}"}