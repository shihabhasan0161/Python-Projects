# Automated Email Sender

A Python application that sends automated emails with text, images, and attachments on a scheduled interval using SMTP.

## Features

- Send emails with subject and body text
- Attach multiple images to emails
- Attach files (PDF, documents, etc.) to emails
- Schedule emails to send at regular intervals
- Secure credentials using environment variables
- Limit email sends to a maximum number of runs

## Installation

1. Clone this repo
    ```bash
    git clone https://github.com/shihabhasan0161/Python-Projects/tree/main/automatedemailsender.git
    ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your SMTP credentials (use `.env.example` as a template):
   ```
   SMTP_SERVER=
   SMTP_PORT=
   SMTP_EMAIL=
   SMTP_USERNAME=
   SMTP_PASSWORD=
   ```

## Configuration

### Setting Up SMTP

1. Choose an SMTP provider (e.g., Brevo, Gmail, Outlook)
2. Get your SMTP credentials from the provider
3. Update the `.env` file with:
   - `SMTP_SERVER`: Your provider's SMTP server address
   - `SMTP_PORT`: Usually 587 (for TLS) or 465 (for SSL)
   - `SMTP_EMAIL`: The email address sending the emails
   - `SMTP_USERNAME`: Your login username
   - `SMTP_PASSWORD`: Your login password

### Setting Up Schedule

Edit the scheduling line in `main.py`:

```python
schedule.every(5).seconds.do(send_mail)  # Send every 5 seconds
```

Common schedule options:
- `schedule.every(10).seconds.do(send_mail)`
- `schedule.every(5).minutes.do(send_mail)`
- `schedule.every(1).hours.do(send_mail)`
- `schedule.every().day.at("10:30").do(send_mail)`

You can also change `max_run` to limit how many times emails are sent:
```python
max_run = 5  # Send maximum 5 emails before stopping
```

## Usage

Run the application:
```bash
python main.py
```

Customize the email in the `send_mail()` function:
```python
msg = main(
    "Your Subject",
    "Your email body text",
    r"C:\path\to\image.jpg",  # Optional: image path(s)
    r"C:\path\to\file.pdf"    # Optional: attachment path(s)
)
```

## Dependencies

- `python-dotenv` – Load environment variables from `.env` file
- `schedule` – Schedule tasks at regular intervals
- Python built-in modules: `smtplib`, `email`, `os`, `time`

## Notes

- This example uses Brevo SMTP; you can use any SMTP provider
- Store sensitive credentials in `.env` file, never commit it to version control
- The `.gitignore` file already excludes the `.env` file
- Multiple images and attachments can be passed as lists

---

Happy emailing! 📬