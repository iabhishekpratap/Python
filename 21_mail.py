import smtplib

hostname='smtp.gmail.com'
email = "creatorapsingh@gmail.com"
password = "cgolivkhnpuotzqn" 

with smtplib.SMTP(host=hostname) as connection: #client session connected to SMTP server.
    connection.starttls() #Upgrades the connection to a secure, encrypted using TLS
    connection.login(user=email, password=password) #Logging in to the SMTP Server
    
    #sending mail
    connection.sendmail(
        from_addr=email,
        to_addrs="selfassest@gmail.com",

        msg="this is the test mail"
    )

print("email send succsessfully")