// Función para mostrar las sublistas en la tabla
function displaySublistInTable(listOfLists) {
    const tableBody = document.querySelector("#process-table tbody");
    tableBody.innerHTML = "";  // Limpiar contenido previo de la tabla

    // Recorrer cada sublista y crear una nueva fila para cada una
    listOfLists.forEach(sublist => {
        const row = document.createElement("tr");

        const maximizeCell = document.createElement("td");
        const minimizeCell = document.createElement("td");

        // Mostrar el contenido de la sublista en ambas columnas
        maximizeCell.textContent = sublist.join(", ");
        minimizeCell.textContent = sublist.join(", ");

        row.appendChild(maximizeCell);
        row.appendChild(minimizeCell);

        // Añadir la fila a la tabla
        tableBody.appendChild(row);
    });
}

// Esta función genera datos o los recibe de algún lugar
function generatePopulationAndDisplay() {
    const dynamicData = [
        [Math.floor(Math.random() * 10), Math.floor(Math.random() * 10), Math.floor(Math.random() * 10)],
        [Math.floor(Math.random() * 10), Math.floor(Math.random() * 10), Math.floor(Math.random() * 10)],
        [Math.floor(Math.random() * 10), Math.floor(Math.random() * 10), Math.floor(Math.random() * 10)]
    ];

    // Llama a la función para mostrar la población generada dinámicamente
    displaySublistInTable(dynamicData);
}

// Asignar el evento al botón "INICIAR"
document.getElementById("start").addEventListener("click", function() {
    // Llamar a la función que genera la población y la muestra
    generatePopulationAndDisplay();
});
