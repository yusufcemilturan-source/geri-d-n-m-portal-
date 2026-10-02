from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "gizli_anahtar"

# Geçici veri deposu
kullanicilar = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        islem = request.form.get("islem")
        email = request.form.get("email")
        sifre = request.form.get("sifre")

        if islem == "kayit":
            if not email or not sifre:
                flash("Lütfen alanları doldurun.", "error")
            else:
                kullanicilar[email] = sifre
                flash("Hesabınız oluşturuldu. Giriş yapabilirsiniz.", "success")

        elif islem == "giris":
            if email in kullanicilar and kullanicilar[email] == sifre and sifre != "":
                return "<h1>Giriş Başarılı! Hoş Geldiniz.</h1>"
            else:
                flash("E-posta veya şifre hatalı!", "error")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)