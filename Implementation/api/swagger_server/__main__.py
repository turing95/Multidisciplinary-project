#!/usr/bin/env python3

import connexion

from swagger_server import encoder

from flask import send_from_directory


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')

    @app.app.route('/images/<path:path>')
    def serve_path_images_as_static(path):
        return send_from_directory('../images', path)

    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Tourist app API'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
