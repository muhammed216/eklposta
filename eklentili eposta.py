from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import smtplib

kullanici = 'muhammedsuleey@gmail.com'
sifre = 'fycrox1234'

alici = kullanici
baslik = 'Python gonderisi'
mesaj = 'deneme mesaji'

context = ssl.create_default_context()

port = 465
host = "smtp.gmail.com"

eposta_sunucu = smtplib.SMTP_SSL(host=host, port=port, context=context)
eposta_sunucu.login(kullanici, sifre)
eposta_sunucu.sendmail(kullanici, alici, mesaj)


posta = MIMEMultipart()
posta['from'] = kullanici
posta['to'] = kullanici
posta['subject'] = baslik



posta.attach(MIMEText(mesaj, 'plain'))
eklenti_dosya_ismi = "arjantin.jpg"


with(open(eklenti_dosya_ismi, 'rb'))as eklenti_dosyasi:
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((eklenti_dosyasi).read())
    encoders.encode_base64(payload)

    payload.add_header("Content-Decomposition", "attachment", filename=eklenti_dosya_ismi)
    posta.attach(payload)

    posta_str = posta.as_string()


port = 465
host = "smtp.gmail.com"

eposta_sunucu = smtplib.SMTP_SSL(host=host, port=port, context=context)
eposta_sunucu.login(kullanici, sifre)
eposta_sunucu.sendmail(kullanici, alici, posta_str)

from imap_tools import MailBox
posta_kutusu = MailBox('imap.gmail.com')
posta_kutusu.login(kullanici, sifre, initial_folder="INBOX")
import datetime
from imap_tools import AND
kriter = AND(date_gte=datetime.date(2024,1,30), from_=kullanici)
for msg in posta_kutusu.fetch(kriter):
    print(msg.text)

with  MailBox('imap.gmail.com').login(kullanici, sifre, initial_folder="INBOX") as posta_kutusu:
        kriter = AND(date_gte=datetime.date(2024, 1, 30), from_=kullanici)
        for msg in posta_kutusu.fetch(kriter):
            print(msg.text)


dosya_ismi = 'e-posta.ipynb'
def dosya_isminden_mail_bul(eposta_kutusu_param, dosya_ismi_param, kriter_param):
    for mesaj in eposta_kutusu_param.fetch(kriter):
        if mesaj.attachments:
            for ek in mesaj.attachments:
                if dosya_ismi_param == ek.filename:
                    return('{} isimli dosya, {} tarihli ve {} baslikli epostadir.'.format(
                        dosya_ismi_param,
                        mesaj.date_str,
                        mesaj.subject
                    ))
    return ('{} isimli dosya, eposta kutusunda bulunamadi.'.format(dosya_ismi_param))





