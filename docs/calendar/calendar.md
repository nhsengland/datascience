<!DOCTYPE html>
<html>
  <head>
    <script src='https://cdn.jsdelivr.net/npm/fullcalendar/index.global.min.js'></script>
    <link href='https://cdn.jsdelivr.net/npm/fullcalendar/main.min.css' rel='stylesheet' />
    <script>
      document.addEventListener('DOMContentLoaded', function() {
        const calendarEl = document.getElementById('calendar');

        fetch('events.json')
          .then(response => {
            if (!response.ok) {
              throw new Error('Failed to fetch events');
            }
            return response.json();
          })
          .then(data => {
            const calendar = new FullCalendar.Calendar(calendarEl, {
              initialView: 'dayGridMonth',
              events: data,
              eventTimeFormat: {
                hour: 'numeric',
                minute: '2-digit',
                meridiem: 'short', // Use 'short' to display 'am/pm'
                hour12: true // Use 12-hour format
              },
              eventMouseEnter: function(info) {
                const tooltip = document.createElement('div');
                tooltip.classList.add('tooltip');
                tooltip.textContent = info.event.extendedProps.description;
                document.body.appendChild(tooltip);
                tooltip.style.top = info.jsEvent.clientY + 10 + 'px';
                tooltip.style.left = info.jsEvent.clientX + 10 + 'px';
                info.el.addEventListener('mouseleave', function() {
                  tooltip.remove();
                });
              },
              eventClick: function(info) {
                if (info.event.extendedProps.teamsLink) {
                  window.open(info.event.extendedProps.teamsLink, '_blank');
                } else {
                  alert('Teams link not available for this event');
                }
              }
            });
            calendar.render();
          })
          .catch(error => console.error('Error fetching or parsing events:', error));
      });
    </script>
    <style>
      .tooltip {
        position: absolute;
        z-index: 1000;
        background-color: #fff;
        border: 1px solid #ccc;
        padding: 5px;
        border-radius: 3px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
      }
    </style>
  </head>
  <body>
    <div id='calendar'></div>
  </body>
</html>
