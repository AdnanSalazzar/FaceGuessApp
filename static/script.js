/* const form = document.querySelector(".box");
const fileInput = form.querySelector(".box__file");
const uploadMessage = form.querySelector(".box__uploading");
const successMessage = form.querySelector(".box__success");
const errorMessage = form.querySelector(".box__error");

form.addEventListener("dragover", (e) => {
  e.preventDefault();
  form.classList.add("box--dragging");
});

form.addEventListener("dragleave", () => {
  form.classList.remove("box--dragging");
});

fileInput.addEventListener("change", () => {
  uploadMessage.style.display = "block";
  successMessage.style.display = "none";
  errorMessage.style.display = "none";
});

form.addEventListener("submit", (e) => {
  e.preventDefault();
  uploadMessage.style.display = "block";
  successMessage.style.display = "none";
  errorMessage.style.display = "none";

  // Simulate upload for demo
  setTimeout(() => {
    uploadMessage.style.display = "none";
    successMessage.style.display = "block";
  }, 2000);
});
 */