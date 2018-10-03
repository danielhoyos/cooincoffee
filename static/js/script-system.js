/* 
===========================
|          INDICE         | 
===========================
| 1. Funciones generales  |
| 2. Facturación          |
| 3. Reportes             |
| 4. Window.load          |
|_________________________|
*/
// 1. Funciones Generales
let fNumber = {
    formatear : function (num){
        return new Intl.NumberFormat().format(num);
    },
    go : function(num, simbol){
        this.simbol = simbol ||'';
        return this.simbol + this.formatear(num);
    }
}
let reporte = null;

// 2. Facturación
function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+-)');
    var replacement = prefix + '-' + ndx + '-';
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}
function deleteForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
        (formCount <= 10) ? $("#add").show() : $("#add").hide();
        (formCount > 2) ? $('.delete').show() : $('.delete').hide();

        if (formCount > 1) {
            // Delete the item/form
            $(btn).parents('.detalle').remove();

            var forms = $('.detalle'); // Get all the forms

            // Update the total number of forms (1 less than before)
            $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);

            var i = 0;
            // Go through the forms and set their indices, names and IDs
            for (formCount = forms.length; i < formCount; i++) {
                $(forms.get(i)).find(':input').each(function() {
                    updateElementIndex(this, prefix, i);
                });
            }
        }
    return false;
}
function addForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    (formCount < 9) ? $("#add").show() : $("#add").hide();
    (formCount > 0) ? $(".delete").show() : $(".delete").hide();

    if (formCount < 10) {
      // Clone a form (without event handlers) from the first form
      var row = $(".detalle:last").clone(false).get(0);
      // Insert it after the last form
      $(row).removeAttr('id').insertAfter(".detalle:last");
      // Remove the bits we don't want in the new row/form
      // e.g. error messages
      $(".errorlist", row).remove();
      $(row).children().removeClass('error');
      
      // Relabel/rename all the relevant bits 
        $(".detalle:last :input").each(function() {
            updateElementIndex(this, prefix, formCount);
            if ( $(this).attr('type') == 'number' ) $(this).val('');
        });
      
      // Add an event handler for the delete item/form link 
      $(row).find('.delete').click(function() {
        return deleteForm(this, prefix);
      });

      // Update the total form count
      $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1); 

    }
    return false;
}
function codigoFactura(codigo){
    $.ajax({
        data : { 'codigo' : codigo },
        url : 'facturacion/codigo/',
        type : 'json',
        method : 'GET',
        success : function (data) {
            (data.length == 0) ? $("#btn-registar-factura").removeAttr('disabled') : $("#btn-registar-factura").attr('disabled', 'disabled');
        }
    });
}

// 3. Reportes
function request_graphics_report(data, ctx){
    $.ajax({
        method: 'GET',
        url: '../reporte_data/',
        data : data,
        success: function(data_report){
            show_report(data_report, ctx)
        }
    });
}

function request_cooperativa_report(data, ctx){
    $.ajax({
        method: 'GET',
        url: '../reporte_cooperativas/',
        data : data,
        success: function(data_report){
            let html = '';

            for (let index = 0; index < data_report.cooperativas.length; index++) {
                html += `<tr>
                            <td>${data_report.cooperativas[index].cooperativa}</td>
                            <td>${fNumber.go(data_report.cooperativas[index].total, '$ ')}</td>
                        </tr>`;
            }

            html += `<tr>
                        <td></td>
                        <td class="font-weight-bold">TOTAL: ${fNumber.go(data_report.total, '$ ')}</td>
                    </tr>`;

            let table = document.getElementById(ctx);
            let year_cooperativa_report = document.getElementById('year-cooperativa-report');
            
            table.innerHTML = html;
            year_cooperativa_report.innerHTML = data_report.year;
        }
    });
}

function request_tipos_report(data, ctx){
    $.ajax({
        method: 'GET',
        url: '../reporte_tipos/',
        data : data,
        success: function(data_report){
            let html = '';

            for (let index = 0; index < data_report.ventas.length; index++) {
                html += `<tr>
                            <td>${data_report.ventas[index].tipo_cafe}</td>
                            <td>${fNumber.go(data_report.ventas[index].total, '$ ')}</td>
                        </tr>`;
            }

            html += `<tr>
                        <td></td>
                        <td class="font-weight-bold">TOTAL: ${fNumber.go(data_report.total, '$ ')}</td>
                    </tr>`;

            let table = document.getElementById(ctx);
            let year_tipos_report = document.getElementById('year-tipos-report');
            
            table.innerHTML = html;
            year_tipos_report.innerHTML = data_report.year;
        }
    });
}

function request_kilos_report(data, ctx){
    $.ajax({
        method: 'GET',
        url: '../reporte_kilos/',
        data : data,
        success: function(data_report){
            let html = '';

            for (let index = 0; index < data_report.kilos.length; index++) {
                html += `<tr>
                            <td>${data_report.kilos[index].tipo_cafe}</td>
                            <td>${data_report.kilos[index].total}</td>
                        </tr>`;
            }

            html += `<tr>
                        <td></td>
                        <td class="font-weight-bold">TOTAL: ${data_report.total}</td>
                    </tr>`;

            let table = document.getElementById(ctx);
            let year_kilos_report = document.getElementById('year-kilos-report');
            
            table.innerHTML = html;
            year_kilos_report.innerHTML = data_report.year;
        }
    });
}

function show_report(data_report, id){
    if (reporte != null){
        reporte.destroy();
    }

    let ctx = document.getElementById(id).getContext('2d');
    reporte = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: data_report.labels,
            datasets: [
                {
                    label: 'TOTAL: ' + fNumber.go(data_report.total, "$ "),
                    data: data_report.data,
                    backgroundColor: 'rgba(200, 0, 0, 0.5)',
                    borderColor: 'rgba(255, 0, 0, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            title: {
                display: true,
                text: data_report.title
            },
            scales: {
                xAxes: [{
                    ticks: {
                        beginAtZero : true,
                        callback: function(value) {
                            return fNumber.go(value, "$ ");
                        }
                    }
                }]
            },
            tooltips: {
                callbacks : {
                    label : function(tooltipItem){
                        label = `Total: ${fNumber.go(tooltipItem.xLabel, "$ ")}`;

                        return label;
                    }
                }
            } 
        }
    });
}

// 4. Window.load
$(document).ready(function() {
    // Facturación
    $(".delete").hide();

    $("#add").click(function() {
        return addForm(this, 'form');
    });

    $(".delete").click(function() {
        return deleteForm(this, 'form');
    });

    $("#codigo-factura").keyup(function(){
        ($("#codigo-factura").val().length > 3) ? codigoFactura($("#codigo-factura").val()) : $("#btn-registar-factura").attr('disabled', 'disabled');
    })

    // Buscadores
    $("#tabla-facturas, #tabla-cooperativas, #tabla-asociados, #tabla-tipos-cafe").DataTable({
        "language": {
            "decimal": ",",
            "thousands": ".",
            "info": "",
            "infoEmpty": "",
            "infoPostFix": "",
            "infoFiltered": "(filtrado de un total de _MAX_ registros)",
            "loadingRecords": "Cargando...",
            "lengthMenu": "Mostrar _MENU_ registros",
            "paginate": {
                "first": "Primero",
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            },
            "processing": "Procesando...",
            "search": "Buscar:",
            "searchPlaceholder": "",
            "zeroRecords": "No se encontraron resultados",
            "emptyTable": "Ningún dato disponible en esta tabla",
            "aria": {
                "sortAscending":  ": Activar para ordenar la columna de manera ascendente",
                "sortDescending": ": Activar para ordenar la columna de manera descendente"
            },
            //only works for built-in buttons, not for custom buttons
            "buttons": {
                "create": "Nuevo",
                "edit": "Cambiar",
                "remove": "Borrar",
                "copy": "Copiar",
                "csv": "fichero CSV",
                "excel": "tabla Excel",
                "pdf": "documento PDF",
                "print": "Imprimir",
                "colvis": "Visibilidad columnas",
                "collection": "Colección",
                "upload": "Seleccione fichero...."
            },
            "select": {
                "rows": {
                    _: '%d filas seleccionadas',
                    0: 'clic fila para seleccionar',
                    1: 'una fila seleccionada'
                }
            }
        },
        buttons: {
            buttons: [
                { extend: 'copy', className: 'copyButton' },
                { extend: 'excel', className: 'excelButton' }
            ]
        }     
    });
    // Fin Buscadores

    // Reportes
    $('#btn-graphics-report').click(function(e){
        e.preventDefault();

        let cooperativa = $("#cooperativa-graphics").val() !== '' ? $("#cooperativa").val() : undefined;
        let asociado    = $("#asociado-graphics").val() !== '' ? $("#asociado").val() : undefined;
        let year        = $("#year-graphics").val() !== '' ? $("#year-graphics").val() : undefined;

        let data = {
            'cooperativa' : cooperativa,
            'asociado' : asociado,
            'year' : year
        }

        // Llamado a la función del reporte
        request_graphics_report(data, 'graphics-report');
    });

    $("#btn-report-cooperativa").click(function(e){
        let year = $("#year-cooperativa").val() !== '' ? $("#year-cooperativa").val() : undefined;
        let data = {
            'year' : year
        }

        e.preventDefault();
        request_cooperativa_report(data, 'tbody-cooperativas');
    });

    $("#btn-report-kilos").click(function(e){
        let year = $("#year-kilos").val() !== '' ? $("#year-kilos").val() : undefined;
        let data = {
            'year' : year
        }

        e.preventDefault();
        request_kilos_report(data, 'tbody-kilos');
    });

    $("#btn-report-tipos").click(function(e){
        let year = $("#year-tipos").val() !== '' ? $("#year-tipos").val() : undefined;
        let data = {
            'year' : year
        }

        e.preventDefault();
        request_tipos_report(data, 'tbody-tipos');
    });
});