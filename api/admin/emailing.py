from flask import Blueprint, jsonify
from client.authentication import is_admin
from mails import test_match_email


emailing_blueprint = Blueprint(
    'emailing',
    __name__,
    template_folder='./templates'
)


@emailing_blueprint.route('/admin/emailing/ping', methods=['GET'])
@is_admin
def ping_pong():
    return jsonify(
        {
            'status': 'success',
            'message': 'pong'
        }
    )


@emailing_blueprint.route('/admin/emailing/test', methods=['GET'])
@is_admin
def test_emails():
    test_match_email()
    return jsonify(
        {
            'status': 'success',
            'message': 'pong'
        }
    )
