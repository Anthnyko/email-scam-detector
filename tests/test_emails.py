from src.predict import classify_email

emails = ["Hi Anthony, just confirming our meeting tomorrow at 10am. Let me know if you need the Zoom link again."
, "Your account has been compromised. Click here immediately to verify your identity and avoid suspension."
, "Congratulations! You’ve been selected for a $500 Amazon gift card. Just complete this short survey."
, "Your order #12345 has shipped. Track your package here: www.store.com/track"
, "Dear user, we noticed unusual activity in your bank account. Please login here to secure it: http://fakebank-login.com"
]

for i, email in enumerate(emails):
    print(f"Email {i+1}: {classify_email(email)}")