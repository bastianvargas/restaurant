// Chart.defaults.global.elements.rectangle.backgroundColor = '#FF0000';

var bar_ctx = document.getElementById('bar-chart').getContext('2d');

var purple_orange_gradient = bar_ctx.createLinearGradient(0, 0, 0, 600);
purple_orange_gradient.addColorStop(0, 'orange');
purple_orange_gradient.addColorStop(1, 'purple');

var bar_chart = new Chart(bar_ctx, {
    type: 'bar',
    data: {
        labels: fecha,
        datasets: [{
            label: '$',
            data: total,
						backgroundColor: purple_orange_gradient,
						hoverBackgroundColor: purple_orange_gradient,
						hoverBorderWidth: 2,
						hoverBorderColor: 'purple'
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});
