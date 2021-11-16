def handle_uploaded_file(user_file):
    with open('static/' + user_file.name, 'wb+') as f:
        for chunk in user_file.chunks():
            f.write(chunk)