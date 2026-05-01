let pumpIntervals = {};

intervalId = setInterval(async () => {
  try {
    const irSensorResponse = await fetch("/ir-sensor-detection");
    const data = await irSensorResponse.json();

    const buttons = document.querySelectorAll(".btn-start-action");

    if (["/inventory"].includes(window.location.pathname)) {
      const errorMessageElement = document.getElementById("error-message");
      if (data.sensor_results == 0) {
        buttons.forEach((button) => {
          button.disabled = true;
          button.style.setProperty("background-color", "#5EBD74", "important");
          button.style.cursor = "not-allowed";
          document.querySelector(".message-container").style.display = "block";
          errorMessageElement.classList.remove("hidden");
          errorMessageElement.innerHTML =
            "Please make sure you have placed the mixer.";
        });
      } else {
        buttons.forEach((button) => {
          button.disabled = false;
          button.style.cursor = "Pointer";
          document.querySelector(".message-container").style.display = "none";
          button.style.setProperty("background-color", "#28a745", "important");
          errorMessageElement.classList.add("hidden");
        });
      }
    }
  } catch (error) {
    console.error("Error checking IR sensor:", error);
  }
}, 500);

function cleanPumpAction(pumpNumber) {
  event.preventDefault();
  const startButton = document.getElementById(`start_${pumpNumber}`);
  const stopButton = document.getElementById(`stop_${pumpNumber}`);
  const data = {
    pump_number: pumpNumber,
    action: "clean",
  };

  fetch("/inventory/pump/refill", {
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

      const showMessage = (element, message) => {
        messageContainer.style.display = "block";
        element.classList.remove("hidden");
        element.classList.add("show-message");
        element.innerHTML = message;
      };

      const hideMessages = () => {
        messageContainer.style.display = "none";
        [successMessageElement, errorMessageElement].forEach((element) => {
          element.classList.add("hidden");
          element.classList.remove("show-message");
        });
      };

      if (data.status === "success") {
        showMessage(successMessageElement, data.message);
        startButton.style.display = "none";
        stopButton.style.display = "inline-block";

        // Store interval ID so it can be cleared later
        pumpIntervals[pumpNumber] = setInterval(() => {
          checkPumpStatus(pumpNumber, pumpIntervals[pumpNumber]);
        }, 3000);

        setTimeout(hideMessages, 4000);
      } else {
        showMessage(errorMessageElement, data.message);
        setTimeout(hideMessages, 4000);
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

  fetch("/inventory/pump/refill", {
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

function OpenAdjustModal(pump_number, qty, event) {
  event.preventDefault();

  const selectedQuantity = document.getElementById("selected_qty");
  const adjustModal = document.getElementById("AdjustQuantityModal");
  const submitBtn = document.getElementById("submitAdjustVolumeBtn");

  adjustModal.style.display = "block";

  selectedQuantity.innerText = qty;

  submitBtn.onclick = null;

  document.querySelectorAll(".option").forEach((option) => {
    option.onclick = function () {
      const value = this.getAttribute("data-value");
      selectedQuantity.innerText = value;
    };
  });

  submitBtn.onclick = function (e) {
    e.preventDefault();

    const payloadData = {
      pump_number: pump_number,
      quantity: selectedQuantity.innerText,
    };

    console.log(payloadData);

    fetch("/inventory/settings/quantity", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payloadData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        adjustModal.style.display = "none";
        window.location = "/inventory";
      })
      .catch((error) => console.error("Error:", error));
  };
}

function closeAdjustModal() {
  const adjustModal = document.getElementById("AdjustQuantityModal");
  adjustModal.style.display = "none";
}
