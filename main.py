from bakery import assert_equal
from drafter import *
from dataclasses import dataclass, field
from drafter.llm import *
from meta import *

# Configure website
set_website_title("TaskAI - Smart Study Scheduler")
set_website_style("none")  # Use custom styling
set_site_information(
    "TaskAI Study Scheduler",
    """
    An AI-powered study scheduler that helps students manage their coursework 
    and extracurricular activities efficiently.
    """,
    [],
    [],
    [],
)
set_gemini_server("https://draftergeminiproxy.avneet-sehgal72.workers.dev/")

# Modern Custom CSS Styling - Dark/Orange Theme (Claude-inspired)
add_website_css("""
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
        background: #0d0d0d;
        background-image: 
            radial-gradient(ellipse at 20% 20%, rgba(255, 138, 0, 0.15) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 80%, rgba(255, 179, 71, 0.1) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 50%, rgba(255, 100, 0, 0.05) 0%, transparent 70%);
        min-height: 100vh;
        padding: 20px;
        color: #e5e5e5;
        line-height: 1.6;
    }
    
    /* Main container */
    .container {
        max-width: 900px;
        margin: 0 auto;
        background: linear-gradient(145deg, #1a1a1a 0%, #141414 100%);
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 0 0 40px rgba(255, 138, 0, 0.1);
        padding: 40px;
        animation: fadeIn 0.5s ease-in;
        border: 1px solid rgba(255, 138, 0, 0.2);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Headers */
    h1 {
        font-size: 2.5em;
        font-weight: 700;
        margin-bottom: 10px;
        text-align: center;
        background: linear-gradient(135deg, #ff8a00 0%, #ffb347 50%, #ff6b00 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 30px rgba(255, 138, 0, 0.3);
    }
    
    h2 {
        color: #ff8a00;
        font-size: 1.8em;
        font-weight: 600;
        margin: 25px 0 15px 0;
        padding-bottom: 10px;
        border-bottom: 2px solid rgba(255, 138, 0, 0.3);
    }
    
    h3 {
        color: #ffb347;
        font-size: 1.3em;
        font-weight: 600;
        margin: 20px 0 10px 0;
    }
    
    /* Buttons */
    button, .button {
        background: linear-gradient(135deg, #ff8a00 0%, #ff6b00 100%);
        color: #0d0d0d;
        border: none;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 5px;
        box-shadow: 0 4px 15px rgba(255, 138, 0, 0.3), 0 0 20px rgba(255, 138, 0, 0.1);
        font-family: 'Space Grotesk', sans-serif;
    }
    
    button:hover, .button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(255, 138, 0, 0.5), 0 0 30px rgba(255, 138, 0, 0.2);
        background: linear-gradient(135deg, #ffb347 0%, #ff8a00 100%);
    }
    
    button:active {
        transform: translateY(0);
    }
    
    /* Input fields */
    input[type="text"], input[type="file"], textarea, select {
        width: 100%;
        padding: 12px 15px;
        margin: 8px 0;
        border: 2px solid #333;
        border-radius: 10px;
        font-size: 16px;
        font-family: 'Space Grotesk', sans-serif;
        transition: all 0.3s ease;
        background: #1a1a1a;
        color: #e5e5e5;
    }
    
    input[type="text"]:focus, textarea:focus, select:focus {
        outline: none;
        border-color: #ff8a00;
        background: #222;
        box-shadow: 0 0 0 3px rgba(255, 138, 0, 0.15), 0 0 20px rgba(255, 138, 0, 0.1);
    }
    
    select {
        cursor: pointer;
        appearance: none;
        background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23ff8a00' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
        background-repeat: no-repeat;
        background-position: right 10px center;
        background-size: 20px;
        padding-right: 40px;
    }
    
    select option {
        background: #1a1a1a;
        color: #e5e5e5;
    }
    
    /* Lists */
    ul, ol {
        margin: 15px 0;
        padding-left: 25px;
    }
    
    li {
        margin: 10px 0;
        padding: 12px;
        background: #1f1f1f;
        border-radius: 8px;
        border-left: 4px solid #ff8a00;
        transition: all 0.2s ease;
        color: #e5e5e5;
    }
    
    li:hover {
        background: #2a2a2a;
        transform: translateX(5px);
        border-left-color: #ffb347;
    }
    
    /* Cards */
    .card {
        background: #1f1f1f;
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
        border: 1px solid #333;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        border-color: #ff8a00;
        box-shadow: 0 4px 20px rgba(255, 138, 0, 0.15);
    }
    
    /* Horizontal rules */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #ff8a00, transparent);
        margin: 30px 0;
    }
    
    /* Pre-formatted text (for schedule display) */
    pre {
        background: #1a1a1a;
        padding: 20px;
        border-radius: 12px;
        border-left: 4px solid #ff8a00;
        overflow-x: auto;
        font-family: 'SF Mono', 'Fira Code', monospace;
        font-size: 14px;
        line-height: 1.6;
        white-space: pre-wrap;
        word-wrap: break-word;
        color: #e5e5e5;
    }
    
    /* Bold and italic text */
    strong, b {
        color: #ffb347;
        font-weight: 600;
    }
    
    em, i {
        color: #999;
        font-style: italic;
    }
    
    /* Links */
    a {
        color: #ff8a00;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    
    a:hover {
        color: #ffb347;
        text-decoration: underline;
        text-shadow: 0 0 10px rgba(255, 138, 0, 0.3);
    }
    
    /* Step indicator */
    .step-indicator {
        background: linear-gradient(135deg, #ff8a00 0%, #ff6b00 100%);
        color: #0d0d0d;
        padding: 8px 20px;
        border-radius: 20px;
        display: inline-block;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 20px;
        box-shadow: 0 0 20px rgba(255, 138, 0, 0.2);
    }
    
    /* Info box */
    .info-box {
        background: rgba(255, 138, 0, 0.1);
        padding: 15px 20px;
        border-radius: 10px;
        border-left: 4px solid #ff8a00;
        margin: 15px 0;
        color: #e5e5e5;
    }
    
    /* Success message */
    .success {
        background: rgba(40, 167, 69, 0.15);
        color: #5cb85c;
        padding: 15px 20px;
        border-radius: 10px;
        border-left: 4px solid #28a745;
        margin: 15px 0;
    }
    
    /* Emoji enhancement */
    .emoji {
        font-size: 1.5em;
        margin: 0 5px;
    }
    
    /* Spacing utilities */
    .spacing {
        margin: 20px 0;
    }
    
    /* Center alignment */
    .center {
        text-align: center;
    }
    
    /* Button group */
    .button-group {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin: 20px 0;
        justify-content: center;
    }
    
    /* Responsive design */
    /* Day tile selector */
    .day-tile {
        display: inline-block;
        padding: 12px 18px;
        background: #1a1a1a;
        border: 2px solid #333;
        border-radius: 8px;
        font-weight: 600;
        color: #999;
        transition: all 0.2s ease;
        min-width: 50px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        cursor: pointer;
    }
    
    .day-tile:hover {
        border-color: #ff8a00;
        background: #222;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(255,138,0,0.2);
        color: #ffb347;
    }
    
    .day-tile.selected {
        background: linear-gradient(135deg, #ff8a00 0%, #ff6b00 100%) !important;
        border-color: #ff8a00;
        color: #0d0d0d;
        box-shadow: 0 4px 20px rgba(255,138,0,0.4);
    }
    
    /* Checkboxes */
    input[type="checkbox"] {
        width: 20px;
        height: 20px;
        accent-color: #ff8a00;
        cursor: pointer;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1a1a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #ff8a00;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #ffb347;
    }
    
    /* Paragraph text */
    p {
        color: #c5c5c5;
    }

    @media (max-width: 768px) {
        .container {
            padding: 20px;
        }
        
        h1 {
            font-size: 2em;
        }
        
        h2 {
            font-size: 1.5em;
        }
        
        button {
            width: 100%;
            margin: 5px 0;
        }
    }
""")

# Data structures
@dataclass
class Course:
    name: str
    credits: int
    days: str  # e.g., "MWF" or "TTh"
    time: str  # e.g., "9:00 AM - 10:15 AM"

@dataclass 
class ClubActivity:
    name: str
    day: str
    time: str

@dataclass
class StudyEvent:
    """Represents a study session event for the calendar"""
    title: str
    start_datetime: str  # ISO format: "2025-12-09T19:00:00"
    end_datetime: str    # ISO format: "2025-12-09T21:00:00"
    course_code: str
    description: str

@dataclass
class State:
    major: str = ""
    courses: list[Course] = field(default_factory=list)
    clubs: list[ClubActivity] = field(default_factory=list)
    semester_start: str = "2025-12-09"  # Default to next week
    semester_end: str = "2026-05-15"     # Default to end of spring semester
    study_events: list[StudyEvent] = field(default_factory=list)
    tips: str = ""
    current_step: str = "welcome"  # welcome, major, semester_dates, courses, clubs, generate
    # Temporary fields for manual entry persistence
    temp_course_name: str = ""
    temp_credits: str = "3"
    temp_time: str = ""
    temp_days: dict = field(default_factory=lambda: {
        "day_monday": "",
        "day_tuesday": "",
        "day_wednesday": "",
        "day_thursday": "",
        "day_friday": "",
        "day_saturday": "",
        "day_sunday": ""
    })
    
# Helper function to parse CSV
def parse_course_csv(csv_content: str) -> tuple[list[Course], list[str]]:
    """Parse CSV content and return list of courses and errors.
    Supports two formats:
    1. Simple format: Course Name, Credits, Days, Time
    2. WebReg/Calendar format: Subject, Start Date, Start Time, End Date, End Time, All Day Event, Location
    """
    from datetime import datetime
    
    courses = []
    errors = []
    lines = csv_content.strip().split('\n')
    
    if not lines:
        return courses, ["Empty CSV file"]
    
    # Detect format based on header
    header = lines[0].lower()
    
    # Check if it's WebReg/Calendar format
    if 'start date' in header or 'start time' in header or 'end time' in header:
        # WebReg/Calendar format: Subject, Start Date, Start Time, End Date, End Time, All Day Event, Location
        # We need to group events by course name and determine the days/times
        
        course_data = {}  # {course_name: {'dates': [...], 'start_time': str, 'end_time': str}}
        
        for idx, line in enumerate(lines[1:], start=2):  # Skip header
            if not line.strip():
                continue
                
            parts = [p.strip() for p in line.split(',')]
            if len(parts) < 5:
                errors.append(f"Row {idx}: Not enough columns for calendar format.")
                continue
            
            course_name = parts[0]
            start_date_str = parts[1]  # MM/DD/YYYY
            start_time_str = parts[2]  # HH:MM AM/PM
            end_date_str = parts[3]    # MM/DD/YYYY
            end_time_str = parts[4]    # HH:MM AM/PM
            
            if not course_name or not start_date_str or not start_time_str:
                errors.append(f"Row {idx}: Missing required fields.")
                continue
            
            # Parse the date to get day of week
            try:
                event_date = datetime.strptime(start_date_str, '%m/%d/%Y')
                day_of_week = event_date.weekday()  # 0=Monday, 6=Sunday
                
                # Map day number to abbreviation
                day_abbrevs = {0: 'M', 1: 'Tu', 2: 'W', 3: 'Th', 4: 'F', 5: 'Sa', 6: 'Su'}
                day_abbrev = day_abbrevs[day_of_week]
                
            except ValueError as e:
                errors.append(f"Row {idx}: Invalid date format '{start_date_str}'.")
                continue
            
            # Store course data
            if course_name not in course_data:
                course_data[course_name] = {
                    'days': set(),
                    'start_time': start_time_str,
                    'end_time': end_time_str,
                    'first_date': event_date,
                    'last_date': event_date
                }
            
            course_data[course_name]['days'].add(day_abbrev)
            if event_date < course_data[course_name]['first_date']:
                course_data[course_name]['first_date'] = event_date
            if event_date > course_data[course_name]['last_date']:
                course_data[course_name]['last_date'] = event_date
        
        # Convert course_data to Course objects
        for course_name, data in course_data.items():
            # Sort days in proper order
            day_order = {'M': 0, 'Tu': 1, 'W': 2, 'Th': 3, 'F': 4, 'Sa': 5, 'Su': 6}
            sorted_days = sorted(data['days'], key=lambda d: day_order.get(d, 7))
            days_str = ''.join(sorted_days)
            
            # Create time range string
            time_str = f"{data['start_time']} - {data['end_time']}"
            
            # Estimate credits based on meeting frequency (rough estimate)
            credits = 3  # Default
            if len(data['days']) >= 3:
                credits = 3
            elif len(data['days']) == 2:
                credits = 3
            elif len(data['days']) == 1:
                credits = 1
            
            courses.append(Course(
                name=course_name,
                credits=credits,
                days=days_str,
                time=time_str
            ))
        
        # Return the first and last dates for semester bounds
        if course_data:
            all_first = min(d['first_date'] for d in course_data.values())
            all_last = max(d['last_date'] for d in course_data.values())
            # Store in a special way - we'll handle this in the route
            
    else:
        # Simple format: Course Name, Credits, Days, Time
        start_idx = 1 if lines and ('course' in header or 'name' in header) else 0
        
        for idx, line in enumerate(lines[start_idx:], start=start_idx+1):
            if line.strip():
                parts = [p.strip() for p in line.split(',')]
                if len(parts) >= 4:
                    name, credits, days, time = parts[0], parts[1], parts[2], parts[3]
                    valid = True
                    
                    # Validate required fields
                    if not name or not days or not time:
                        errors.append(f"Row {idx}: Missing required fields (name, days, or time).")
                        valid = False
                    
                    # Validate credits
                    try:
                        int_credits = int(credits) if credits.isdigit() else 3
                    except:
                        errors.append(f"Row {idx}: Invalid credits value '{credits}' (must be a number).")
                        valid = False
                    
                    # Validate time format
                    if valid and '-' not in time:
                        errors.append(f"Row {idx}: Invalid time format '{time}' (expected format: 'HH:MM AM/PM - HH:MM AM/PM').")
                        valid = False
                    
                    if valid:
                        courses.append(Course(
                            name=name,
                            credits=int_credits,
                            days=days,
                            time=time
                        ))
                else:
                    errors.append(f"Row {idx}: Not enough columns (expected at least 4: Name, Credits, Days, Time).")
    
    return courses, errors


def get_semester_dates_from_csv(csv_content: str) -> tuple[str, str]:
    """Extract semester start and end dates from WebReg CSV format."""
    from datetime import datetime
    
    lines = csv_content.strip().split('\n')
    if not lines:
        return "", ""
    
    header = lines[0].lower()
    if 'start date' not in header:
        return "", ""
    
    dates = []
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = [p.strip() for p in line.split(',')]
        if len(parts) >= 2:
            try:
                event_date = datetime.strptime(parts[1], '%m/%d/%Y')
                dates.append(event_date)
            except:
                continue
    
    if dates:
        start_date = min(dates).strftime('%Y-%m-%d')
        end_date = max(dates).strftime('%Y-%m-%d')
        return start_date, end_date
    
    return "", ""

# Routes
@route
def index(state: State) -> Page:
    """Welcome page"""
    return Page(state, [
        Div(
            Header("Welcome to TaskAI! 🎓", 1),
            LineBreak(),
            change_text_align(
                change_text_size("Your AI-powered study scheduler that helps you balance coursework and activities.", "1.1em"),
                "center"
            ),
            LineBreak(),
            LineBreak(),
            bold("TaskAI will help you:"),
            BulletedList([
                "📚 Organize your class schedule",
                "🎯 Track your extracurricular activities",
                "📅 Generate personalized study sessions for 2 weeks",
                "💡 Get AI-powered study tips for each subject"
            ]),
            LineBreak(),
            change_margin(
                change_text_align(Button("Get Started 🚀", set_major), "center"),
                "20px 0"
            ),
            classes="container"
        )
    ])

@route
def set_major(state: State) -> Page:
    """Step 1: Ask for major"""
    state.current_step = "major"
    return Page(state, [
        Div(
            Div("Step 1 of 4", classes="step-indicator"),
            Header("Tell us your major 🎓", 2),
            LineBreak(),
            "Your major helps us prioritize which classes need more study time:",
            LineBreak(),
            LineBreak(),
            change_padding(TextBox("major_input", state.major), "15px"),
            LineBreak(),
            Button("Next: Add Courses →", save_major, [Argument("major", state.major)]),
            classes="container"
        )
    ])

@route
def save_major(state: State, major: str, major_input: str) -> Page:
    """Save major and proceed to course entry"""
    state.major = major_input if major_input else major
    state.current_step = "courses"
    return choose_course_input(state)

@route
def choose_course_input(state: State) -> Page:
    """Step 2: Choose how to input courses"""
    return Page(state, [
        Header("Step 2: Add Your Courses", 2),
        LineBreak(),
        f"Major: {bold(state.major)}",
        LineBreak(),
        LineBreak(),
        "Choose how you'd like to add your courses:",
        LineBreak(),
        LineBreak(),
        Button("Upload CSV from WebReg", upload_csv_page),
        " or ",
        Button("Enter Courses Manually", manual_course_entry),
        LineBreak(),
        LineBreak(),
        italic("CSV format: Course Name, Credits, Days, Time"),
        LineBreak(),
        italic("Example: CISC181,3,MWF,9:00 AM - 9:50 AM")
    ])

@route
def upload_csv_page(state: State) -> Page:
    """Page for uploading CSV"""
    return Page(state, [
        Header("Upload Course Schedule CSV", 2),
        LineBreak(),
        "Upload your course schedule from WebReg:",
        LineBreak(),
        LineBreak(),
        FileUpload("csv_file"),
        LineBreak(),
        Button("Upload and Parse", parse_csv),
        LineBreak(),
        LineBreak(),
        Button("← Back", choose_course_input)
    ])

@route
def parse_csv(state: State, csv_file: str) -> Page:
    """Parse uploaded CSV and display courses"""
    try:
        state.courses, errors = parse_course_csv(csv_file)
        
        # Try to extract semester dates from WebReg format
        start_date, end_date = get_semester_dates_from_csv(csv_file)
        if start_date and end_date:
            state.semester_start = start_date
            state.semester_end = end_date
            print(f"✅ Detected semester dates: {start_date} to {end_date}")
        
        print(f"✅ Parsed {len(state.courses)} courses from CSV")
        for course in state.courses[:5]:  # Print first 5
            print(f"  - {course.name}: {course.days} at {course.time}")
        if len(state.courses) > 5:
            print(f"  ... and {len(state.courses) - 5} more")
        
        # If there were errors, show them
        if errors:
            error_list = BulletedList(errors)
            return Page(state, [
                Header("Some rows were skipped due to errors", 2),
                LineBreak(),
                f"Successfully parsed {len(state.courses)} courses, but encountered {len(errors)} error(s):",
                LineBreak(),
                error_list,
                LineBreak(),
                Button("Continue with parsed courses", show_courses),
                LineBreak(),
                Button("← Try uploading again", upload_csv_page)
            ])
        
        return show_courses(state)
    except Exception as e:
        print(f"❌ Error parsing CSV: {e}")
        import traceback
        traceback.print_exc()
        return Page(state, [
            Header("Error Parsing CSV", 2),
            LineBreak(),
            f"There was an error parsing your CSV: {str(e)}",
            LineBreak(),
            LineBreak(),
            "Please make sure your CSV follows one of these formats:",
            LineBreak(),
            "1. Simple format: Course Name, Credits, Days, Time",
            LineBreak(),
            "2. WebReg format: Subject, Start Date, Start Time, End Date, End Time, All Day Event, Location",
            LineBreak(),
            LineBreak(),
            Button("← Try Again", upload_csv_page)
        ])

@route
def manual_course_entry(state: State) -> Page:
    """Page for manually entering courses"""
    return Page(state, [
        Div(
            Header("Add Course Manually", 2),
            LineBreak(),
            
            # Semester Dates Section
            Div(
                Header("📅 Semester Dates", 3),
                "When does your semester start?",
                LineBreak(),
                TextBox("semester_start", state.semester_start, placeholder="YYYY-MM-DD (e.g., 2025-12-09)"),
                LineBreak(),
                LineBreak(),
                "When does your semester end?",
                LineBreak(),
                TextBox("semester_end", state.semester_end, placeholder="YYYY-MM-DD (e.g., 2026-05-15)"),
                classes="info-box"
            ),
            LineBreak(),
            LineBreak(),
            HorizontalRule(),
            LineBreak(),
            
            # Course Entry Section
            Header("➕ Add a Course", 3),
            LineBreak(),
            "Course Name:",
            LineBreak(),
            TextBox("course_name", state.temp_course_name),
            LineBreak(),
            LineBreak(),
            "Credits:",
            LineBreak(),
            SelectBox("credits", ["1", "2", "3", "4", "5"], state.temp_credits),
            LineBreak(),
            LineBreak(),
            "Days of the Week:",
            LineBreak(),
            # Build day selector with proper checkbox handling and visual feedback
            """<div style='display: flex; flex-wrap: wrap; gap: 10px; margin: 10px 0;'>
                <label style='cursor: pointer;' onclick="toggleDay(this);">
                    <input type='checkbox' name='day_monday' value='M' style='display: none;'>
                    <span class='day-tile' style='display: inline-block; padding: 12px 18px; background: #1a1a1a; border: 2px solid #333; border-radius: 8px; font-weight: 600; color: #999; transition: all 0.2s ease; min-width: 50px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.3); cursor: pointer;'>M</span>
                </label>
                <label style='cursor: pointer;' onclick="toggleDay(this);">
                    <input type='checkbox' name='day_tuesday' value='Tu' style='display: none;'>
                    <span class='day-tile' style='display: inline-block; padding: 12px 18px; background: #1a1a1a; border: 2px solid #333; border-radius: 8px; font-weight: 600; color: #999; transition: all 0.2s ease; min-width: 50px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.3); cursor: pointer;'>Tu</span>
                </label>
                <label style='cursor: pointer;' onclick="toggleDay(this);">
                    <input type='checkbox' name='day_wednesday' value='W' style='display: none;'>
                    <span class='day-tile' style='display: inline-block; padding: 12px 18px; background: #1a1a1a; border: 2px solid #333; border-radius: 8px; font-weight: 600; color: #999; transition: all 0.2s ease; min-width: 50px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.3); cursor: pointer;'>W</span>
                </label>
                <label style='cursor: pointer;' onclick="toggleDay(this);">
                    <input type='checkbox' name='day_thursday' value='Th' style='display: none;'>
                    <span class='day-tile' style='display: inline-block; padding: 12px 18px; background: #1a1a1a; border: 2px solid #333; border-radius: 8px; font-weight: 600; color: #999; transition: all 0.2s ease; min-width: 50px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.3); cursor: pointer;'>Th</span>
                </label>
                <label style='cursor: pointer;' onclick="toggleDay(this);">
                    <input type='checkbox' name='day_friday' value='F' style='display: none;'>
                    <span class='day-tile' style='display: inline-block; padding: 12px 18px; background: #1a1a1a; border: 2px solid #333; border-radius: 8px; font-weight: 600; color: #999; transition: all 0.2s ease; min-width: 50px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.3); cursor: pointer;'>F</span>
                </label>
                <label style='cursor: pointer;' onclick="toggleDay(this);">
                    <input type='checkbox' name='day_saturday' value='Sa' style='display: none;'>
                    <span class='day-tile' style='display: inline-block; padding: 12px 18px; background: #1a1a1a; border: 2px solid #333; border-radius: 8px; font-weight: 600; color: #999; transition: all 0.2s ease; min-width: 50px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.3); cursor: pointer;'>Sa</span>
                </label>
                <label style='cursor: pointer;' onclick="toggleDay(this);">
                    <input type='checkbox' name='day_sunday' value='Su' style='display: none;'>
                    <span class='day-tile' style='display: inline-block; padding: 12px 18px; background: #1a1a1a; border: 2px solid #333; border-radius: 8px; font-weight: 600; color: #999; transition: all 0.2s ease; min-width: 50px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.3); cursor: pointer;'>Su</span>
                </label>
            </div>
            <script>
                function toggleDay(labelElement) {
                    const checkbox = labelElement.querySelector('input[type="checkbox"]');
                    const tile = labelElement.querySelector('.day-tile');
                    checkbox.checked = !checkbox.checked;
                    
                    if (checkbox.checked) {
                        tile.style.background = 'linear-gradient(135deg, #ff8a00 0%, #ff6b00 100%)';
                        tile.style.borderColor = '#ff8a00';
                        tile.style.color = '#0d0d0d';
                        tile.style.boxShadow = '0 4px 20px rgba(255,138,0,0.4)';
                    } else {
                        tile.style.background = '#1a1a1a';
                        tile.style.borderColor = '#333';
                        tile.style.color = '#999';
                        tile.style.boxShadow = '0 2px 4px rgba(0,0,0,0.3)';
                    }
                }
                
                // Initialize tiles based on checkbox state when page loads
                document.addEventListener('DOMContentLoaded', function() {
                    document.querySelectorAll('input[type="checkbox"][name^="day_"]').forEach(checkbox => {
                        const tile = checkbox.parentElement.querySelector('.day-tile');
                        if (checkbox.checked && tile) {
                            tile.style.background = 'linear-gradient(135deg, #ff8a00 0%, #ff6b00 100%)';
                            tile.style.borderColor = '#ff8a00';
                            tile.style.color = '#0d0d0d';
                            tile.style.boxShadow = '0 4px 20px rgba(255,138,0,0.4)';
                        }
                    });
                });
            </script>""",
            LineBreak(),
            LineBreak(),
            "Time (e.g., 9:00 AM - 9:50 AM):",
            LineBreak(),
            TextBox("time", state.temp_time),
            LineBreak(),
            LineBreak(),
            Button("Add Course", add_course),
            LineBreak(),
            LineBreak(),
            Button("← Back", choose_course_input),
            classes="container"
        )
    ])

@route
def add_course(state: State, course_name: str, credits: str, time: str, 
               semester_start: str, semester_end: str,
               day_monday: str = "", day_tuesday: str = "", day_wednesday: str = "",
               day_thursday: str = "", day_friday: str = "", day_saturday: str = "", 
               day_sunday: str = "") -> Page:
    """Add a course to the list and update semester dates"""
    # Update semester dates if provided
    if semester_start:
        state.semester_start = semester_start
    if semester_end:
        state.semester_end = semester_end
    
    # Save temp fields for persistence
    state.temp_course_name = course_name
    state.temp_credits = credits
    state.temp_time = time
    state.temp_days = {
        "day_monday": day_monday,
        "day_tuesday": day_tuesday,
        "day_wednesday": day_wednesday,
        "day_thursday": day_thursday,
        "day_friday": day_friday,
        "day_saturday": day_saturday,
        "day_sunday": day_sunday
    }
    
    # Combine selected days into a string
    days_list = []
    if day_monday: days_list.append("M")
    if day_tuesday: days_list.append("Tu")
    if day_wednesday: days_list.append("W")
    if day_thursday: days_list.append("Th")
    if day_friday: days_list.append("F")
    if day_saturday: days_list.append("Sa")
    if day_sunday: days_list.append("Su")
    days = "".join(days_list)
    
    # Add course if all fields are filled
    if course_name and days and time:
        state.courses.append(Course(
            name=course_name,
            credits=int(credits),
            days=days,
            time=time
        ))
        # Clear temp fields after successful add
        state.temp_course_name = ""
        state.temp_credits = "3"
        state.temp_time = ""
        state.temp_days = {
            "day_monday": "",
            "day_tuesday": "",
            "day_wednesday": "",
            "day_thursday": "",
            "day_friday": "",
            "day_saturday": "",
            "day_sunday": ""
        }
    return show_courses(state)

@route
@route
def show_courses(state: State) -> Page:
    """Display all courses and option to continue"""
    from datetime import datetime, timedelta
    import json
    
    course_list = [f"{c.name} ({c.credits} credits) - {c.days} at {c.time}" for c in state.courses]
    
    # Helper functions for calendar preview
    def parse_days(days_str):
        day_map = {'M': 0, 'Tu': 1, 'W': 2, 'Th': 3, 'F': 4, 'Sa': 5, 'Su': 6}
        days = []
        i = 0
        while i < len(days_str):
            if i + 1 < len(days_str) and days_str[i:i+2] in day_map:
                days.append(day_map[days_str[i:i+2]])
                i += 2
            elif days_str[i] in day_map:
                days.append(day_map[days_str[i]])
                i += 1
            else:
                i += 1
        return days
    
    def parse_time_range(time_str):
        try:
            # Split by ' - ' first (with spaces), then try just '-'
            if ' - ' in time_str:
                parts = time_str.split(' - ')
            elif '-' in time_str:
                parts = time_str.split('-')
            else:
                return None
            
            if len(parts) != 2:
                return None
            
            start_str = parts[0].strip()
            end_str = parts[1].strip()
            
            # Parse start time - try multiple formats
            start_time = None
            for fmt in ['%I:%M %p', '%I:%M%p', '%H:%M', '%I:%M']:
                try:
                    start_time = datetime.strptime(start_str, fmt)
                    break
                except ValueError:
                    continue
            
            if start_time is None:
                return None
            
            # Parse end time - try multiple formats
            end_time = None
            for fmt in ['%I:%M %p', '%I:%M%p', '%H:%M', '%I:%M']:
                try:
                    end_time = datetime.strptime(end_str, fmt)
                    break
                except ValueError:
                    continue
            
            if end_time is None:
                return None
            
            return (start_time.hour, start_time.minute, end_time.hour, end_time.minute)
        except:
            return None
    
    # Generate class events for calendar preview (full semester)
    preview_events = []
    if state.courses and state.semester_start:
        try:
            semester_start = datetime.strptime(state.semester_start, '%Y-%m-%d')
            # Use semester_end if available, otherwise show 4 weeks
            if state.semester_end:
                preview_end = datetime.strptime(state.semester_end, '%Y-%m-%d')
            else:
                preview_end = semester_start + timedelta(days=28)
            
            for course in state.courses:
                weekdays = parse_days(course.days)
                time_parts = parse_time_range(course.time)
                
                if not weekdays or not time_parts:
                    continue
                
                start_hour, start_min, end_hour, end_min = time_parts
                
                current_date = semester_start
                while current_date <= preview_end:
                    if current_date.weekday() in weekdays:
                        class_start = current_date.replace(hour=start_hour, minute=start_min, second=0)
                        class_end = current_date.replace(hour=end_hour, minute=end_min, second=0)
                        
                        preview_events.append({
                            "title": course.name,
                            "start": class_start.strftime('%Y-%m-%dT%H:%M:%S'),
                            "end": class_end.strftime('%Y-%m-%dT%H:%M:%S'),
                            "backgroundColor": "#e74c3c",
                            "borderColor": "#c0392b"
                        })
                    current_date += timedelta(days=1)
        except Exception as e:
            print(f"Error generating preview: {e}")
    
    events_json = json.dumps(preview_events)
    
    calendar_preview = f"""
    <link href='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.10/index.global.min.css' rel='stylesheet' />
    <script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.10/index.global.min.js'></script>
    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        console.log('Initializing course preview calendar...');
        var calendarEl = document.getElementById('preview-calendar');
        if (!calendarEl) {{
            console.error('Calendar element #preview-calendar not found!');
            return;
        }}
        
        var events = {events_json};
        console.log('Loaded ' + events.length + ' course events for preview');
        
        try {{
            var calendar = new FullCalendar.Calendar(calendarEl, {{
                initialView: 'timeGridWeek',
                initialDate: '{state.semester_start}',
                headerToolbar: {{
                    left: 'prev,next today',
                    center: 'title',
                    right: 'dayGridMonth,timeGridWeek,timeGridDay'
                }},
                slotMinTime: '06:00:00',
                slotMaxTime: '23:00:00',
                allDaySlot: false,
                height: 'auto',
                events: events,
                eventClick: function(info) {{
                    alert(info.event.title + '\\n' + 
                          info.event.start.toLocaleString());
                }}
            }});
            calendar.render();
            console.log('Course preview calendar rendered successfully!');
        }} catch(e) {{
            console.error('Error rendering calendar:', e);
        }}
    }});
    </script>
    """ if state.courses else ""
    
    return Page(state, [
        Div(
            calendar_preview,
            Header("Your Courses", 2),
            LineBreak(),
            f"Major: {state.major}",
            LineBreak(),
            f"Semester: {state.semester_start} to {state.semester_end}",
            LineBreak(),
            f"Total Courses: {len(state.courses)}",
            LineBreak(),
            LineBreak(),
            
            # Calendar Preview - Always show if courses exist
            ("<div style='background: #1a1a1a; padding: 20px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.4), 0 0 30px rgba(255,138,0,0.1); margin: 20px 0; border: 1px solid rgba(255,138,0,0.2);'>" +
             "<h3 style='color: #ff8a00; margin-top: 0;'>📅 Your Class Schedule</h3>" +
             "<p style='color: #999;'>Showing your classes for the entire semester</p>" +
             "<div id='preview-calendar' style='min-height: 500px;'></div>" +
             "</div>") if state.courses else "<p style='color: #999;'>No courses added yet.</p>",
            
            LineBreak(),
            Button("Add Another Course", "/manual_course_entry"),
            " ",
            Button("Next: Add Clubs/Activities", "/clubs_page") if state.courses else "",
            LineBreak(),
            LineBreak(),
            Button("← Back", "/choose_course_input"),
            classes="container"
        )
    ])

@route
def clubs_page(state: State) -> Page:
    """Step 3: Add club activities"""
    state.current_step = "clubs"
    
    club_list = [f"{c.name} - {c.day} at {c.time}" for c in state.clubs]
    
    return Page(state, [
        Header("Step 3: Add Clubs & Activities", 2),
        LineBreak(),
        "Add your extracurricular activities:",
        LineBreak(),
        LineBreak(),
        "Activity Name:",
        LineBreak(),
        TextBox("club_name"),
        LineBreak(),
        LineBreak(),
        "Days of the Week:",
        LineBreak(),
        """<div style='display: flex; flex-wrap: wrap; gap: 10px; margin: 10px 0;'>
            <label style='cursor: pointer;'>
                <input type='checkbox' name='club_day_monday' value='Monday' style='display: none;'>
                <span class='day-tile-club' onclick='this.parentElement.querySelector("input").checked = !this.parentElement.querySelector("input").checked; this.classList.toggle("selected");'>Mon</span>
            </label>
            <label style='cursor: pointer;'>
                <input type='checkbox' name='club_day_tuesday' value='Tuesday' style='display: none;'>
                <span class='day-tile-club' onclick='this.parentElement.querySelector("input").checked = !this.parentElement.querySelector("input").checked; this.classList.toggle("selected");'>Tue</span>
            </label>
            <label style='cursor: pointer;'>
                <input type='checkbox' name='club_day_wednesday' value='Wednesday' style='display: none;'>
                <span class='day-tile-club' onclick='this.parentElement.querySelector("input").checked = !this.parentElement.querySelector("input").checked; this.classList.toggle("selected");'>Wed</span>
            </label>
            <label style='cursor: pointer;'>
                <input type='checkbox' name='club_day_thursday' value='Thursday' style='display: none;'>
                <span class='day-tile-club' onclick='this.parentElement.querySelector("input").checked = !this.parentElement.querySelector("input").checked; this.classList.toggle("selected");'>Thu</span>
            </label>
            <label style='cursor: pointer;'>
                <input type='checkbox' name='club_day_friday' value='Friday' style='display: none;'>
                <span class='day-tile-club' onclick='this.parentElement.querySelector("input").checked = !this.parentElement.querySelector("input").checked; this.classList.toggle("selected");'>Fri</span>
            </label>
            <label style='cursor: pointer;'>
                <input type='checkbox' name='club_day_saturday' value='Saturday' style='display: none;'>
                <span class='day-tile-club' onclick='this.parentElement.querySelector("input").checked = !this.parentElement.querySelector("input").checked; this.classList.toggle("selected");'>Sat</span>
            </label>
            <label style='cursor: pointer;'>
                <input type='checkbox' name='club_day_sunday' value='Sunday' style='display: none;'>
                <span class='day-tile-club' onclick='this.parentElement.querySelector("input").checked = !this.parentElement.querySelector("input").checked; this.classList.toggle("selected");'>Sun</span>
            </label>
        </div>
        <style>
            .day-tile-club {
                display: inline-block;
                padding: 12px 18px;
                background: #1a1a1a;
                border: 2px solid #333;
                border-radius: 8px;
                font-weight: 600;
                color: #999;
                transition: all 0.2s ease;
                min-width: 50px;
                text-align: center;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
            }
            .day-tile-club:hover {
                border-color: #ff8a00;
                background: #222;
                transform: translateY(-2px);
                box-shadow: 0 4px 15px rgba(255,138,0,0.2);
            }
            .day-tile-club.selected {
                background: linear-gradient(135deg, #ff8a00 0%, #ff6b00 100%);
                border-color: #ff8a00;
                color: #0d0d0d;
                box-shadow: 0 4px 20px rgba(255,138,0,0.4);
            }
        </style>""",
        LineBreak(),
        LineBreak(),
        "Time:",
        LineBreak(),
        TextBox("club_time"),
        LineBreak(),
        LineBreak(),
        Button("Add Activity", "/add_club"),
        LineBreak(),
        LineBreak(),
        HorizontalRule(),
        LineBreak(),
        Header("Your Activities:", 3),
        BulletedList(club_list) if club_list else "No activities added yet.",
        LineBreak(),
        LineBreak(),
        Button("Generate Study Schedule", "/generate_schedule") if state.courses else "<em>Please add courses first</em>",
        LineBreak(),
        LineBreak(),
        Button("← Back to Courses", "/show_courses")
    ])

@route
def add_club(state: State, club_name: str, club_time: str,
             club_day_monday: str = "", club_day_tuesday: str = "", club_day_wednesday: str = "",
             club_day_thursday: str = "", club_day_friday: str = "", club_day_saturday: str = "", 
             club_day_sunday: str = "") -> Page:
    """Add a club activity"""
    # Combine selected days into a string
    days_list = []
    if club_day_monday: days_list.append("Monday")
    if club_day_tuesday: days_list.append("Tuesday")
    if club_day_wednesday: days_list.append("Wednesday")
    if club_day_thursday: days_list.append("Thursday")
    if club_day_friday: days_list.append("Friday")
    if club_day_saturday: days_list.append("Saturday")
    if club_day_sunday: days_list.append("Sunday")
    club_days = ", ".join(days_list) if days_list else "Monday"
    
    if club_name and club_time:
        state.clubs.append(ClubActivity(
            name=club_name,
            day=club_days,
            time=club_time
        ))
    return clubs_page(state)

@route
def loading_page(state: State) -> Page:
    """Display loading screen while generating schedule"""
    return Page(state, [
        """
        <div class="loading-overlay">
            <div class="loading-container">
                <div class="loading-icon">
                    <div class="calendar-animation">
                        <div class="calendar-page">
                            <div class="calendar-header"></div>
                            <div class="calendar-grid">
                                <div class="calendar-cell"></div>
                                <div class="calendar-cell"></div>
                                <div class="calendar-cell"></div>
                                <div class="calendar-cell"></div>
                                <div class="calendar-cell active"></div>
                                <div class="calendar-cell"></div>
                            </div>
                        </div>
                        <div class="sparkles">
                            <div class="sparkle"></div>
                            <div class="sparkle"></div>
                            <div class="sparkle"></div>
                        </div>
                    </div>
                </div>
                <h2 class="loading-title">Creating Your Perfect Study Schedule ✨</h2>
                <div class="loading-steps">
                    <div class="step step-1">
                        <div class="step-icon">📚</div>
                        <div class="step-text">Analyzing your courses</div>
                    </div>
                    <div class="step step-2">
                        <div class="step-icon">🎯</div>
                        <div class="step-text">Optimizing study times</div>
                    </div>
                    <div class="step step-3">
                        <div class="step-icon">💡</div>
                        <div class="step-text">Generating personalized tips</div>
                    </div>
                    <div class="step step-4">
                        <div class="step-icon">📅</div>
                        <div class="step-text">Building your calendar</div>
                    </div>
                </div>
                <div class="loading-bar-container">
                    <div class="loading-bar"></div>
                </div>
                <p class="loading-subtext">This may take a few moments...</p>
            </div>
        </div>
        
        <style>
            .loading-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: linear-gradient(135deg, #0d0d0d 0%, #1a1a1a 50%, #0d0d0d 100%);
                background-image: 
                    radial-gradient(ellipse at 30% 30%, rgba(255, 138, 0, 0.2) 0%, transparent 50%),
                    radial-gradient(ellipse at 70% 70%, rgba(255, 179, 71, 0.15) 0%, transparent 50%);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 9999;
                animation: fadeIn 0.5s ease;
            }
            
            .loading-container {
                text-align: center;
                padding: 40px;
                max-width: 600px;
            }
            
            .calendar-animation {
                position: relative;
                width: 120px;
                height: 120px;
                margin: 0 auto 30px;
                animation: float 3s ease-in-out infinite;
            }
            
            .calendar-page {
                width: 100px;
                height: 100px;
                background: #1a1a1a;
                border-radius: 12px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.5), 0 0 40px rgba(255,138,0,0.2);
                padding: 10px;
                animation: pulse 2s ease-in-out infinite;
                border: 1px solid rgba(255,138,0,0.3);
            }
            
            .calendar-header {
                width: 100%;
                height: 20px;
                background: linear-gradient(135deg, #ff8a00 0%, #ff6b00 100%);
                border-radius: 6px 6px 0 0;
                margin-bottom: 8px;
            }
            
            .calendar-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 6px;
            }
            
            .calendar-cell {
                width: 20px;
                height: 20px;
                background: #2a2a2a;
                border-radius: 4px;
                animation: cellPulse 1.5s ease-in-out infinite;
            }
            
            .calendar-cell.active {
                background: linear-gradient(135deg, #ff8a00 0%, #ff6b00 100%);
                animation: cellGlow 1.5s ease-in-out infinite;
            }
            
            .sparkles {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
            }
            
            .sparkle {
                position: absolute;
                width: 8px;
                height: 8px;
                background: #ff8a00;
                border-radius: 50%;
                animation: sparkle 2s ease-in-out infinite;
                box-shadow: 0 0 10px rgba(255,138,0,0.5);
            }
            
            .sparkle:nth-child(1) {
                top: 10%;
                left: 20%;
                animation-delay: 0s;
            }
            
            .sparkle:nth-child(2) {
                top: 70%;
                right: 20%;
                animation-delay: 0.7s;
            }
            
            .sparkle:nth-child(3) {
                bottom: 20%;
                left: 10%;
                animation-delay: 1.4s;
            }
            
            .loading-title {
                color: #ff8a00;
                font-size: 28px;
                margin: 20px 0;
                animation: slideUp 0.6s ease;
                text-shadow: 0 0 20px rgba(255,138,0,0.3);
            }
            
            .loading-steps {
                margin: 30px 0;
                animation: slideUp 0.8s ease;
            }
            
            .step {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 15px;
                padding: 15px;
                margin: 10px auto;
                max-width: 400px;
                background: rgba(255,138,0,0.1);
                border-radius: 12px;
                color: #e5e5e5;
                opacity: 0.5;
                transition: all 0.3s ease;
                border: 1px solid rgba(255,138,0,0.1);
            }
            
            .step-icon {
                font-size: 24px;
                animation: bounce 2s ease-in-out infinite;
            }
            
            .step-text {
                font-size: 16px;
                font-weight: 500;
            }
            
            .step.active {
                opacity: 1;
                background: rgba(255,138,0,0.2);
                transform: scale(1.05);
                border-color: rgba(255,138,0,0.3);
            }
            
            .step-1 { animation: stepActivate 8s ease-in-out infinite; animation-delay: 0s; }
            .step-2 { animation: stepActivate 8s ease-in-out infinite; animation-delay: 2s; }
            .step-3 { animation: stepActivate 8s ease-in-out infinite; animation-delay: 4s; }
            .step-4 { animation: stepActivate 8s ease-in-out infinite; animation-delay: 6s; }
            
            .spinner-container {
                margin: 40px 0 30px;
                display: flex;
                justify-content: center;
                align-items: center;
                animation: slideUp 1s ease;
            }
            
            .spinner {
                width: 60px;
                height: 60px;
                border: 5px solid rgba(255,138,0,0.2);
                border-top-color: #ff8a00;
                border-radius: 50%;
                animation: spin 1s linear infinite;
            }
            
            .loading-subtext {
                color: rgba(255,255,255,0.7);
                font-size: 14px;
                animation: slideUp 1.2s ease;
            }
            
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-20px); }
            }
            
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.05); }
            }
            
            @keyframes cellPulse {
                0%, 100% { opacity: 0.3; }
                50% { opacity: 1; }
            }
            
            @keyframes cellGlow {
                0%, 100% { 
                    box-shadow: 0 0 5px rgba(255,138,0,0.5);
                    transform: scale(1);
                }
                50% { 
                    box-shadow: 0 0 20px rgba(255,138,0,1);
                    transform: scale(1.1);
                }
            }
            
            @keyframes sparkle {
                0%, 100% { 
                    opacity: 0;
                    transform: scale(0);
                }
                50% { 
                    opacity: 1;
                    transform: scale(1);
                }
            }
            
            @keyframes slideUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-5px); }
            }
            
            @keyframes stepActivate {
                0%, 100% { 
                    opacity: 0.5;
                    background: rgba(255,255,255,0.1);
                    transform: scale(1);
                }
                12.5%, 25% { 
                    opacity: 1;
                    background: rgba(255,255,255,0.2);
                    transform: scale(1.05);
                }
            }
        </style>
        
        <script>
            // Auto-redirect to actual generation after showing loading animation
            setTimeout(function() {
                window.location.href = '/generate_schedule_actual';
            }, 1000);
        </script>
        """
    ])

@route
def generate_schedule(state: State, club_name: str = "", club_time: str = "",
                     club_day_monday: str = "", club_day_tuesday: str = "", club_day_wednesday: str = "",
                     club_day_thursday: str = "", club_day_friday: str = "", club_day_saturday: str = "", 
                     club_day_sunday: str = "") -> Page:
    """Show loading page and generate schedule"""
    # Ignore the club parameters - they're just from the form
    
    print(f"\n🎯 GENERATE_SCHEDULE called with {len(state.courses)} courses")
    for i, course in enumerate(state.courses[:3]):
        print(f"  Course {i+1}: {course.name} - {course.days} at {course.time}")
    if len(state.courses) > 3:
        print(f"  ... and {len(state.courses) - 3} more")
    
    # Prepare course and club information
    course_info = "\n".join([
        f"- {c.name} ({c.credits} credits, {c.days} at {c.time})"
        for c in state.courses
    ])
    
    club_info = "\n".join([
        f"- {c.name} on {c.day} at {c.time}"
        for c in state.clubs
    ]) if state.clubs else "No clubs/activities"
    
    # Start with loading page
    loading_html = """
        <div class="loading-overlay" id="loadingOverlay">
            <div class="loading-container">
                <div class="loading-icon">
                    <div class="calendar-animation">
                        <div class="calendar-page">
                            <div class="calendar-header"></div>
                            <div class="calendar-grid">
                                <div class="calendar-cell"></div>
                                <div class="calendar-cell"></div>
                                <div class="calendar-cell"></div>
                                <div class="calendar-cell"></div>
                                <div class="calendar-cell active"></div>
                                <div class="calendar-cell"></div>
                            </div>
                        </div>
                        <div class="sparkles">
                            <div class="sparkle"></div>
                            <div class="sparkle"></div>
                            <div class="sparkle"></div>
                        </div>
                    </div>
                </div>
                <h2 class="loading-title">Creating Your Perfect Study Schedule ✨</h2>
                <div class="loading-steps">
                    <div class="step step-1">
                        <div class="step-icon">📚</div>
                        <div class="step-text">Analyzing your courses</div>
                    </div>
                    <div class="step step-2">
                        <div class="step-icon">🎯</div>
                        <div class="step-text">Optimizing study times</div>
                    </div>
                    <div class="step step-3">
                        <div class="step-icon">💡</div>
                        <div class="step-text">Generating personalized tips</div>
                    </div>
                    <div class="step step-4">
                        <div class="step-icon">📅</div>
                        <div class="step-text">Building your calendar</div>
                    </div>
                </div>
                <div class="spinner-container">
                    <div class="spinner"></div>
                </div>
                <p class="loading-subtext" id="progressText">Preparing your schedule...</p>
            </div>
        </div>
        
        <iframe id="generationFrame" style="display: none;"></iframe>
        """
    
    # Add the same styles from loading_page
    loading_styles = """
        <style>
            .loading-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: linear-gradient(135deg, #0d0d0d 0%, #1a1a1a 50%, #0d0d0d 100%);
                background-image: 
                    radial-gradient(ellipse at 30% 30%, rgba(255, 138, 0, 0.2) 0%, transparent 50%),
                    radial-gradient(ellipse at 70% 70%, rgba(255, 179, 71, 0.15) 0%, transparent 50%);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 9999;
                animation: fadeIn 0.5s ease;
            }
            
            .loading-container {
                text-align: center;
                padding: 40px;
                max-width: 600px;
            }
            
            .calendar-animation {
                position: relative;
                width: 120px;
                height: 120px;
                margin: 0 auto 30px;
                animation: float 3s ease-in-out infinite;
            }
            
            .calendar-page {
                width: 100px;
                height: 100px;
                background: #1a1a1a;
                border-radius: 12px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.5), 0 0 40px rgba(255,138,0,0.2);
                padding: 10px;
                animation: pulse 2s ease-in-out infinite;
                border: 1px solid rgba(255,138,0,0.3);
            }
            
            .calendar-header {
                width: 100%;
                height: 20px;
                background: linear-gradient(135deg, #ff8a00 0%, #ff6b00 100%);
                border-radius: 6px 6px 0 0;
                margin-bottom: 8px;
            }
            
            .calendar-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 6px;
            }
            
            .calendar-cell {
                width: 20px;
                height: 20px;
                background: #2a2a2a;
                border-radius: 4px;
                animation: cellPulse 1.5s ease-in-out infinite;
            }
            
            .calendar-cell.active {
                background: linear-gradient(135deg, #ff8a00 0%, #ff6b00 100%);
                animation: cellGlow 1.5s ease-in-out infinite;
            }
            
            .sparkles {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
            }
            
            .sparkle {
                position: absolute;
                width: 8px;
                height: 8px;
                background: #ff8a00;
                border-radius: 50%;
                animation: sparkle 2s ease-in-out infinite;
                box-shadow: 0 0 10px rgba(255,138,0,0.5);
            }
            
            .sparkle:nth-child(1) {
                top: 10%;
                left: 20%;
                animation-delay: 0s;
            }
            
            .sparkle:nth-child(2) {
                top: 70%;
                right: 20%;
                animation-delay: 0.7s;
            }
            
            .sparkle:nth-child(3) {
                bottom: 20%;
                left: 10%;
                animation-delay: 1.4s;
            }
            
            .loading-title {
                color: white;
                font-size: 28px;
                margin: 20px 0;
                animation: slideUp 0.6s ease;
            }
            
            .loading-steps {
                margin: 30px 0;
                animation: slideUp 0.8s ease;
            }
            
            .step {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 15px;
                padding: 15px;
                margin: 10px auto;
                max-width: 400px;
                background: rgba(255,255,255,0.1);
                border-radius: 12px;
                color: white;
                opacity: 0.5;
                transition: all 0.3s ease;
            }
            
            .step-icon {
                font-size: 24px;
                animation: bounce 2s ease-in-out infinite;
            }
            
            .step-text {
                font-size: 16px;
                font-weight: 500;
            }
            
            .step.active {
                opacity: 1;
                background: rgba(255,255,255,0.2);
                transform: scale(1.05);
            }
            
            .step-1 { animation: stepActivate 8s ease-in-out infinite; animation-delay: 0s; }
            .step-2 { animation: stepActivate 8s ease-in-out infinite; animation-delay: 2s; }
            .step-3 { animation: stepActivate 8s ease-in-out infinite; animation-delay: 4s; }
            .step-4 { animation: stepActivate 8s ease-in-out infinite; animation-delay: 6s; }
            
            .spinner-container {
                margin: 40px 0 30px;
                display: flex;
                justify-content: center;
                align-items: center;
                animation: slideUp 1s ease;
            }
            
            .spinner {
                width: 60px;
                height: 60px;
                border: 5px solid rgba(255,255,255,0.2);
                border-top-color: white;
                border-radius: 50%;
                animation: spin 1s linear infinite;
            }
            
            .loading-subtext {
                color: rgba(255,255,255,0.8);
                font-size: 14px;
                animation: slideUp 1.2s ease;
            }
            
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-20px); }
            }
            
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.05); }
            }
            
            @keyframes cellPulse {
                0%, 100% { opacity: 0.3; }
                50% { opacity: 1; }
            }
            
            @keyframes cellGlow {
                0%, 100% { 
                    box-shadow: 0 0 5px rgba(102,126,234,0.5);
                    transform: scale(1);
                }
                50% { 
                    box-shadow: 0 0 20px rgba(102,126,234,1);
                    transform: scale(1.1);
                }
            }
            
            @keyframes sparkle {
                0%, 100% { 
                    opacity: 0;
                    transform: scale(0);
                }
                50% { 
                    opacity: 1;
                    transform: scale(1);
                }
            }
            
            @keyframes slideUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-5px); }
            }
            
            @keyframes stepActivate {
                0%, 100% { 
                    opacity: 0.5;
                    background: rgba(255,255,255,0.1);
                    transform: scale(1);
                }
                12.5%, 25% { 
                    opacity: 1;
                    background: rgba(255,255,255,0.2);
                    transform: scale(1.05);
                }
            }
        </style>
        
        <script>
            var progressText = document.getElementById('progressText');
            var generationComplete = false;
            
            // Update status text periodically
            var statusMessages = [
                'Analyzing your courses...',
                'Optimizing study times...',
                'Generating personalized tips...',
                'Building your calendar...'
            ];
            var messageIndex = 0;
            
            function updateStatus() {
                if (!generationComplete) {
                    progressText.textContent = statusMessages[messageIndex];
                    messageIndex = (messageIndex + 1) % statusMessages.length;
                    setTimeout(updateStatus, 5000);
                }
            }
            
            // Start status updates
            updateStatus();
            
            // Load the actual generation in an iframe
            var iframe = document.getElementById('generationFrame');
            iframe.onload = function() {
                // Generation complete - redirect immediately to results
                generationComplete = true;
                progressText.textContent = 'Complete! Loading results...';
                window.location.href = '/show_results';
            };
            iframe.src = '/generate_schedule_actual';
        </script>
    """
    
    return Page(state, [loading_html, loading_styles])

@route  
def generate_schedule_actual(state: State) -> Page:
    """Actually generate the schedule with Gemini (called by iframe)"""
    state.current_step = "generate"
    
    # Prepare course and club information
    course_info = "\n".join([
        f"- {c.name} ({c.credits} credits, {c.days} at {c.time})"
        for c in state.courses
    ])
    
    club_info = "\n".join([
        f"- {c.name} on {c.day} at {c.time}"
        for c in state.clubs
    ]) if state.clubs else "No clubs/activities"
    
    # Build explicit blocked time slots for each day of the week
    day_mapping = {
        'M': 'Monday', 'Tu': 'Tuesday', 'W': 'Wednesday', 
        'Th': 'Thursday', 'F': 'Friday', 'Sa': 'Saturday', 'Su': 'Sunday'
    }
    
    # Create a more detailed blocked times structure
    blocked_times = []
    blocked_by_day = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}
    
    for course in state.courses:
        # Parse days from course
        days_str = course.days
        i = 0
        course_days = []
        while i < len(days_str):
            if i + 1 < len(days_str) and days_str[i:i+2] in day_mapping:
                course_days.append(day_mapping[days_str[i:i+2]])
                i += 2
            elif days_str[i] in day_mapping:
                course_days.append(day_mapping[days_str[i]])
                i += 1
            else:
                i += 1
        
        for day in course_days:
            blocked_times.append(f"  ❌ {day}: {course.time} → {course.name} (CLASS)")
            if day in blocked_by_day:
                blocked_by_day[day].append(f"{course.time} ({course.name})")
    
    for club in state.clubs:
        blocked_times.append(f"  ❌ {club.day}: {club.time} → {club.name} (ACTIVITY)")
        if club.day in blocked_by_day:
            blocked_by_day[club.day].append(f"{club.time} ({club.name})")
    
    blocked_times_str = "\n".join(blocked_times) if blocked_times else "  None"
    
    # Create a summary by day
    day_summary = []
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        if blocked_by_day[day]:
            day_summary.append(f"  {day}: BUSY at " + ", ".join(blocked_by_day[day]))
    day_summary_str = "\n".join(day_summary) if day_summary else "  No blocked times"
    
    # GEMINI CALL: Generate structured schedule in simple pipe-delimited format
    schedule_prompt = f"""You are a study scheduling assistant. Create an IDEAL study schedule for a {state.major} student.

SEMESTER: {state.semester_start} to {state.semester_end}

═══════════════════════════════════════════════════════════════════════════════
⚠️⚠️⚠️ CRITICAL: READ ALL BLOCKED TIMES CAREFULLY BEFORE GENERATING ⚠️⚠️⚠️
═══════════════════════════════════════════════════════════════════════════════

STUDENT'S CLASS SCHEDULE (NEVER OVERLAP WITH THESE):
{course_info}

STUDENT'S CLUB ACTIVITIES (NEVER OVERLAP WITH THESE):
{club_info}

═══════════════════════════════════════════════════════════════════════════════
⛔⛔⛔ BLOCKED TIME SLOTS - ABSOLUTELY NO STUDY SESSIONS HERE: ⛔⛔⛔
═══════════════════════════════════════════════════════════════════════════════
{blocked_times_str}
  ❌ EVERY DAY: 11:00 PM to 6:00 AM (sleep time)

DAILY SCHEDULE (WHEN STUDENT IS BUSY):
{day_summary_str}

═══════════════════════════════════════════════════════════════════════════════
✅ SAFE TIME WINDOWS FOR STUDY SESSIONS:
═══════════════════════════════════════════════════════════════════════════════
- Early Morning: 6:00 AM - 8:00 AM (before classes start)
- Between Classes: ONLY if there is 1+ HOUR GAP and study session ENDS 10 min before next class
- After ALL Classes End: Usually after 3:00 PM - 5:00 PM depending on schedule
- Evening: 6:00 PM - 10:00 PM (BEST TIME - prioritize this!)
- Weekends: Saturday and Sunday are great for longer sessions

═══════════════════════════════════════════════════════════════════════════════
🚫 OVERLAP VALIDATION RULES - CHECK EACH SESSION AGAINST THESE:
═══════════════════════════════════════════════════════════════════════════════
For EVERY study session you generate, verify:
1. The START TIME is NOT during any class/activity listed above
2. The END TIME is NOT during any class/activity listed above
3. The session does NOT span across a class time
4. Leave 10-minute buffer BEFORE each class starts

EXAMPLES OF INVALID SESSIONS (DO NOT DO THIS):
- If class is 9:35 AM - 10:55 AM → Study at 9:00-10:00 is INVALID (overlaps)
- If class is 9:35 AM - 10:55 AM → Study at 10:00-11:30 is INVALID (overlaps)
- If class is 9:35 AM - 10:55 AM → Study at 9:00-11:30 is INVALID (spans across)

EXAMPLES OF VALID SESSIONS:
- If class ENDS at 10:55 AM and next is 12:40 PM → Study 11:00-12:30 is VALID
- If last class ends at 3:30 PM → Study 4:00-6:00 PM is VALID
- Evening study at 7:00 PM - 9:00 PM is almost always VALID

═══════════════════════════════════════════════════════════════════════════════

STUDY SESSION RULES:
1. Sessions: 1-2 hours (shorter between classes if needed)
2. Per course: 2-3 study sessions per week
3. More credits = more study time needed
4. Distribute evenly across the week
5. PREFER EVENING (6-10 PM) AND WEEKEND SESSIONS

OUTPUT FORMAT (one session per line):
DATE|START_TIME|END_TIME|COURSE_CODE|DESCRIPTION

Example:
2026-02-03|18:00|20:00|CISC210080|Review data structures concepts
2026-02-04|19:00|21:00|MATH342010|Practice problem sets

RULES:
- 24-hour time format (18:00 not 6:00 PM)
- Date format: YYYY-MM-DD
- Create 50-80 study sessions across the semester
- 5 fields per line separated by |
- Use EXACT course codes from above

DOUBLE-CHECK: Before outputting each line, verify the time slot is FREE on that day.

START OUTPUT (only pipe-delimited lines, no other text):"""

    try:
        # Call Gemini for schedule
        print("=" * 80)
        print("Calling Gemini for schedule generation...")
        print("Blocked times:", blocked_times_str)
        print("Day summary:", day_summary_str)
        print("=" * 80)
        schedule_response = call_gemini([LLMMessage("user", schedule_prompt)])
        
        if isinstance(schedule_response, LLMError):
            state.study_events = []
            state.tips = f"❌ Gemini Error: {schedule_response.message}\n\nPlease try again."
            print(f"Gemini error: {schedule_response.message}")
        else:
            response_text = schedule_response.content.strip()
            print(f"Gemini response ({len(response_text)} chars):")
            print(response_text[:500])
            print("=" * 80)
            
            # Parse the pipe-delimited format
            state.study_events = []
            lines = response_text.strip().split('\n')
            
            for line in lines:
                line = line.strip()
                if not line or '|' not in line:
                    continue
                
                # Split by pipe character
                parts = [p.strip() for p in line.split('|')]
                
                # Must have exactly 5 parts
                if len(parts) != 5:
                    print(f"Skipping invalid line (expected 5 parts, got {len(parts)}): {line}")
                    continue
                
                date_str, start_time, end_time, course_code, description = parts
                
                # Validate date format (YYYY-MM-DD)
                if len(date_str) != 10 or date_str.count('-') != 2:
                    print(f"Skipping invalid date: {date_str}")
                    continue
                
                # Validate time format (HH:MM)
                if len(start_time) < 4 or len(end_time) < 4 or ':' not in start_time or ':' not in end_time:
                    print(f"Skipping invalid time: {start_time} - {end_time}")
                    continue
                
                # Ensure HH:MM format (pad if needed)
                if len(start_time) == 4:  # H:MM format
                    start_time = '0' + start_time
                if len(end_time) == 4:  # H:MM format
                    end_time = '0' + end_time
                
                # Construct ISO datetime strings
                start_datetime = f"{date_str}T{start_time}:00"
                end_datetime = f"{date_str}T{end_time}:00"
                
                # Create event
                event = StudyEvent(
                    title=f"Study {course_code}",
                    start_datetime=start_datetime,
                    end_datetime=end_datetime,
                    course_code=course_code,
                    description=description
                )
                state.study_events.append(event)
                print(f"✓ Added event: {event.title} on {date_str} {start_time}-{end_time}")
            
            print(f"\n✅ Successfully parsed {len(state.study_events)} events")
            
            if len(state.study_events) == 0:
                state.tips = "❌ No events generated. Please try again."
                print("WARNING: No valid events parsed from response")
        
        # SECOND GEMINI CALL: Generate study tips
        if state.study_events:  # Only generate tips if schedule was successful
            print("\nGenerating study tips...")
            tips_prompt = f"""Based on these courses for a {state.major} major:

{course_info}

Provide 5 concise, actionable study tips tailored to these specific subjects. Format as a numbered list.
Focus on:
- Effective study techniques for each subject area
- Time management strategies
- Resource recommendations
- Test preparation advice"""
        
            tips_response = call_gemini([LLMMessage("user", tips_prompt)])
            
            if isinstance(tips_response, LLMError):
                state.tips = "📚 Study your course materials regularly and stay organized!"
            else:
                state.tips = tips_response.content.strip()
                print("Study tips generated successfully")
        else:
            state.tips = "❌ No events generated. Please try again."
            print("Skipping tips generation - no events created")
            
    except Exception as e:
        state.study_events = []
        state.tips = f"❌ Unexpected Error: {str(e)}\n\nPlease try again or check your internet connection."
        print(f"Exception in generate_schedule_actual: {e}")
        import traceback
        traceback.print_exc()
    
    # Return a page that redirects to show_results (with updated state containing study events)
    return show_results(state)

@route
def show_results(state: State) -> Page:
    """Display the AI-generated study schedule with interactive calendar including actual classes"""
    
    import json
    from datetime import datetime, timedelta
    
    # Helper function to convert day abbreviations to weekday numbers
    def parse_days(days_str):
        """Convert 'MW', 'TuTh', etc. to list of weekday numbers (0=Monday, 6=Sunday)"""
        day_map = {
            'M': 0, 'Tu': 1, 'W': 2, 'Th': 3, 'F': 4, 'Sa': 5, 'Su': 6
        }
        days = []
        i = 0
        while i < len(days_str):
            if i + 1 < len(days_str) and days_str[i:i+2] in day_map:
                days.append(day_map[days_str[i:i+2]])
                i += 2
            elif days_str[i] in day_map:
                days.append(day_map[days_str[i]])
                i += 1
            else:
                i += 1
        return days
    
    # Helper function to parse time strings like "9:00 AM - 10:00 AM"
    def parse_time_range(time_str):
        """Parse time string and return (start_hour, start_min, end_hour, end_min)"""
        try:
            print(f"  Parsing time: '{time_str}'")
            
            # Split by ' - ' first (with spaces), then try just '-'
            if ' - ' in time_str:
                parts = time_str.split(' - ')
            elif '-' in time_str:
                parts = time_str.split('-')
            else:
                print(f"  No dash found in time string")
                return None
            
            if len(parts) != 2:
                print(f"  Expected 2 parts, got {len(parts)}")
                return None
            
            start_str = parts[0].strip()
            end_str = parts[1].strip()
            
            print(f"  Start: '{start_str}', End: '{end_str}'")
            
            # Parse start time - try multiple formats
            start_time = None
            for fmt in ['%I:%M %p', '%I:%M%p', '%H:%M', '%I:%M']:
                try:
                    start_time = datetime.strptime(start_str, fmt)
                    break
                except ValueError:
                    continue
            
            if start_time is None:
                print(f"  Could not parse start time: '{start_str}'")
                return None
            
            # Parse end time - try multiple formats
            end_time = None
            for fmt in ['%I:%M %p', '%I:%M%p', '%H:%M', '%I:%M']:
                try:
                    end_time = datetime.strptime(end_str, fmt)
                    break
                except ValueError:
                    continue
            
            if end_time is None:
                print(f"  Could not parse end time: '{end_str}'")
                return None
            
            result = (start_time.hour, start_time.minute, end_time.hour, end_time.minute)
            print(f"  Parsed successfully: {result}")
            return result
        except Exception as e:
            print(f"  Error parsing time: {e}")
            return None
    
    # Generate recurring class events for entire semester
    class_events = []
    if state.courses and state.semester_start and state.semester_end:
        try:
            print(f"Generating class events for {len(state.courses)} courses")
            semester_start = datetime.strptime(state.semester_start, '%Y-%m-%d')
            semester_end = datetime.strptime(state.semester_end, '%Y-%m-%d')
            
            for course in state.courses:
                print(f"Processing course: {course.name}, Days: {course.days}, Time: {course.time}")
                weekdays = parse_days(course.days)
                time_parts = parse_time_range(course.time)
                
                print(f"  Parsed weekdays: {weekdays}, time_parts: {time_parts}")
                
                if not weekdays or not time_parts:
                    print(f"  Skipping course {course.name} - invalid days or time")
                    continue
                
                start_hour, start_min, end_hour, end_min = time_parts
                
                # Generate events for each occurrence of the class
                current_date = semester_start
                event_count = 0
                while current_date <= semester_end:
                    if current_date.weekday() in weekdays:
                        class_start = current_date.replace(hour=start_hour, minute=start_min, second=0)
                        class_end = current_date.replace(hour=end_hour, minute=end_min, second=0)
                        
                        class_events.append({
                            "title": f"📚 {course.name}",
                            "start": class_start.strftime('%Y-%m-%dT%H:%M:%S'),
                            "end": class_end.strftime('%Y-%m-%dT%H:%M:%S'),
                            "description": f"{course.name} - {course.credits} credits",
                            "backgroundColor": "#e74c3c",  # Red for classes
                            "borderColor": "#c0392b",
                            "extendedProps": {
                                "type": "class",
                                "course": course.name,
                                "description": f"Class: {course.name}"
                            }
                        })
                        event_count += 1
                    
                    current_date += timedelta(days=1)
                print(f"  Generated {event_count} class meetings for {course.name}")
        except Exception as e:
            print(f"Error generating class events: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"Total class events generated: {len(class_events)}")
    
    # Convert StudyEvent objects to JSON for JavaScript (study sessions)
    study_events = [
        {
            "title": event.title,
            "start": event.start_datetime,
            "end": event.end_datetime,
            "description": event.description,
            "backgroundColor": "#ff8a00",  # Orange for study sessions
            "borderColor": "#ff6b00",
            "extendedProps": {
                "type": "study",
                "course": event.course_code,
                "description": event.description
            }
        }
        for event in state.study_events
    ]
    
    # Generate club/activity events for entire semester
    club_events = []
    if state.clubs and state.semester_start and state.semester_end:
        try:
            print(f"Generating club events for {len(state.clubs)} clubs")
            semester_start = datetime.strptime(state.semester_start, '%Y-%m-%d')
            semester_end = datetime.strptime(state.semester_end, '%Y-%m-%d')
            
            # Day name to weekday number mapping
            day_name_map = {
                'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
                'Friday': 4, 'Saturday': 5, 'Sunday': 6
            }
            
            for club in state.clubs:
                print(f"Processing club: {club.name}, Day: {club.day}, Time: {club.time}")
                
                # Get weekday number from day name
                weekday = day_name_map.get(club.day)
                if weekday is None:
                    print(f"  Skipping club {club.name} - invalid day: {club.day}")
                    continue
                
                # Parse the time
                time_parts = parse_time_range(club.time)
                if not time_parts:
                    print(f"  Skipping club {club.name} - invalid time: {club.time}")
                    continue
                
                start_hour, start_min, end_hour, end_min = time_parts
                
                # Generate events for each occurrence
                current_date = semester_start
                event_count = 0
                while current_date <= semester_end:
                    if current_date.weekday() == weekday:
                        club_start = current_date.replace(hour=start_hour, minute=start_min, second=0)
                        club_end = current_date.replace(hour=end_hour, minute=end_min, second=0)
                        
                        club_events.append({
                            "title": f"🎯 {club.name}",
                            "start": club_start.strftime('%Y-%m-%dT%H:%M:%S'),
                            "end": club_end.strftime('%Y-%m-%dT%H:%M:%S'),
                            "description": f"Club/Activity: {club.name}",
                            "backgroundColor": "#9b59b6",  # Purple for clubs
                            "borderColor": "#8e44ad",
                            "extendedProps": {
                                "type": "club",
                                "name": club.name,
                                "description": f"Activity: {club.name}"
                            }
                        })
                        event_count += 1
                    
                    current_date += timedelta(days=1)
                print(f"  Generated {event_count} club meetings for {club.name}")
        except Exception as e:
            print(f"Error generating club events: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"Total club events generated: {len(club_events)}")
    
    # Combine all events
    all_events_json = json.dumps(study_events + class_events + club_events)
    
    # JavaScript for FullCalendar with filters
    calendar_js = f"""
    <link href='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.10/index.global.min.css' rel='stylesheet' />
    <script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.10/index.global.min.js'></script>
    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        var calendarEl = document.getElementById('results-calendar');
        if (!calendarEl) {{
            console.error('Calendar element not found!');
            return;
        }}
        
        // All events from Python (study sessions + class meetings)
        var allEvents = {all_events_json};
        console.log('Loaded', allEvents.length, 'total events');
        
        var calendar = new FullCalendar.Calendar(calendarEl, {{
            initialView: 'timeGridWeek',
            initialDate: '{state.semester_start}',
            headerToolbar: {{
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
            }},
            slotMinTime: '06:00:00',
            slotMaxTime: '23:00:00',
            allDaySlot: false,
            height: 'auto',
            events: allEvents,
            eventClick: function(info) {{
                var eventType = info.event.extendedProps.type === 'class' ? '📚 Class' : '✏️ Study Session';
                var eventDetails = 
                    eventType + '\\n\\n' +
                    '🏷️ ' + info.event.title + '\\n\\n' +
                    '🕒 ' + info.event.start.toLocaleString('en-US', {{ 
                        weekday: 'long', 
                        month: 'long', 
                        day: 'numeric',
                        hour: 'numeric',
                        minute: '2-digit'
                    }}) + '\\n' +
                    '   to ' + info.event.end.toLocaleTimeString('en-US', {{ 
                        hour: 'numeric',
                        minute: '2-digit'
                    }}) + '\\n\\n';
                
                if (info.event.extendedProps.description) {{
                    eventDetails += '📝 ' + info.event.extendedProps.description;
                }}
                
                alert(eventDetails);
            }},
            eventDidMount: function(info) {{
                // Add tooltip on hover
                info.el.title = info.event.title + '\\n' + 
                    info.event.start.toLocaleTimeString() + ' - ' + 
                    info.event.end.toLocaleTimeString();
            }}
        }});
        
        calendar.render();
        console.log('Calendar rendered successfully!');
        
        // Filter functionality
        var showStudy = true;
        var showClasses = true;
        var showClubs = true;
        
        function updateCalendar() {{
            var filteredEvents = allEvents.filter(function(event) {{
                if (event.extendedProps.type === 'study' && !showStudy) return false;
                if (event.extendedProps.type === 'class' && !showClasses) return false;
                if (event.extendedProps.type === 'club' && !showClubs) return false;
                return true;
            }});
            calendar.removeAllEvents();
            calendar.addEventSource(filteredEvents);
            
            // Update count
            var studyCount = filteredEvents.filter(e => e.extendedProps.type === 'study').length;
            var classCount = filteredEvents.filter(e => e.extendedProps.type === 'class').length;
            var clubCount = filteredEvents.filter(e => e.extendedProps.type === 'club').length;
            document.getElementById('event-count').textContent = 
                'Showing ' + filteredEvents.length + ' events (' + 
                studyCount + ' study, ' + classCount + ' classes, ' + clubCount + ' activities)';
        }}
        
        document.getElementById('filter-study').addEventListener('change', function(e) {{
            showStudy = e.target.checked;
            updateCalendar();
        }});
        
        document.getElementById('filter-classes').addEventListener('change', function(e) {{
            showClasses = e.target.checked;
            updateCalendar();
        }});
        
        document.getElementById('filter-clubs').addEventListener('change', function(e) {{
            showClubs = e.target.checked;
            updateCalendar();
        }});
    }});
    </script>
    """
    
    return Page(state, [
        Div(
            calendar_js,
            change_text_align(Header("Your Personalized Study Schedule 📚", 1), "center"),
            LineBreak(),
            change_text_align(
                Div(
                    f"Major: {state.major}",
                    LineBreak(),
                    f"Semester: {state.semester_start} to {state.semester_end}",
                    LineBreak(),
                    f"Total Events: {len(state.study_events) + len(class_events) + len(club_events)} ({len(state.study_events)} study + {len(class_events)} classes + {len(club_events)} activities)",
                    classes="info-box"
                ),
                "center"
            ),
            LineBreak(),
            HorizontalRule(),
            LineBreak(),
            
            # Calendar View
            change_color(Header("📅 Your Complete Schedule", 2), "#ff8a00"),
            "<p id='event-count' style='color: #999; font-size: 14px;'>Showing " + str(len(state.study_events) + len(class_events) + len(club_events)) + " events (" + str(len(state.study_events)) + " study sessions, " + str(len(class_events)) + " classes, " + str(len(club_events)) + " activities)</p>",
            
            # Filters
            """<div style='display: flex; gap: 20px; margin-bottom: 20px; padding: 15px; background: #1f1f1f; border-radius: 10px; border: 1px solid #333; flex-wrap: wrap;'>
                <label style='display: flex; align-items: center; cursor: pointer; color: #e5e5e5;'>
                    <input type='checkbox' id='filter-study' checked style='margin-right: 10px; width: 18px; height: 18px; cursor: pointer; accent-color: #ff8a00;'>
                    <span style='font-weight: 500;'>✏️ Study Sessions</span>
                </label>
                <label style='display: flex; align-items: center; cursor: pointer; color: #e5e5e5;'>
                    <input type='checkbox' id='filter-classes' checked style='margin-right: 10px; width: 18px; height: 18px; cursor: pointer; accent-color: #ff8a00;'>
                    <span style='font-weight: 500;'>📚 Classes</span>
                </label>
                <label style='display: flex; align-items: center; cursor: pointer; color: #e5e5e5;'>
                    <input type='checkbox' id='filter-clubs' checked style='margin-right: 10px; width: 18px; height: 18px; cursor: pointer; accent-color: #9b59b6;'>
                    <span style='font-weight: 500;'>🎯 Clubs/Activities</span>
                </label>
            </div>""",
            
            # Calendar Container
            "<div id='results-calendar' style='background: #1a1a1a; padding: 20px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.4), 0 0 30px rgba(255,138,0,0.1); min-height: 600px; border: 1px solid rgba(255,138,0,0.2);'></div>",
            
            LineBreak(),
            LineBreak(),
            HorizontalRule(),
            LineBreak(),
            
            # Tips Section
            change_color(Header("💡 Study Tips & Recommendations", 2), "#ff8a00"),
            change_background_color(
                change_padding(PreformattedText(state.tips), "20px"),
                "#1f1f1f"
            ),
            
            LineBreak(),
            LineBreak(),
            HorizontalRule(),
            LineBreak(),
            
            # Button to go back
            Button("🔄 Start Over", "/"),
            
            classes="container"
        )
    ])

@route
def export_csv(state: State) -> Page:
    """Export all events (study sessions + classes) to CSV format"""
    from datetime import datetime, timedelta
    import io
    
    # Helper functions (same as in show_results)
    def parse_days(days_str):
        day_map = {'M': 0, 'Tu': 1, 'W': 2, 'Th': 3, 'F': 4, 'Sa': 5, 'Su': 6}
        days = []
        i = 0
        while i < len(days_str):
            if i + 1 < len(days_str) and days_str[i:i+2] in day_map:
                days.append(day_map[days_str[i:i+2]])
                i += 2
            elif days_str[i] in day_map:
                days.append(day_map[days_str[i]])
                i += 1
            else:
                i += 1
        return days
    
    def parse_time_range(time_str):
        try:
            # Split by ' - ' first (with spaces), then try just '-'
            if ' - ' in time_str:
                parts = time_str.split(' - ')
            elif '-' in time_str:
                parts = time_str.split('-')
            else:
                return None
            
            if len(parts) != 2:
                return None
            
            start_str = parts[0].strip()
            end_str = parts[1].strip()
            
            # Parse start time - try multiple formats
            start_time = None
            for fmt in ['%I:%M %p', '%I:%M%p', '%H:%M', '%I:%M']:
                try:
                    start_time = datetime.strptime(start_str, fmt)
                    break
                except ValueError:
                    continue
            
            if start_time is None:
                return None
            
            # Parse end time - try multiple formats
            end_time = None
            for fmt in ['%I:%M %p', '%I:%M%p', '%H:%M', '%I:%M']:
                try:
                    end_time = datetime.strptime(end_str, fmt)
                    break
                except ValueError:
                    continue
            
            if end_time is None:
                return None
            
            return (start_time.hour, start_time.minute, end_time.hour, end_time.minute)
        except:
            return None
    
    # Build CSV content
    csv_lines = []
    csv_lines.append("Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location")
    
    # Add study sessions
    for event in state.study_events:
        try:
            start_dt = datetime.fromisoformat(event.start_datetime)
            end_dt = datetime.fromisoformat(event.end_datetime)
            
            csv_lines.append(
                f'"{event.title}",'
                f'{start_dt.strftime("%m/%d/%Y")},'
                f'{start_dt.strftime("%I:%M %p")},'
                f'{end_dt.strftime("%m/%d/%Y")},'
                f'{end_dt.strftime("%I:%M %p")},'
                f'False,'
                f'"{event.description}",'
                f'""'
            )
        except Exception as e:
            print(f"Error exporting study event: {e}")
    
    # Add class meetings
    if state.courses and state.semester_start and state.semester_end:
        try:
            semester_start = datetime.strptime(state.semester_start, '%Y-%m-%d')
            semester_end = datetime.strptime(state.semester_end, '%Y-%m-%d')
            
            for course in state.courses:
                weekdays = parse_days(course.days)
                time_parts = parse_time_range(course.time)
                
                if not weekdays or not time_parts:
                    continue
                
                start_hour, start_min, end_hour, end_min = time_parts
                
                current_date = semester_start
                while current_date <= semester_end:
                    if current_date.weekday() in weekdays:
                        class_start = current_date.replace(hour=start_hour, minute=start_min, second=0)
                        class_end = current_date.replace(hour=end_hour, minute=end_min, second=0)
                        
                        csv_lines.append(
                            f'"{course.name}",'
                            f'{class_start.strftime("%m/%d/%Y")},'
                            f'{class_start.strftime("%I:%M %p")},'
                            f'{class_end.strftime("%m/%d/%Y")},'
                            f'{class_end.strftime("%I:%M %p")},'
                            f'False,'
                            f'"Class: {course.name} - {course.credits} credits",'
                            f'""'
                        )
                    
                    current_date += timedelta(days=1)
        except Exception as e:
            print(f"Error exporting class events: {e}")
    
    csv_content = "\n".join(csv_lines)
    
    # Return as downloadable file
    return Page(state, [
        f"""
        <script>
            // Create a blob and trigger download
            var csvContent = `{csv_content}`;
            var blob = new Blob([csvContent], {{ type: 'text/csv;charset=utf-8;' }});
            var link = document.createElement('a');
            var url = URL.createObjectURL(blob);
            link.setAttribute('href', url);
            link.setAttribute('download', 'my_schedule_{state.semester_start}.csv');
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            
            // Redirect back to results after a moment
            setTimeout(function() {{
                window.location.href = '/show_results';
            }}, 500);
        </script>
        <div style='text-align: center; padding: 50px;'>
            <h2>📥 Downloading your schedule...</h2>
            <p>If the download doesn't start automatically, <a href='/show_results'>click here</a> to return to your schedule.</p>
        </div>
        """
    ])

hide_debug_information()
start_server(State())
