// Función para mostrar las sublistas en la tabla
function displaySublistInTable(maximizeList, minimizeList) {
  const tableBody = document.querySelector("#process-table tbody");
  tableBody.innerHTML = "";  // Limpiar contenido previo de la tabla

  for (let i = 0; i < maximizeList.length; i++) {
    const row = document.createElement("tr");

    const genCell = document.createElement("td");
    const maxCell = document.createElement("td");
    const minCell = document.createElement("td");

    const maxPre = document.createElement("pre");
    const minPre = document.createElement("pre");

    let maxGen = "";
    let minGen = "";

    maximizeList[i].forEach(sublist => {
      maxGen += "[" + sublist.join(", ") + "]\n";
    });

    minimizeList[i].forEach(sublist => {
      minGen += "[" + sublist.join(", ") + "]\n";
    });

    maxPre.textContent = maxGen;
    minPre.textContent = minGen;

    genCell.textContent = i;
    maxCell.appendChild(maxPre);
    minCell.appendChild(minPre);

    row.appendChild(genCell);
    row.appendChild(maxCell);
    row.appendChild(minCell);

    tableBody.appendChild(row)
  }
}

// Función para generar la población y mostrarla
function generatePopulationAndDisplay() {
  // Obtener el número seleccionado del input
  const selectedNumber = document.getElementById("number-input").value;

  // Usar el número seleccionado en la URL de fetch
  fetch(`http://localhost:8000/api/get-result/${selectedNumber}`)
    .then(response => response.json())
    .then(data => {
      const maxData = data['data']['maximize'];
      const minData = data['data']['minimize'];
      displaySublistInTable(maxData, minData);
    })
    .catch(error => { console.error('Error: ', error); });
}

// Asignar el evento al botón "INICIAR"
document.getElementById("start").addEventListener("click", function () {
  // Llamar a la función que genera la población y la muestra
  generatePopulationAndDisplay();
});

document.getElementById("generate-population").addEventListener("click", function () {
  fetch('http://localhost:8000/api/get-population')
    .then(response => response.json())
    .then(data => {
      let textArea = document.getElementById("population-text");
      let generation = data['data']['population'];
      let text = ""
      generation.forEach(sublist => {
        text += "[" + sublist.join(", ") + "]\n";
      });

      textArea.textContent = text;
    })
    .catch(error => { console.error('Error: ', error); });
});
