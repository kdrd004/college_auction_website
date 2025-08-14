from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dictionary to store Excel file paths for different auction types
EXCEL_FILES = {
    'Classical Dance': 'classical_dance_results.xlsx',
    'Classical Singing': 'classical_singing_results.xlsx',
    'Folk Singing': 'folk_singing_results.xlsx',
    'Western Singing': 'western_singing_results.xlsx',
    'Lazy Dance': 'lazy_dance_results.xlsx',
    'Retro Kannada': 'retro_kannada_results.xlsx',
    'Auction 2': 'auction2_results.xlsx',
    'Western Dance': 'western_dance_results.xlsx'
}

# Define the columns for all Excel sheets
COLUMNS = [
    'Player Name', 'Position', 'Status', 'Event', 'Bid Amount', 
    'Team Name', 'Photo Associated', 'Sold To Group', 'Timestamp'
]

def create_excel_if_not_exists(event_type):
    """Create Excel file if it doesn't exist for the given event type"""
    excel_file = EXCEL_FILES.get(event_type)
    if not excel_file:
        return False, f"Invalid event type: {event_type}"
    
    if not os.path.exists(excel_file):
        try:
            df = pd.DataFrame(columns=COLUMNS)
            df.to_excel(excel_file, index=False)
            return True, f"Created new Excel file: {excel_file}"
        except Exception as e:
            return False, f"Error creating Excel file: {str(e)}"
    return True, "Excel file already exists"

@app.route('/')
def serve_html():
    return send_from_directory('.', 'classicalauction.html')

@app.route('/save-player-status', methods=['POST'])
def save_player_status():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['playerName', 'position', 'status', 'event', 'bidAmount', 'teamName', 'photoAssociated']
        for field in required_fields:
            if field not in data:
                return jsonify({'success': False, 'message': f'Missing required field: {field}'})
        
        # Get the Excel file for the event type
        event_type = data['event']
        excel_file = EXCEL_FILES.get(event_type)
        
        if not excel_file:
            return jsonify({'success': False, 'message': f'Invalid event type: {event_type}'})
        
        # Create Excel file if it doesn't exist
        success, message = create_excel_if_not_exists(event_type)
        if not success:
            return jsonify({'success': False, 'message': message})
        
        # Read existing data
        try:
            df = pd.read_excel(excel_file)
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error reading Excel file: {str(e)}'})
        
        # Create new row
        new_row = pd.DataFrame([{
            'Player Name': data['playerName'],
            'Position': data['position'],
            'Status': data['status'],
            'Event': data['event'],
            'Bid Amount': data['bidAmount'],
            'Team Name': data['teamName'],
            'Photo Associated': data['photoAssociated'],
            'Sold To Group': data.get('soldToGroup', ''),
            'Timestamp': data.get('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        }])
        
        # Append new row
        df = pd.concat([df, new_row], ignore_index=True)
        
        # Save back to Excel
        df.to_excel(excel_file, index=False)
        
        return jsonify({
            'success': True,
            'message': f'Successfully saved to {excel_file}',
            'data': data
        })
        
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'})

if __name__ == '__main__':
    # Create Excel files for all event types if they don't exist
    for event_type in EXCEL_FILES.keys():
        success, message = create_excel_if_not_exists(event_type)
        print(message)
    
    app.run(debug=True) 