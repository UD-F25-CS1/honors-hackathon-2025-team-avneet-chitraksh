# This contains the new show_results function - copy this to main.py

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
        #67
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
                    '📌 ' + info.event.title + '\\n\\n' +
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
