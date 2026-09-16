# 1º projeto em python
import qrcode


def main():
    url = input("Digite sua url: ").strip()
    img = qrcode.make(url)
    salvar_qrcode(img)
    print("QrCode produzido com sucesso!")


def salvar_qrcode(img):
    titulo = input("Digite o título(Enter para skip): ").strip()
    if titulo == "":
        img.save("QrCode.png")
    else:
        img.save(f"{titulo}.png")


if __name__ == "__main__":
    main()
