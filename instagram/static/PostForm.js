const input = document.querySelector(".ig-file");

const profile = document.querySelector(".avatar");
input.parentNode.insertBefore(profile, input);

const preview = document.querySelector(".avatar img");

input.addEventListener("change", (e) => {
  const file = e.target.files[0];

  if (!file) return;

  preview.src = URL.createObjectURL(file);
});
