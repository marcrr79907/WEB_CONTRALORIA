document.addEventListener("DOMContentLoaded", function() {

  var orgbtnAceptar = document.getElementById('orgbtnAceptar');

  orgbtnAceptar.addEventListener('click', function() {
    var seleccion = document.getElementById('seleccion').value;
    console.log("Opción seleccionada:", seleccion);

    $('#orgModal').modal('hide');
  });
});

document.addEventListener('DOMContentLoaded', function() {
    var get_id = document.getElementById('orgbtnAceptar');
    get_id.addEventListener('click', function() {
        // Obtener el valor seleccionado del select
        var seleccion = document.getElementById('seleccion').value;

        // Actualizar el valor del campo oculto con el id seleccionado
        document.getElementById('org_seleccion').value = seleccion;

        // Enviar el formulario
        document.getElementById('orgFormulario').submit();
    });
});
