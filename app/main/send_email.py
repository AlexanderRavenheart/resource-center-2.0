from django.core import mail

def contacts_form(name, email, message):
    connection = mail.get_connection()
    connection.open()

    email = mail.EmailMessage(
        'OpenRA Resource Center - Contacts form',
        'Name: %s\nEmail: %s\nMessage: %s\n' % (name, email, message),
        settings.ADMIN_EMAIL_FROM,
        [settings.ADMIN_EMAIL_TO],
        connection=connection)

    email.send()
    connection.close()
