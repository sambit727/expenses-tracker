var ctx = document.getElementById('myChart').getContext('2d');
// const x_label = [1,2,3,4,5,6,7];
// const x_label = {{ x_labels|safe }};
// console.log(x_label);
// // const y_label = [35.60, 35.90, 159.99, 46, 23];
// const y_label = {{ y_labels|safe }}
// console.log(y_label);
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: x_label,
        datasets: [{
            label: false,
            data: y_label,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend: false,
        scales: {
            yAxes: [{
                display: true,
                gridLines: {
                color: 'gray'
                },
                ticks: {
                    beginAtZero: true
                }
            }],
            xAxes: [{
                display: true,
                gridLines: {
                color: 'gray'
                },
                ticks: {
                    beginAtZero: true
                }
            }],

        }
    }
});
Chart.defaults.global.defaultFontColor = '#fff';
Chart.defaults.global.defaultFontFamily = 'Arial';
Chart.defaults.global.defaultFontSize = 14;

var submitBtn = document.getElementById('submit-entry-btn').addEventListener("click", (event) => {
    event.preventDefault();

    const id_category = document.getElementById('id_category').value;
    const id_amount = document.getElementById('id_amount').value;

    const dataForm = new FormData()
    // var entryForm = document.getElementsByClassName("entry-form")
    // var formData = JSON.stringify($("#entry-form").serializeArray());
    
    dataForm.append('category', id_category);
    dataForm.append('amount', id_amount);
    dataForm.append('csrfmiddlewaretoken', '{{ csrf_token }}');

    const requestOptions = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: dataForm,
      };
      fetch('/', requestOptions)
        // .then((response) => response.json())
        // .then((data) => console.log(data));
        .then((result) => console.log('Success:', result));
})
