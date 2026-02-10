$(function(){
    $('#firstBtn').click(function(){
        $('li').css('background-color', 'lightblue')
        $('li:first').css('background-color', 'green')

    })
    $('#lastBtn').click(function(){
        $('li').css('background-color', 'lightblue')
        $('li:last').css('background-color', 'red')

    })
    $('#evenBtn').click(function(){
        $('li').css('background-color', 'lightblue')
        $('li:even').css('background-color', 'red')

    })
    $('#oddBtn').click(function(){
        $('li').css('background-color', 'lightblue')
        $('li:odd').css('background-color', 'red')

    })
    $('#eqBtn').click(function(){
        $('li').css('background-color', 'lightblue')
        $('li:nth-child(3)').css('background-color', 'purple')

    })
})