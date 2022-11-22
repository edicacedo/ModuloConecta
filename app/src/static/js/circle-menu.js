
        $(function() {
            $('.map').maphilight();
        });    
        
        $.fn.maphilight.defaults = {
            fill: true,
            fillColor: '000000',
            fillOpacity: 0.3,
            stroke: false,
            strokeColor: 'ff0000',
            strokeOpacity: 10,
            strokeWidth: 3,
            fade: true,
            alwaysOn: false,
            neverOn: false,
            groupBy: false,
            wrapClass: true,
            shadow: true,
            shadowX: 0,
            shadowY: 0,
            shadowRadius: 20,
            shadowColor: '4e8bed',
            shadowOpacity: 0.8,
            shadowPosition: 'outside',
            shadowFrom: false
        }    