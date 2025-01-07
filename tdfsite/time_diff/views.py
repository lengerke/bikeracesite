from django.shortcuts import render
from datetime import datetime, timedelta
from .models import TimeEntry  # Import the model

# Fixed time for calculation (e.g., midnight or any other fixed time)
FIXED_TIME = "09:00"  # Fixed time in HH:mm format

def calculate_time_difference(request):
    time_diff = None
    error_message = None
    if request.method == "POST":
        user_name = request.POST.get("user_name")  # Get the user's name from the form
        user_input_time = request.POST.get("user_time")  # Get the user's input time
        if user_name and user_input_time:
            try:
                # Parse the times from string (HH:mm format)
                fixed_time_obj = datetime.strptime(FIXED_TIME, "%H:%M")
                user_time_obj = datetime.strptime(user_input_time, "%H:%M")

                # Check if the entered time is before the fixed time
                if user_time_obj < fixed_time_obj:
                    error_message = "Entered time cannot be earlier than the fixed time."
                else:
                    # Calculate the difference
                    time_diff = user_time_obj - fixed_time_obj

                    # Convert the time difference to minutes
                    time_diff_minutes = time_diff.total_seconds() / 60  # convert seconds to minutes

                    # Save the time entry in the database
                    time_entry = TimeEntry(user_name=user_name, user_time=user_time_obj.time(), time_difference=time_diff_minutes)
                    time_entry.save()  # Save to database

            except ValueError:
                error_message = "Invalid time format. Please use HH:mm format."

    # Get all saved entries to display in the template
    #time_entries = TimeEntry.objects.all()  # for unordered view
    time_entries = TimeEntry.objects.all().order_by('time_difference')
    return render(request, "time_diff/time_diff.html", {
        "time_diff": time_diff,
        "time_entries": time_entries,
        "error_message": error_message  # Pass the error message to the template
    })
