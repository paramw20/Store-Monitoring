import secrets
from flask import Blueprint, jsonify, request, Response
from app.models import Report
from app.reports import generate_report, get_report_status_from_db, get_report_data_from_db

report_bp = Blueprint('report_bp', __name__, url_prefix='/api')

@report_bp.route('/trigger_report', methods=['POST'])
def trigger_report():
    try:
        report_id = secrets.token_urlsafe(16)
        generate_report(report_id)
        return jsonify({'report_id': report_id, 'message': 'Report generation triggered successfully'}), 200
    except Exception as e:
        return jsonify({'error_message': 'Failed to trigger report generation', 'error': str(e)}), 500

@report_bp.route('/get_report', methods=['GET'])
def get_report():
    try:
        report_id = request.args.get('report_id')
        if not report_id:
            return jsonify({'error': 'Missing report ID'}), 400

        report_status = get_report_status_from_db(report_id)
        if not report_status:
            return jsonify({'error': 'Invalid report ID'}), 400

        if report_status == 'Running':
            return jsonify({'status': 'Running'}), 200
        elif report_status == 'Complete':
            report_data = get_report_data_from_db(report_id)
            if report_data:
                return Response(report_data, mimetype='text/csv'), 200
            else:
                return jsonify({'error': 'Failed to retrieve report data'}), 400
        else:
            return jsonify({'error': 'Invalid report status'}), 400
    except Exception as e:
        return jsonify({'error_message': 'An error occurred while fetching the report', 'error': str(e)}), 500
