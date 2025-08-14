# College Auction Fest

A comprehensive web-based auction management system for college events, featuring multiple auction categories with real-time bidding and data management capabilities.

## 🎯 Project Overview

This project is a full-stack auction management system designed for college festivals and events. It provides an interactive web interface for conducting auctions across various categories including dance, singing, and sports events. The system includes real-time bidding, player management, and automated Excel data export functionality.

## 🏗️ Project Structure

```
college-auction-fest/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── project-info.json        # Project metadata
├── index.html               # Main landing page with navigation
├── server.py                # Flask backend server for data management
├── host.py                  # Simple HTTP server for static file hosting
├── *.html                   # Individual auction pages for different events
├── assets/                  # Organized assets directory
│   ├── css/
│   │   └── styles.css       # Main stylesheet
│   ├── images/              # All images and photos
│   ├── js/                  # JavaScript files (if any)
│   └── logos/               # Team logos
└── *.xlsx                   # Excel files for auction results (generated)
```

## 🎭 Auction Categories

The system supports multiple auction categories:

### Dance Events
- **Classical Dance** (`classicaldanceauction.html`)
- **Lazy Dance** (`lazydanceauction.html`)
- **Retro Kannada Dance** (`retrokannadaauction.html`)
- **Western Dance** (`westerndanceauction.html`)
- **Tribal Folk Dance** (`tribalfolkdanceauction.html`)

### Singing Events
- **Classical Singing** (`singingclassical.html`)
- **Folk Singing** (`singingfolk.html`)
- **Western Singing** (`singingwestern.html`)

### Sports Events
- Various sports categories with team logos and player images

## 🚀 Features

### Frontend Features
- **Modern UI Design**: Animated gradient backgrounds with geometric patterns
- **Responsive Design**: Bootstrap-based responsive layout
- **Interactive Bidding Interface**: Real-time bid tracking and status updates
- **Image Gallery**: Player photos and team logos display
- **Navigation System**: Easy switching between different auction categories

### Backend Features
- **Flask REST API**: RESTful endpoints for data management
- **Excel Integration**: Automatic Excel file generation and data export
- **CORS Support**: Cross-origin resource sharing enabled
- **Data Validation**: Input validation and error handling
- **Timestamp Tracking**: Automatic timestamp generation for all transactions

### Data Management
- **Player Information**: Name, position, status, event category
- **Bidding Data**: Bid amounts, team assignments, sale status
- **Photo Association**: Links players to their images
- **Team Management**: Team assignments and group tracking

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5.3.0
- **Backend**: Python Flask
- **Data Storage**: Excel files (pandas)
- **Server**: HTTP Server (Python built-in) / Flask development server
- **Dependencies**: Flask, Flask-CORS, pandas

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## 🔧 Installation & Setup

### 1. Clone or Download the Project
```bash
# If using git
git clone <repository-url>
cd college-auction-fest

# Or simply download and extract the project folder
```

### 2. Install Python Dependencies
```bash
pip install flask flask-cors pandas openpyxl
```

### 3. Run the Application

#### Option 1: Using Flask Server (Recommended)
```bash
python server.py
```
The Flask server will start on `http://localhost:5000`

#### Option 2: Using Simple HTTP Server
```bash
python host.py
```
The HTTP server will start on `http://localhost:8000`

#### Option 3: Using Legacy Excel Server
```bash
python save_to_excel.py
```
This starts the legacy server on `http://localhost:5000`

### 4. Access the Application
Open your web browser and navigate to:
- Flask Server: `http://localhost:5000`
- HTTP Server: `http://localhost:8000/index.html`

## 📖 Usage Guide

### For Auction Organizers

1. **Start the Server**: Run one of the server options mentioned above
2. **Navigate to Events**: Use the main page to select auction categories
3. **Manage Players**: Add player information, photos, and starting bids
4. **Conduct Auctions**: Use the interactive interface for real-time bidding
5. **Track Results**: All data is automatically saved to Excel files

### For Bidders/Teams

1. **View Available Players**: Browse through player photos and information
2. **Place Bids**: Use the bidding interface to place competitive bids
3. **Track Status**: Monitor bid status and team assignments
4. **View Results**: Check final auction results and team rosters

## 📊 Data Management

### Excel File Structure
Each auction category generates its own Excel file with the following columns:
- Player Name
- Position
- Status
- Event
- Bid Amount
- Team Name
- Photo Associated
- Sold To Group
- Timestamp

### Generated Files
The system automatically creates Excel files for each event:
- `classical_dance_results.xlsx`
- `classical_singing_results.xlsx`
- `folk_singing_results.xlsx`
- `western_singing_results.xlsx`
- `lazy_dance_results.xlsx`
- `retro_kannada_results.xlsx`
- `auction2_results.xlsx`
- `western_dance_results.xlsx`

## 🎨 Customization

### Adding New Auction Categories
1. Create a new HTML file for the auction interface
2. Add the category to the `EXCEL_FILES` dictionary in `server.py`
3. Update navigation links in `index.html`
4. Add corresponding images and logos

### Styling Customization
- Modify `styles.css` for visual changes
- Update Bootstrap classes for layout adjustments
- Customize gradient animations in the main HTML files

## 🔒 Security Considerations

- The application is designed for local network use
- CORS is enabled for development purposes
- Input validation is implemented on the backend
- Consider implementing authentication for production use

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Kill process using the port
   netstat -ano | findstr :5000
   taskkill /PID <PID> /F
   ```

2. **Missing Dependencies**
   ```bash
   pip install -r requirements.txt
   # or install individually
   pip install flask flask-cors pandas openpyxl
   ```

3. **Excel File Permission Errors**
   - Ensure Excel files are not open in other applications
   - Check file permissions in the project directory

4. **Image Loading Issues**
   - Verify image file paths are correct
   - Check file extensions match the HTML references

## 📝 API Endpoints

### POST `/save-player-status`
Saves player auction data to Excel files.

**Request Body:**
```json
{
    "playerName": "Player Name",
    "position": "Position",
    "status": "Available/Sold",
    "event": "Event Category",
    "bidAmount": "Amount",
    "teamName": "Team Name",
    "photoAssociated": "Image Path"
}
```

**Response:**
```json
{
    "success": true,
    "message": "Successfully saved to filename.xlsx",
    "data": {...}
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Support

For support and questions:
- Check the troubleshooting section above
- Review the code comments for implementation details
- Create an issue in the project repository

---

**Note**: This project is designed for educational and event management purposes. Ensure compliance with local regulations when using for actual auctions or financial transactions.
