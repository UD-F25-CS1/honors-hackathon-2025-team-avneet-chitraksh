from bakery import assert_equal
from drafter import *
from dataclasses import dataclass, field
from drafter.llm import *
from meta import *

# Configure website
set_website_title("TaskAI - Smart Study Scheduler")
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
        Header("Welcome to TaskAI! 🎓", 1),
        LineBreak(),
        "Your AI-powered study scheduler that helps you balance coursework and activities.",
        LineBreak(),
        LineBreak(),
        "TaskAI will help you:",
        BulletedList([
            "Organize your class schedule",
            "Track your extracurricular activities",
            "Generate personalized study sessions",
            "Get AI-powered study tips for each subject"
        ]),
        LineBreak(),
        Button("Get Started", set_major)
    ])

@route
def set_major(state: State) -> Page:
    """Step 1: Ask for major"""
    state.current_step = "major"
    return Page(state, [
        Header("Step 1: Tell us your major", 2),
        LineBreak(),
        "Your major helps us prioritize which classes need more study time:",
        LineBreak(),
        LineBreak(),
        TextBox("major_input", state.major),
        LineBreak(),
        Button("Next: Add Courses", save_major, [Argument("major", state.major)])
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
    
    prompt = f"""You are a study scheduling assistant. A student majoring in {state.major} needs help creating a study schedule.

Their courses:
{course_info}

Their clubs/activities:
{club_info}

Please create:
1. A weekly study schedule with specific time blocks for each course
2. Study tips tailored to each subject/course
3. Prioritize courses based on their major ({state.major}) and credit hours

Format your response in two clear sections:
STUDY SCHEDULE:
[specific times and subjects]

STUDY TIPS:
[tips for each course]"""
    
    conversation = [LLMMessage("user", prompt)]
    
    try:
        response = call_gemini(conversation)
        
        # Check if response is an error
        if isinstance(response, LLMError):
            state.study_schedule = f"Error: {response.error}"
            state.tips = "The AI service encountered an issue. Please make sure the Gemini server is accessible and try again."
        else:
            # Response is LLMResponse, extract text
            full_response = response.text
            
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
        Header("Your Personalized Study Schedule 📚", 1),
        LineBreak(),
        f"Major: {bold(state.major)}",
        LineBreak(),
        LineBreak(),
        HorizontalRule(),
        LineBreak(),
        Header("Study Schedule:", 2),
        PreformattedText(state.study_schedule),
        LineBreak(),
        HorizontalRule(),
        LineBreak(),
        Header("Study Tips & Recommendations:", 2),
        PreformattedText(state.tips),
        LineBreak(),
        HorizontalRule(),
        LineBreak(),
        Button("Start Over", index),
        " ",
        Button("Modify Clubs", clubs_page),
        LineBreak(),
        LineBreak(),
        italic("Tip: Screenshot this schedule for easy reference!")
    ])
hide_debug_information()
# Start the server
start_server(State())


start_server(State())
