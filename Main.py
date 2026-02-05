import yagmail

class EmailService:
    def __init__(self, correo, password):
        self.yag = yagmail.SMTP(correo, password)

    def enviar(self, destinatarios, asunto, cuerpo):
        self.yag.send(
            to=destinatarios,
            subject=asunto,
            contents=cuerpo
        )


def construir_mensaje(integrantes, repo_url):
    mensaje = "Integrantes del equipo:\n"
    for integrante in integrantes:
        mensaje += f"- {integrante}\n"

    mensaje += f"\nRepositorio del proyecto:\n{repo_url}"
    return mensaje


if __name__ == "__main__":
    correo = "jherrerat4@ucentral.edu.co"
    password_app = "droe bxko cjnn vvnl"

    integrantes = [
        "Jean Marco Herrera Torres",
        "Nelson Nicolas Cruz Capella"
    ]

    repo_url = "https://github.com/JHerrerat7/MensajeViaCorreoElectronico_Python.git"
    destinatarios = ["gbricenor@ucentral.edu.co"]

    servicio = EmailService(correo, password_app)
    mensaje = construir_mensaje(integrantes, repo_url)

    servicio.enviar(
        destinatarios,
        "Entrega ejercicio – Envío de correo",
        mensaje
    )

    print("Correo enviado correctamente")
