from flask import Flask, request, jsonify
import requests
from ics import Calendar
from datetime import datetime

app = Flask(__name__)

# Map departments to their ICS URLs
DEPARTMENT_URLS = {
    "software engineering": "https://www3.primuss.de/stpl/index.php?FH=fhh&Language=de&mode=ical&Session=5a76cd513e52a4d20b724290d10d2eb2&User=tsudakaran&sem=8&type=4",
    "operational excellence": "https://www3.primuss.de/stpl/index.php?FH=fhh&Language=de&mode=ical&Session=5a76cd513e52a4d20b724290d10d2eb2&User=tsudakaran&sem=8&type=1&typeid=5",
    "artificial intelligence": "https://www3.primuss.de/stpl/index.php?FH=fhh&Language=de&mode=ical&Session=5a76cd513e52a4d20b724290d10d2eb2&User=tsudakaran&sem=8&type=1&typeid=251"
}

DEFAULT_ICAL_URL = "https://www3.primuss.de/stpl/index.php?FH=fhh&Language=de&mode=ical&Session=5a76cd513e52a4d20b724290d10d2eb2&User=tsudakaran&sem=8&type=4"

@app.route('/timetable', methods=['GET'])
def get_timetable():
    date_str = request.args.get('date', '')
    department = request.args.get('department', '').lower()
    time_filter = request.args.get('time', '')

    # Resolve URL
    url = DEPARTMENT_URLS.get(department, DEFAULT_ICAL_URL)

    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else datetime.today().date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    try:
        response = requests.get(url)
        response.raise_for_status()
        calendar = Calendar(response.text)
    except Exception as e:
        return jsonify({"error": f"Unable to fetch timetable: {str(e)}"}), 500

    timetable = []
    for event in calendar.events:
        if event.begin.date() == target_date:
            if time_filter:
                event_time = event.begin.to('local').format('HH:mm')
                if not event_time.startswith(time_filter[:2]):
                    continue
            timetable.append({
                "title": event.name,
                "start": event.begin.to('local').format('HH:mm'),
                "end": event.end.to('local').format('HH:mm'),
                "location": event.location or "N/A",
                "description": event.description or ""
            })

    if not timetable:
        return jsonify({"message": f"No classes found for {department or 'default'} on {target_date}."})

    return jsonify({
        "department": department or "Default",
        "date": target_date.isoformat(),
        "entries": timetable
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
