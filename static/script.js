setInterval(() => {
  fetch("/api/feature")
    .then(res => res.json())
    .then(data => {
      const area = document.getElementById("feature-area");
      area.innerHTML = data.showFeature ?
        "<p>🎉 New Feature is Enabled!</p>" :
        "<p>🚧 Feature Coming Soon...</p>";
    });
}, 5000);

