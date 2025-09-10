import requests

USEPLUNK_API_URL = "https://api.useplunk.com/v1/send"
USEPLUNK_API_KEY = "sk_e018919f0784429c320ea75de1a997e4e665a39395160a5c"

def send_welcome_email(user_email, fname):
    """
    Envoie un email de bienvenue via l'API UsePlunk.
    """
    payload = {
        "to": user_email,
        "subject": "Bienvenue sur Ita RH !",
        "body": f"Bonjour {fname},\n\nBienvenue sur Ita RH ! Votre compte a été créé avec succès.\n\nCordialement,\nL'équipe Ita RH"
    }
    
    headers = {
        "Authorization": f"Bearer {USEPLUNK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(USEPLUNK_API_URL, json=payload, headers=headers)
    
    if response.status_code != 200:
        print(f"Erreur lors de l'envoi de l'email : {response.text}")
    else:
        print(f"Email envoyé à {user_email}")
