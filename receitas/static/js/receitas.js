$(document).ready(function() {

    $('btn_avaliar').click(function() {
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