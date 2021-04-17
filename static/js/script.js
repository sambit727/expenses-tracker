
buildGraph()

function buildGraph(xLabelArray, yLabelArray){
    var ctx = document.getElementById('myChart').getContext('2d');

    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xLabelArray,
            datasets: [{
                label: false,
                data: yLabelArray,
                // backgroundColor: [
                //     'rgba(255, 99, 132, 0.2)',
                //     'rgba(54, 162, 235, 0.2)',
                //     'rgba(255, 206, 86, 0.2)',
                //     'rgba(75, 192, 192, 0.2)',
                //     'rgba(153, 102, 255, 0.2)',
                //     'rgba(255, 159, 64, 0.2)'
                // ],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                // borderColor: [
                //     'rgba(255, 99, 132, 1)',
                //     'rgba(54, 162, 235, 1)',
                //     'rgba(255, 206, 86, 1)',
                //     'rgba(75, 192, 192, 1)',
                //     'rgba(153, 102, 255, 1)',
                //     'rgba(255, 159, 64, 1)'
                // ],
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            legend: false,
            scales: {
                yAxes: [{
                    display: true,
                    gridLines: {
                    color: 'gray',
                    },
                    ticks: {
                        beginAtZero: true
                    }
                }],
                xAxes: [{
                    display: true,
                    gridLines: {
                    color: 'gray',
                    tickMarkLength: 0
                    },
                    ticks: {
                        beginAtZero: true,
                        display: false
                    }
                    
                }],

            }
        }
    });
    Chart.defaults.global.defaultFontColor = '#fff';
    Chart.defaults.global.defaultFontFamily = 'Arial';
    Chart.defaults.global.defaultFontSize = 14;
    console.log('Graph Loaded')
}

var activeItem = null
buildList()

function buildList() {
    var wrapper = document.getElementById('entry-wrapper');
    wrapper.innerHTML = ''

    var url = 'http://127.0.0.1:8000/entry-list/'

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){
        console.log('Success:', data)

        var list = data

        var xLabelArray = [];
        var xLabels = data.forEach((i) => {
            xLabelArray.push(i.date)
        })
        xLabelArray.reverse()

        var yLabelArray = [];
        var yLabels = data.forEach((i) => {
            yLabelArray.push(i.amount)
        })
        yLabelArray.reverse()


        buildGraph(xLabelArray, yLabelArray)

        for (var i in list){

            var item = `
                <div class="entries">
                    <p>${list[i].date}</p>
                    <p>${list[i].category}</p>
                    <p>£ ${list[i].amount.toFixed(2)}</p>
                    <a class="edit-btn">Edit</a>
                    <a class="delete-btn">Delete</a>
                </div>
            `
            wrapper.innerHTML += item

        }
        console.log('Successfully loaded all entries')

        for (var i in list){
            var editBtn = document.getElementsByClassName('edit-btn')[i];
            var deleteBtn = document.getElementsByClassName('delete-btn')[i];


            deleteBtn.addEventListener('click', (function(item){
                return function(){
                    deleteItem(item)
                }
            })(list[i]))


            editBtn.addEventListener('click', (function(item){
                return function(){
                    editItem(item)
                }
            })(list[i]))


        }
    })
}

function deleteItem(item){
    console.log('Delete Clicked')
    
    fetch(`http://127.0.0.1:8000/delete-entry/${item.id}/`, {
        method:'DELETE',
        headers:{
            'Content-Type': 'application/json',
        }
    }).then((response) => {
        console.log(response)
        buildList()
        console.log('Entries reloaded after delete')
    })
}

function editItem(item){
    console.log('Item Clicked:', item)
    activeItem = item
    document.getElementById('id_category').value = activeItem.category
    document.getElementById('id_amount').value = activeItem.amount
    }


function submitEntryForm(){
    var submitBtn = document.getElementById('submit-entry-btn').addEventListener("click", (event) => {
        event.preventDefault();
    
        const id_category = document.getElementById('id_category').value;
        const id_amount = document.getElementById('id_amount').value;
    
        const dataForm = new FormData()
    
        dataForm.append('category', id_category);
        dataForm.append('amount', id_amount);
        dataForm.append('csrfmiddlewaretoken', '{{ csrf_token }}');
        console.log(dataForm);
    
        const requestOptions = {
            method: 'POST',
            body: dataForm,
          };
    
          var url = 'http://127.0.0.1:8000/create-entry/'
          
          if(activeItem != null){
              var url = `http://127.0.0.1:8000/edit-entry/${activeItem.id}/`
              activeItem = null
          }
    
          fetch(url, requestOptions)
            .then((response) => {
                response.json()
                buildList()
                // buildGraph()
            })
            .then(data => {
                console.log('Success:', data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        })
    
}

submitEntryForm()

if (window.performance) {
    console.info("window.performance works fine on this browser");
  }
  console.info(performance.navigation.type);
  if (performance.navigation.type == performance.navigation.TYPE_RELOAD) {
    console.info( "This page is reloaded" );
  } else {
    console.info( "This page is not reloaded");
  }