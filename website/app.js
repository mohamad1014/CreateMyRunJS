function displayRouteUrls() {
    var container = document.getElementById('routeUrlsContent');
    container.innerHTML = ''; // Clear previous content
    routeUrls.forEach(function(route) {
        var link = document.createElement('a');
        link.href = route.url;
        link.textContent = route.color;
        link.target = '_blank'; // Open link in a new tab
        link.style.display = 'block'; // Display each link on a new line
        link.style.color = route.color.toLowerCase(); // Set the text color to match the color name
        link.style.textDecoration = 'underline'; // Underline the link
        container.appendChild(link);
    });
}