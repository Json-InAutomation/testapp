let pumpIntervals = {};

function cleanPumpAction(pumpNumber) {
  event.preventDefault();

  const startButton = document.getElementById(`start_${pumpNumber}`);
  const stopButton = document.getElementById(`stop_${pumpNumber}`);

  const data = {
    pump_number: pumpNumber,
    action: "clean",
  };

  fetch("/bottle-config/pump/refill", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      const messageContainer = document.querySelector(".message-container");
      const successMessageElement = document.getElementById("success-message");
      const errorMessageElement = document.getElementById("error-message");

      if (data.status === "success") {
        messageContainer.style.display = "block";
        successMessageElement.classList.remove("hidden");
        successMessageElement.classList.add("show-message");
        successMessageElement.innerHTML = data.message;
        startButton.style.display = "none";
        stopButton.style.display = "inline-block";

        // Store interval ID so it can be cleared later
        pumpIntervals[pumpNumber] = setInterval(() => {
          checkPumpStatus(pumpNumber, pumpIntervals[pumpNumber]);
        }, 2000);

        setTimeout(function () {
          messageContainer.style.display = "none";
          successMessageElement.classList.add("hidden");
          successMessageElement.classList.remove("show-message");
        }, 5000);
      } else {
        messageContainer.style.display = "block";
        errorMessageElement.classList.remove("hidden");
        errorMessageElement.classList.add("show-message");
        errorMessageElement.innerHTML = data.message;
        setTimeout(function () {
          errorMessageElement.classList.add("hidden");
          errorMessageElement.classList.remove("show-message");
          messageContainer.style.display = "none";
        }, 5000);
      }
    })
    .catch((error) => console.error("Error:", error));
}


function checkPumpStatus(pumpNumber, intervalId) {
  fetch("/workstatus", {
    method: "GET",
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.percent_done === 100) {
        const successMessageElement =
          document.getElementById("success-message");

        clearInterval(intervalId);

        const startButton = document.getElementById(`start_${pumpNumber}`);
        const stopButton = document.getElementById(`stop_${pumpNumber}`);

        startButton.style.display = "inline-block";
        stopButton.style.display = "none";

        successMessageElement.classList.remove("hidden");
        successMessageElement.classList.add("show-message");
        successMessageElement.innerHTML = `${pumpNumber} re-fill process completed.`;

        setTimeout(function () {
          successMessageElement.classList.add("hidden");
          successMessageElement.classList.remove("show-message");
        }, 5000);
      }
    })
    .catch((error) => console.error("Error:", error));
}

function cancelPumpAction(pumpNumber) {
  event.preventDefault();

  const startButton = document.getElementById(`start_${pumpNumber}`);
  const stopButton = document.getElementById(`stop_${pumpNumber}`);

  const data = {
    pump_number: pumpNumber,
    action: "cancel",
  };

  fetch("/bottle-config/pump/refill", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      const messageContainer = document.querySelector(".message-container");
      const errorMessageElement = document.getElementById("error-message");

      if (data.status === "success") {
        clearInterval(pumpIntervals[pumpNumber]);

        startButton.style.display = "inline-block";
        stopButton.style.display = "none";
        messageContainer.style.display = "block";
        errorMessageElement.classList.remove("hidden");
        errorMessageElement.classList.add("show-message");
        errorMessageElement.innerHTML = data.message;

        setTimeout(function () {
          messageContainer.style.display = "none";
          errorMessageElement.classList.add("hidden");
          errorMessageElement.classList.remove("show-message");
        }, 5000);
      }
    })
    .catch((error) => console.error("Error:", error));
}
