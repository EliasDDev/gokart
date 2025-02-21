let selectedTime = null; // Store selected time

// Fetch available slots when date changes
document.getElementById("datePicker").addEventListener("change", function () {
    fetchAvailableSlots(this.value);
});

// Function to Fetch Available Time Slots from Django
function fetchAvailableSlots(date) {
    $.get(`/get-available-slots/?date=${date}`, function (data) {
        let times = data.slots;
        let html = times.length > 0
            ? times.map(time => `<button type="button" class="time-btn" onclick="selectTime('${time}')">${time}</button>`).join("")
            : "<p>No available slots</p>";

        document.getElementById("timeSlots").innerHTML = html;
    });
}

function selectTime(time) {
    selectedTime = time; // Store selected time
    document.getElementById("selectedTime").value = time; // Update hidden input

    // Highlight selected button
    document.querySelectorAll(".time-btn").forEach(btn => btn.classList.remove("selected"));
    event.target.classList.add("selected");
}