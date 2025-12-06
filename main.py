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
class State:
    major: str = ""
    courses: list[Course] = field(default_factory=list)
    clubs: list[ClubActivity] = field(default_factory=list)
    study_schedule: str = ""
    tips: str = ""
    current_step: str = "welcome"  # welcome, major, courses, clubs, generate
    
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
        Header("Add Course Manually", 2),
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
        Button("Add Course", add_course),
        LineBreak(),
        LineBreak(),
        Button("← Back", choose_course_input)
    ])

@route
def add_course(state: State, course_name: str, credits: str, days: str, time: str) -> Page:
    """Add a course to the list"""
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
        Header("Your Courses", 2),
        LineBreak(),
        f"Major: {bold(state.major)}",
        LineBreak(),
        LineBreak(),
        NumberedList(course_list) if course_list else "No courses added yet.",
        LineBreak(),
        Button("Add Another Course", manual_course_entry),
        " ",
        Button("Next: Add Clubs/Activities", clubs_page) if state.courses else "",
        LineBreak(),
        LineBreak(),
        Button("← Back", choose_course_input)
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
    """Generate AI study schedule using Gemini"""
    state.current_step = "generate"
    
    # Prepare prompt for Gemini
    course_info = "\n".join([
        f"- {c.name} ({c.credits} credits, {c.days} at {c.time})"
        for c in state.courses
    ])
    
    club_info = "\n".join([
        f"- {c.name} on {c.day} at {c.time}"
        for c in state.clubs
    ]) if state.clubs else "No clubs/activities"
    
    prompt = f"""You are a study scheduling assistant. A student majoring in {state.major} needs help creating a study schedule for the next couple of weeks.

Their courses:
{course_info}

Their clubs/activities:
{club_info}

IMPORTANT CONSTRAINTS:
- DO NOT schedule any study sessions between 11:00 PM and 6:00 AM (students need sleep!)
- Only schedule study sessions between 6:00 AM and 11:00 PM
- Avoid scheduling during their class times and club activities
- Consider meal times (breakfast, lunch, dinner)

Please create:
1. A detailed weekly study schedule for the next 2 weeks with specific day/time blocks for each course
   - Include date, day of week, time range, and subject
   - Suggest 1-3 hour study blocks
   - Prioritize courses based on their major ({state.major}) and credit hours
   - Balance the workload across the week
   
2. Subject-specific study tips for each course
   - Tailor recommendations to the course subject
   - Suggest study techniques appropriate for that field

Format your response in two clear sections:

STUDY SCHEDULE:
Week 1:
[specific dates, days, times and subjects - remember no scheduling between 11pm-6am]

Week 2:
[specific dates, days, times and subjects - remember no scheduling between 11pm-6am]

STUDY TIPS:
[tips for each specific course]"""
    
    conversation = [LLMMessage("user", prompt)]
    
    try:
        response = call_gemini(conversation)
        
        # Check if response is an error
        if isinstance(response, LLMError):
            state.study_schedule = f"Error: {response.message}"
            state.tips = "The AI service encountered an issue. Please make sure the Gemini proxy server is accessible and try again."
        else:
            # Response is LLMResponse, extract content
            full_response = response.content
            
            # Try to split into schedule and tips
            if "STUDY TIPS:" in full_response:
                parts = full_response.split("STUDY TIPS:")
                state.study_schedule = parts[0].replace("STUDY SCHEDULE:", "").strip()
                state.tips = parts[1].strip()
            else:
                state.study_schedule = full_response
                state.tips = "Check your schedule above for details!"
            
    except Exception as e:
        state.study_schedule = f"Error generating schedule: {str(e)}"
        state.tips = "Please try again or check your internet connection."
    
    return show_results(state)

@route
def show_results(state: State) -> Page:
    """Display the AI-generated study schedule and tips"""
    return Page(state, [
        Div(
            change_text_align(Header("Your Personalized Study Schedule 📚", 1), "center"),
            LineBreak(),
            change_text_align(
                Div(
                    "Major: ",
                    change_color(bold(state.major), "#764ba2"),
                    classes="info-box"
                ),
                "center"
            ),
            LineBreak(),
            HorizontalRule(),
            LineBreak(),
            change_color(Header("📅 Study Schedule", 2), "#667eea"),
            change_background_color(
                change_padding(PreformattedText(state.study_schedule), "20px"),
                "#f8f9fa"
            ),
            LineBreak(),
            HorizontalRule(),
            LineBreak(),
            change_color(Header("💡 Study Tips & Recommendations", 2), "#667eea"),
            change_background_color(
                change_padding(PreformattedText(state.tips), "20px"),
                "#f8f9fa"
            ),
            LineBreak(),
            HorizontalRule(),
            LineBreak(),
            Div(
                Button("🔄 Start Over", index),
                " ",
                Button("✏️ Modify Activities", clubs_page),
                classes="button-group"
            ),
            LineBreak(),
            change_text_align(
                change_color(
                    "💾 Tip: Screenshot this schedule for easy reference!",
                    "#666"
                ),
                "center"
            ),
            classes="container"
        )
    ])
hide_debug_information()
# Start the server
start_server(State())


start_server(State())
