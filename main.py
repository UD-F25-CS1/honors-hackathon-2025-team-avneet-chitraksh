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

# Modern Custom CSS Styling
add_website_css("""
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        padding: 20px;
        color: #333;
        line-height: 1.6;
    }
    
    /* Main container */
    .container {
        max-width: 900px;
        margin: 0 auto;
        background: white;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        padding: 40px;
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Headers */
    h1 {
        color: #667eea;
        font-size: 2.5em;
        font-weight: 700;
        margin-bottom: 10px;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    h2 {
        color: #764ba2;
        font-size: 1.8em;
        font-weight: 600;
        margin: 25px 0 15px 0;
        padding-bottom: 10px;
        border-bottom: 3px solid #667eea;
    }
    
    h3 {
        color: #555;
        font-size: 1.3em;
        font-weight: 600;
        margin: 20px 0 10px 0;
    }
    
    /* Buttons */
    button, .button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 5px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        font-family: 'Inter', sans-serif;
    }
    
    button:hover, .button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    button:active {
        transform: translateY(0);
    }
    
    /* Input fields */
    input[type="text"], input[type="file"], textarea, select {
        width: 100%;
        padding: 12px 15px;
        margin: 8px 0;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        font-size: 16px;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        background: #f8f9fa;
    }
    
    input[type="text"]:focus, textarea:focus, select:focus {
        outline: none;
        border-color: #667eea;
        background: white;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    select {
        cursor: pointer;
        appearance: none;
        background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23667eea' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
        background-repeat: no-repeat;
        background-position: right 10px center;
        background-size: 20px;
        padding-right: 40px;
    }
    
    /* Lists */
    ul, ol {
        margin: 15px 0;
        padding-left: 25px;
    }
    
    li {
        margin: 10px 0;
        padding: 12px;
        background: #f8f9fa;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        transition: all 0.2s ease;
    }
    
    li:hover {
        background: #e8eaf6;
        transform: translateX(5px);
    }
    
    /* Cards */
    .card {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 12px;
        margin: 15px 0;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        border-color: #667eea;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.15);
    }
    
    /* Horizontal rules */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 30px 0;
    }
    
    /* Pre-formatted text (for schedule display) */
    pre {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 12px;
        border-left: 4px solid #667eea;
        overflow-x: auto;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        line-height: 1.6;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
    
    /* Bold and italic text */
    strong, b {
        color: #764ba2;
        font-weight: 600;
    }
    
    em, i {
        color: #666;
        font-style: italic;
    }
    
    /* Links */
    a {
        color: #667eea;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    
    a:hover {
        color: #764ba2;
        text-decoration: underline;
    }
    
    /* Step indicator */
    .step-indicator {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        display: inline-block;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 20px;
    }
    
    /* Info box */
    .info-box {
        background: #e8eaf6;
        padding: 15px 20px;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 15px 0;
        color: #555;
    }
    
    /* Success message */
    .success {
        background: #d4edda;
        color: #155724;
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
    
# Helper function to parse CSV
def parse_course_csv(csv_content: str) -> list[Course]:
    """Parse CSV content and return list of courses"""
    courses = []
    lines = csv_content.strip().split('\n')
    
    # Skip header if present
    start_idx = 1 if lines and ('course' in lines[0].lower() or 'name' in lines[0].lower()) else 0
    
    for line in lines[start_idx:]:
        if line.strip():
            parts = [p.strip() for p in line.split(',')]
            if len(parts) >= 4:
                courses.append(Course(
                    name=parts[0],
                    credits=int(parts[1]) if parts[1].isdigit() else 3,
                    days=parts[2],
                    time=parts[3]
                ))
    return courses

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
        state.courses = parse_course_csv(csv_file)
        return show_courses(state)
    except Exception as e:
        return Page(state, [
            Header("Error Parsing CSV", 2),
            LineBreak(),
            f"There was an error parsing your CSV: {str(e)}",
            LineBreak(),
            LineBreak(),
            "Please make sure your CSV follows this format:",
            LineBreak(),
            italic("Course Name, Credits, Days, Time"),
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
            TextBox("course_name"),
            LineBreak(),
            LineBreak(),
            "Credits:",
            LineBreak(),
            SelectBox("credits", ["1", "2", "3", "4", "5"], "3"),
            LineBreak(),
            LineBreak(),
            "Days (e.g., MWF, TTh, MW):",
            LineBreak(),
            TextBox("days"),
            LineBreak(),
            LineBreak(),
            "Time (e.g., 9:00 AM - 9:50 AM):",
            LineBreak(),
            TextBox("time"),
            LineBreak(),
            LineBreak(),
            Button("Add Course", "/add_course"),
            LineBreak(),
            LineBreak(),
            Button("← Back", "/choose_course_input"),
            classes="container"
        )
    ])

@route
def add_course(state: State, course_name: str, credits: str, days: str, time: str, 
               semester_start: str, semester_end: str) -> Page:
    """Add a course to the list and update semester dates"""
    # Update semester dates if provided
    if semester_start:
        state.semester_start = semester_start
    if semester_end:
        state.semester_end = semester_end
    
    # Add course if all fields are filled
    if course_name and days and time:
        state.courses.append(Course(
            name=course_name,
            credits=int(credits),
            days=days,
            time=time
        ))
    return show_courses(state)

@route
def show_courses(state: State) -> Page:
    """Display all courses and option to continue"""
    course_list = [f"{c.name} ({c.credits} credits) - {c.days} at {c.time}" for c in state.courses]
    
    return Page(state, [
        Div(
            Header("Your Courses", 2),
            LineBreak(),
            f"Major: {state.major}",
            LineBreak(),
            f"Semester: {state.semester_start} to {state.semester_end}",
            LineBreak(),
            LineBreak(),
            NumberedList(course_list) if course_list else "No courses added yet.",
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
        "Day:",
        LineBreak(),
        SelectBox("club_day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]),
        LineBreak(),
        LineBreak(),
        "Time:",
        LineBreak(),
        TextBox("club_time"),
        LineBreak(),
        LineBreak(),
        Button("Add Activity", add_club),
        LineBreak(),
        LineBreak(),
        HorizontalRule(),
        LineBreak(),
        Header("Your Activities:", 3),
        BulletedList(club_list) if club_list else "No activities added yet.",
        LineBreak(),
        LineBreak(),
        Button("Generate Study Schedule", generate_schedule) if state.courses else italic("Please add courses first"),
        LineBreak(),
        LineBreak(),
        Button("← Back to Courses", show_courses)
    ])

@route
def add_club(state: State, club_name: str, club_day: str, club_time: str) -> Page:
    """Add a club activity"""
    if club_name and club_time:
        state.clubs.append(ClubActivity(
            name=club_name,
            day=club_day,
            time=club_time
        ))
    return clubs_page(state)

@route
def generate_schedule(state: State) -> Page:
    """Generate AI study schedule using Gemini with pipe-delimited text output"""
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
    
    # GEMINI CALL: Generate structured schedule in simple pipe-delimited format
    schedule_prompt = f"""You are a study scheduling assistant. Create a study schedule for a {state.major} student.

SEMESTER: {state.semester_start} to {state.semester_end}
Create a comprehensive study schedule for the ENTIRE SEMESTER.

Their courses:
{course_info}

Their clubs/activities:
{club_info}

CONSTRAINTS:
- NO scheduling between 11:00 PM and 6:00 AM (sleep time)
- Avoid class times: {', '.join([f"{c.days} {c.time}" for c in state.courses])}
- Avoid club times: {club_info}
- Create 1-3 hour study blocks
- Prioritize courses based on major ({state.major}) and credit hours
- Schedule throughout the ENTIRE semester from {state.semester_start} to {state.semester_end}

OUTPUT FORMAT - Return each study session on a new line in this EXACT format:
DATE|START_TIME|END_TIME|COURSE_CODE|DESCRIPTION

Example:
2025-12-09|19:00|21:00|CISC210080|Review assembly language programming
2025-12-10|14:00|16:00|MATH342010|Practice linear algebra problems
2025-12-11|08:00|10:00|CPEG202080|Study logic gates and circuits

RULES:
- Use 24-hour time format (e.g., 19:00 not 7:00 PM)
- Date format: YYYY-MM-DD
- Create 50-80 study sessions spread across the ENTIRE semester ({state.semester_start} to {state.semester_end})
- Vary times: morning (08:00-11:00), afternoon (13:00-17:00), evening (18:00-22:00)
- Each line must have exactly 5 fields separated by | (pipe character)
- Distribute sessions evenly throughout the semester
- Increase frequency closer to typical exam periods (midterms around week 8, finals in last 2 weeks)

START OUTPUT (no extra text before or after):"""

    try:
        # Call Gemini for schedule
        print("=" * 80)
        print("Calling Gemini for schedule generation...")
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
        print(f"Exception in generate_schedule: {e}")
        import traceback
        traceback.print_exc()
    
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
            parts = time_str.replace(' ', '').split('-')
            if len(parts) != 2:
                return None
            
            start_str, end_str = parts
            
            # Parse start time
            if 'AM' in start_str or 'PM' in start_str:
                start_time = datetime.strptime(start_str, '%I:%M%p')
            else:
                start_time = datetime.strptime(start_str, '%H:%M')
            
            # Parse end time
            if 'AM' in end_str or 'PM' in end_str:
                end_time = datetime.strptime(end_str, '%I:%M%p')
            else:
                end_time = datetime.strptime(end_str, '%H:%M')
            
            return (start_time.hour, start_time.minute, end_time.hour, end_time.minute)
        except:
            return None
    
    # Generate recurring class events for entire semester
    class_events = []
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
                
                # Generate events for each occurrence of the class
                current_date = semester_start
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
                    
                    current_date += timedelta(days=1)
        except Exception as e:
            print(f"Error generating class events: {e}")
    
    # Convert StudyEvent objects to JSON for JavaScript (study sessions)
    study_events = [
        {
            "title": event.title,
            "start": event.start_datetime,
            "end": event.end_datetime,
            "description": event.description,
            "backgroundColor": "#667eea",  # Purple for study sessions
            "borderColor": "#764ba2",
            "extendedProps": {
                "type": "study",
                "course": event.course_code,
                "description": event.description
            }
        }
        for event in state.study_events
    ]
    
    # Combine all events
    all_events_json = json.dumps(study_events + class_events)
    
    # JavaScript for FullCalendar with filters
    calendar_js = f"""
    <link href='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.10/index.global.min.css' rel='stylesheet' />
    <script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.10/index.global.min.js'></script>
    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        var calendarEl = document.getElementById('calendar');
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
                    '� ' + info.event.title + '\\n\\n' +
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
        
        function updateCalendar() {{
            var filteredEvents = allEvents.filter(function(event) {{
                if (event.extendedProps.type === 'study' && !showStudy) return false;
                if (event.extendedProps.type === 'class' && !showClasses) return false;
                return true;
            }});
            calendar.removeAllEvents();
            calendar.addEventSource(filteredEvents);
            
            // Update count
            document.getElementById('event-count').textContent = 
                'Showing ' + filteredEvents.length + ' events (' + 
                ({len(state.study_events)} + ' study sessions, ' + {len(class_events)} + ' class meetings)';
        }}
        
        document.getElementById('filter-study').addEventListener('change', function(e) {{
            showStudy = e.target.checked;
            updateCalendar();
        }});
        
        document.getElementById('filter-classes').addEventListener('change', function(e) {{
            showClasses = e.target.checked;
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
                    f"Total Events: {len(state.study_events) + len(class_events)} ({len(state.study_events)} study sessions + {len(class_events)} classes)",
                    classes="info-box"
                ),
                "center"
            ),
            LineBreak(),
            HorizontalRule(),
            LineBreak(),
            
            # Filter Sidebar and Calendar Container
            "<div style='display: flex; gap: 20px;'>",
            
            # Sidebar with filters
            """<div style='min-width: 200px; background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); height: fit-content;'>
                <h3 style='margin-top: 0; color: #667eea;'>📊 Filters</h3>
                <div style='margin: 15px 0;'>
                    <label style='display: flex; align-items: center; cursor: pointer; padding: 8px; border-radius: 5px; transition: background 0.2s;' onmouseover='this.style.background="#f8f9fa"' onmouseout='this.style.background="transparent"'>
                        <input type='checkbox' id='filter-study' checked style='margin-right: 10px; width: 18px; height: 18px; cursor: pointer;'>
                        <span style='font-weight: 500;'>✏️ Study Sessions</span>
                    </label>
                </div>
                <div style='margin: 15px 0;'>
                    <label style='display: flex; align-items: center; cursor: pointer; padding: 8px; border-radius: 5px; transition: background 0.2s;' onmouseover='this.style.background="#f8f9fa"' onmouseout='this.style.background="transparent"'>
                        <input type='checkbox' id='filter-classes' checked style='margin-right: 10px; width: 18px; height: 18px; cursor: pointer;'>
                        <span style='font-weight: 500;'>📚 Classes</span>
                    </label>
                </div>
                <hr style='margin: 20px 0; border: none; border-top: 1px solid #e0e0e0;'>
                <div style='font-size: 12px; color: #666; line-height: 1.6;'>
                    <strong>Legend:</strong><br>
                    <span style='display: inline-block; width: 12px; height: 12px; background: #667eea; border-radius: 2px; margin-right: 5px;'></span> Study Sessions<br>
                    <span style='display: inline-block; width: 12px; height: 12px; background: #e74c3c; border-radius: 2px; margin-right: 5px;'></span> Classes
                </div>
            </div>""",
            
            # Calendar View
            "<div style='flex: 1;'>",
            change_color(Header("📅 Interactive Schedule Calendar", 2), "#667eea"),
            "<p id='event-count' style='color: #666;'>Showing " + str(len(state.study_events) + len(class_events)) + " events (" + str(len(state.study_events)) + " study sessions, " + str(len(class_events)) + " class meetings)</p>",
            "<div id='calendar' style='background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); min-height: 600px;'></div>",
            "</div>",
            
            "</div>",  # Close flex container
            
            LineBreak(),
            LineBreak(),
            HorizontalRule(),
            LineBreak(),
            
            # Tips Section
            change_color(Header("💡 Study Tips & Recommendations", 2), "#667eea"),
            change_background_color(
                change_padding(PreformattedText(state.tips), "20px"),
                "#f8f9fa"
            ),
            
            LineBreak(),
            LineBreak(),
            
            # Event List (as backup/reference)
            "<details style='margin: 20px 0;'>",
            "<summary style='cursor: pointer; padding: 10px; background: #f8f9fa; border-radius: 8px; font-weight: 600;'>📋 View Complete Schedule List</summary>",
            "<div style='padding: 20px; background: #f8f9fa;'>",
            "<h4 style='color: #667eea;'>✏️ Study Sessions</h4>",
            *[
                f"<div style='margin: 10px 0; padding: 10px; background: white; border-left: 4px solid #667eea; border-radius: 5px;'>"
                f"<strong>{event.title}</strong><br>"
                f"📅 {event.start_datetime[:10]} | 🕒 {event.start_datetime[11:16]} - {event.end_datetime[11:16]}<br>"
                f"📝 {event.description}</div>"
                for event in state.study_events
            ] if state.study_events else ["<p>No study sessions generated.</p>"],
            "<h4 style='color: #e74c3c; margin-top: 20px;'>📚 Classes</h4>",
            *[
                f"<div style='margin: 10px 0; padding: 10px; background: white; border-left: 4px solid #e74c3c; border-radius: 5px;'>"
                f"<strong>{course.name}</strong><br>"
                f"📅 {course.days} | 🕒 {course.time}<br>"
                f"📝 {course.credits} credits</div>"
                for course in state.courses
            ] if state.courses else ["<p>No classes added.</p>"],
            "</div>",
            "</details>",
            
            LineBreak(),
            HorizontalRule(),
            LineBreak(),
            Div(
                Button("🔄 Start Over", "/"),
                " ",
                Button("✏️ Modify Schedule", "/clubs_page"),
                classes="button-group"
            ),
            LineBreak(),
            change_text_align(
                Text("💡 Tip: Use the sidebar filters to show/hide study sessions or classes. Click on calendar events to see details!"),
                "center"
            ),
            classes="container"
        )
    ])
hide_debug_information()
start_server(State())
