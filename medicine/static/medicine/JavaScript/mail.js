const http = require('http');
const nodemailer = require('nodemailer');

// HTTP sunucusunu oluştur
const server = http.createServer((req, res) => {
    if (req.url === '/send-email' && req.method === 'POST') {
        // İsteği işle
        let body = '';
        req.on('data', (chunk) => {
            body += chunk.toString();
        });
        req.on('end', () => {
            // İstek verisini JSON'a çevir
            const requestData = JSON.parse(body);

            // E-posta gönderme işlemini gerçekleştir
            sendEmail(requestData.email);

            // Yanıtı gönder
            res.writeHead(200, {'Content-Type': 'application/json'});
            res.end(JSON.stringify({message: 'Email sent successfully.'}));
        });
    } else {
        res.writeHead(404, {'Content-Type': 'text/plain'});
        res.end('404 Not Found');
    }
});

// SMTP bilgileri
const smtpServer = "mail.kurumsaleposta.com";
const smtpUsername = "reservation@gokbartourism.com";
const smtpPassword = "yfxc5G9=i4.XQ_Y";

// E-posta gönderme işlevi
function sendEmail(recipientEmail) {
    const transporter = nodemailer.createTransport({
        host: smtpServer,
        port: 465,
        secure: true,
        auth: {
            user: smtpUsername,
            pass: smtpPassword
        }
    });

    const mailOptions = {
        from: smtpUsername,
        to: recipientEmail,
        subject: "Reservation is confirmed",
        text: "Your reservation is confirmed. Reservation details: [Buraya rezervasyon detayları eklenecek]"
    };

    transporter.sendMail(mailOptions, function(error, info){
        if (error) {
            console.error(error);
        } else {
            console.log('Email sent: ' + info.response);
        }
    });
}

// Sunucuyu dinlemeye başla
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(Server is running on port ${PORT});
});