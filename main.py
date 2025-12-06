from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

from meta import *

# hide_debug_information()
# set_website_framed(False)
set_website_title("TaskAI")
set_site_information(
    "author",
    """
Your description can go here.
""",
    [],
    [],
    [],
)

@dataclass
class State:
    pass
@dataclass
class Course:
    name: str
    credit_hour: str
    priority: str
@dataclass 
class ClubActivity:
    name: str
    schedule: list[str]
    duration: str
@dataclass
class Schedule:
    pass

@route
def index(state: State) -> Page:
    return Page(state, content=[bold("Welcome to TaskAI!")])


start_server(State())
