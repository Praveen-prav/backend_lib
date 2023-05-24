from flask import Flask, jsonify, request, url_for
# import ssl

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    server_url = request.base_url
    books = [
        {
            'name': 'Book 1',
            'author': 'Author 1',
            'description': 'Description 1',
            'cover_image_path': server_url + url_for('static', filename='assets/images/book1.jpg'),
            'pdf_path': server_url + url_for('static', filename='assets/pdfs/book1.pdf')
        },
        {
            'name': 'Book 2',
            'author': 'Author 2',
            'description': 'Description 2',
            'cover_image_path': server_url + url_for('static', filename='assets/images/book2.jpg'),
            'pdf_path': server_url + url_for('static', filename='assets/pdfs/book2.pdf')
        },
        {
            'name': 'Book 3',
            'author': 'Author 3',
            'description': 'Description 3',
            'cover_image_path': server_url + url_for('static', filename='assets/images/book3.jpg'),
            'pdf_path': server_url + url_for('static', filename='assets/pdfs/book3.pdf')
        },
        {
            'name': 'Book 4',
            'author': 'Author 4',
            'description': 'Description 4',
            'cover_image_path': server_url + url_for('static', filename='assets/images/book4.jpg'),
            'pdf_path': server_url + url_for('static', filename='assets/pdfs/book4.pdf')
        },
        {
            'name': 'Book 5',
            'author': 'Author 5',
            'description': 'Description 5',
            'cover_image_path': server_url + url_for('static', filename='assets/images/book5.jpg'),
            'pdf_path': server_url + url_for('static', filename='assets/pdfs/book5.pdf')
        }
    ]
    return jsonify(books)

if __name__ == '__main__':
    # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    # context.load_cert_chain('cert.pem', 'key.pem')
    app.run()
