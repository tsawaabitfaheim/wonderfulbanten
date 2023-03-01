from flask import Flask, render_template, request, jsonify
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    phonenumber = request.form['phonenumber']
    nationality = request.form['nationality']
    subject = request.form['subject']
    message = request.form['message']

    # Create a SendGrid message object
    message = Mail(
        from_email=email,
        to_emails='tsawaabit.n@gmail.com',  # Replace with your email address
        subject=subject,
        html_content=message)

    try:
        # Send the message using the SendGrid API key
        sg = SendGridAPIClient(api_key='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')  # Replace with your SendGrid API key
        response = sg.send(message)

        # Return a success response
        return jsonify({'success': True})
    except Exception as e:
        # If there was an error sending the message, return an error response
        error_message = str(e)
        return jsonify({'success': False, 'error': error_message})
