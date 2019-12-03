$(document).ready(function() {
    console.log('loaded');

    
    $('#btn_avaliar').click(function() {
        $('#myModal').modal('show');

  
    })
    $('#myModal').on('shown.bs.modal', function () {
        /*
        Funcao responsavel por avaliar a receita
        */
        $.ajax({
            url: URL_AVALIACAO,
            method: 'POST',
            dataType: 'json',
            success: function(response) {

            }
        })  
    })
});