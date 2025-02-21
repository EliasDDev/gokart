// Store date element
let dateElement = document.getElementById('datePicker');

// Set date to a default value.
dateElement.valueAsDate = new Date();
fetchAvailableSlots(dateElement.value);

// Fetch available slots when date changes.
dateElement.addEventListener("change", () => fetchAvailableSlots(dateElement.value));

// Function to fetch available time slots from Django.
function fetchAvailableSlots(dataValue) {
    $.get(`/get-available-slots/?date=${dataValue}`, function (dataValue) {
        let timeSlots = dataValue.slots;
        if (timeSlots.length > 0) {
            let htmlButton = timeSlots.map(time => `<button type="button" class="time-btn" onclick="selectTime('${time}')">${time}</button>`).join("");
            document.getElementById("timeSlots").innerHTML = htmlButton;
        } else {
            document.getElementById("timeSlots").innerHTML = "<p>No available slots</p>";
        }
    });
}

function selectTime(time) {
    // Update selected time.
    document.getElementById("selectedTime").value = time;

    // Highlight selected time slot.
    document.querySelectorAll(".time-btn").forEach(btn => btn.classList.remove("selected"));
    event.target.classList.add("selected");
}