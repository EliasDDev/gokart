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

document.addEventListener("DOMContentLoaded", function () {
    // Function to update the number of gokart selections based on the selected number of drivers.
    function updateGokartSelections() {
        // Fetch gokarts via AJAX (using jQuery)
        $.get("/get-gokarts/", function (dataValue) {
            var numPeople = document.getElementById("numPeople").value;
            var gokartContainer = document.getElementById("gokartContainer");

            // Clear existing selections
            gokartContainer.innerHTML = "";

            // Add new gokart selection inputs
            for (var i = 1; i <= numPeople; i++) {
                var div = document.createElement("div");
                div.classList.add("gokart-selection");

                var selectHTML = `
                    <label for="gokart_id_${i}">Förare ${i}:</label><br>
                    <select name="gokart_id_${i}" required>
                        <option value="" disabled selected>Välj en gokart.</option>
                `;

                // Loop through the received gokarts data and add options dynamically.
                dataValue.forEach(function(gokart) {
                    selectHTML += `<option value="${gokart.id}">${gokart.name}</option>`;
                });

                selectHTML += `</select>`;
                div.innerHTML = selectHTML;

                // Append the new selection to the container
                gokartContainer.appendChild(div);
            }
        });
    }

    updateGokartSelections();
    // Attach the onchange event listener to the number of people input field
    document.getElementById("numPeople").addEventListener("change", updateGokartSelections);
});