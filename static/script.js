function validateForm() {
    const input = document.getElementById("prompt");
    if (!input.value.trim()) {
      input.setCustomValidity("Please describe your use case before submitting.");
      return false;
    }
    return true;
  }
// Show/hide context field based on use case
document.addEventListener("DOMContentLoaded", function () {
  const useCaseSelect = document.getElementById("use_case");
  const contextBlock = document.getElementById("context-block");

  function toggleContextField() {
    const selected = useCaseSelect.value;
    if (selected === "Bug Report" || selected === "Release Notes") {
      contextBlock.style.display = "block";
    } else {
      contextBlock.style.display = "none";
    }
  }

  useCaseSelect.addEventListener("change", toggleContextField);
  toggleContextField(); // initial load
});

// Copy to clipboard function
function copyToClipboard() {
  const content = document.getElementById("formatted-output").innerText;
  navigator.clipboard.writeText(content).then(() => {
    alert("✅ Output copied to clipboard!");
  });
}


 document.querySelectorAll("form[action='/export']").forEach(form => {
      form.addEventListener("submit", function () {
        document.getElementById("export-text").value = document.getElementById("formatted-output").value;
      });
    });