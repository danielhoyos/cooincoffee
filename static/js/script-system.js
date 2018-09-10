$(document).ready(function() {
    // Factura
    function updateElementIndex(el, prefix, ndx) {
        var id_regex = new RegExp('(' + prefix + '-\\d+-)');
        var replacement = prefix + '-' + ndx + '-';
        if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex,
     replacement));
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
                    $(forms.get(i)).children().children().each(function() {
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
          var row = $(".detalle:first").clone(false).get(0);
          // Insert it after the last form
          $(row).removeAttr('id').insertAfter(".detalle:last");
          // Remove the bits we don't want in the new row/form
          // e.g. error messages
          $(".errorlist", row).remove();
          $(row).children().removeClass('error');
          
          // Relabel/rename all the relevant bits
          $(row).children().children().each(function() {
            updateElementIndex(this, prefix, formCount);
            if ( $(this).attr('type') == 'text' )
              $(this).val('');
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

    $(".delete").hide();

    $("#add").click(function() {
        return addForm(this, 'form');
    });

    $(".delete").click(function() {
        return deleteForm(this, 'form');
    });

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

    $("#codigo-factura").keyup(function(){
        ($("#codigo-factura").val().length > 3) ? codigoFactura($("#codigo-factura").val()) : $("#btn-registar-factura").attr('disabled', 'disabled');
    })

    
    // Fin Factura
});