// Función para mostrar las sublistas en la tabla
function displaySublistInTable(maximizeList, maximizeFitness, minimizeList, minimizeFitness) {
  const tableBody = document.querySelector("#process-table tbody");
  tableBody.innerHTML = "";  // Limpiar contenido previo de la tabla

  for (let i = 0; i < maximizeList.length; i++) {
    const row = document.createElement("tr");

    const genCell = document.createElement("td");
    const maxCell = document.createElement("td");
    const minCell = document.createElement("td");
    const maxFitnessCell = document.createElement("td");
    const minFitnessCell = document.createElement("td");

    const maxPre = document.createElement("pre");
    const minPre = document.createElement("pre");
    const minFitPre = document.createElement("pre");
    const maxFitPre = document.createElement("pre");

    let maxGen = "";
    let minGen = "";
    let maxFit = "";
    let minFit = "";

    maximizeList[i].forEach(sublist => {
      maxGen += "[" + sublist.join(", ") + "]\n";
    });

    minimizeList[i].forEach(sublist => {
      minGen += "[" + sublist.join(", ") + "]\n";
    });

    maximizeFitness[i].forEach(sublist => {
        maxFit += sublist + "\n";
    });

    minimizeFitness[i].forEach(sublist => {
        minFit += sublist + "\n";
    });

    maxPre.textContent = maxGen;
    minPre.textContent = minGen;
    maxFitPre.textContent = maxFit;
    minFitPre.textContent = minFit;

    genCell.textContent = i;
    maxCell.appendChild(maxPre);
    minCell.appendChild(minPre);
    maxFitnessCell.appendChild(maxFitPre);
    minFitnessCell.appendChild(minFitPre);

    row.appendChild(genCell);
    row.appendChild(maxCell);
    row.appendChild(maxFitnessCell);
    row.appendChild(minCell);
    row.appendChild(minFitnessCell);

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
      const maxFitness = data['data']['maximize_fitness'];
      const minData = data['data']['minimize'];
      const minFitness = data['data']['minimize_fitness'];
      displaySublistInTable(maxData, maxFitness, minData, minFitness);
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
