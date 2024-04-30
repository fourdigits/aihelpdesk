export function copyCitation() {
  const myInput = document.getElementById("citation-field");
  if (!myInput) {
    return;
  }

  myInput.addEventListener("click", () => {
    const text = myInput.textContent || myInput.innerText;
    navigator.clipboard.writeText(text);

    const tooltip = document.getElementById("citation-tooltip");
    tooltip.innerHTML = "Copied: " + text;
  });
}

export function resetToolTip() {
  const myInput = document.getElementById("citation-field");
  if (!myInput) {
    return;
  }

  myInput.addEventListener("mouseleave", () => {
    const tooltip = document.getElementById("citation-tooltip");
    tooltip.innerHTML = "Copy to clipboard";
  });
}
