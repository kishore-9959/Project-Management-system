document.addEventListener("DOMContentLoaded", function() {
    if (typeof ganttTasks !== "undefined") {
        var ganttData = ganttTasks.map(function(task) {
            return {
                x: task.task,
                y: [
                    new Date(task.start).getTime(),
                    new Date(task.end).getTime()
                ],
                fillColor: task.color
            };
        });

        var options = {
            chart: {
                height: 600,
                type: 'rangeBar',
                toolbar: {
                    show: true
                },
                // 🛑 Disable interactions
                events: {
                    dataPointSelection: function(event, chartContext, config) {
                        event.preventDefault();
                    }
                }
            },
            plotOptions: {
                bar: {
                    horizontal: true,
                    distributed: true,
                    dataLabels: {
                        hideOverflowingLabels: false
                    },
                    // 🔒 Disable drag and drop behavior
                    rangeBarGroupRows: false
                }
            },
            xaxis: {
                type: 'datetime'
            },
            series: [{
                data: ganttData
            }],
            tooltip: {
                x: {
                    format: 'yyyy-MM-dd'
                }
            }
        };

        var chart = new ApexCharts(document.querySelector("#timelineChart"), options);
        chart.render();
    }
});


// document.addEventListener("DOMContentLoaded", function() {
//     var ganttTasks = JSON.parse(document.getElementById('gantt-data').textContent);

//     if (typeof ganttTasks !== "undefined") {
//         var ganttData = ganttTasks.map(function(task) {
//             return {
//                 x: task.task,
//                 y: [
//                     new Date(task.start).getTime(),
//                     new Date(task.end).getTime()
//                 ],
//                 fillColor: task.color
//             };
//         });

//         var options = {
//             chart: {
//                 height: 600,
//                 type: 'rangeBar',
//                 toolbar: { show: true },
//                 events: {
//                     dataPointSelection: function(event, chartContext, config) {
//                         event.preventDefault();
//                     }
//                 }
//             },
//             plotOptions: {
//                 bar: {
//                     horizontal: true,
//                     distributed: true,
//                     dataLabels: {
//                         hideOverflowingLabels: false
//                     }
//                 }
//             },
//             dataLabels: {
//                 enabled: false
//             },
//             xaxis: {
//                 type: 'datetime',
//                 labels: {
//                     format: 'yyyy-MM-dd'
//                 }
//             },
//             yaxis: {
//                 labels: {
//                     style: {
//                         colors: '#000000',
//                         fontSize: '14px'
//                     }
//                 }
//             },
//             series: [{
//                 data: ganttData
//             }],
//             tooltip: {
//                 x: {
//                     format: 'yyyy-MM-dd'
//                 }
//             },
//             grid: {
//                 borderColor: '#d3d3d3', 
//                 strokeDashArray: 2
//             },
//             colors: ganttData.map(task => task.fillColor),
//         };

//         var chart = new ApexCharts(document.querySelector("#timelineChart"), options);
//         chart.render();
//     }
// });


// const tasks = JSON.parse('{{ tasks|escapejs }}');

//         const taskListElement = document.getElementById('task-list');
        
//         tasks.forEach(task => {
//             const taskDiv = document.createElement('div');
//             taskDiv.classList.add('task');
//             taskDiv.style.borderLeftColor = task.color;

//             const taskTitle = document.createElement('h4');
//             taskTitle.innerText = task.task;
//             taskDiv.appendChild(taskTitle);

//             const taskDates = document.createElement('p');
//             taskDates.innerText = `Start: ${task.start} | End: ${task.end}`;
//             taskDiv.appendChild(taskDates);

//             taskListElement.appendChild(taskDiv);
//         });


const tasks = JSON.parse('{{ tasks|safe|escapejs }}');

const taskListElement = document.getElementById('task-list');

tasks.forEach(task => {
    const taskDiv = document.createElement('div');
    taskDiv.classList.add('task');
    taskDiv.style.borderLeftColor = task.color;

    const title = document.createElement('h3');
    title.innerText = task.task;
    taskDiv.appendChild(title);

    const dates = document.createElement('p');
    dates.innerText = `Start: ${task.start} | End: ${task.end}`;
    taskDiv.appendChild(dates);

    taskListElement.appendChild(taskDiv);
});