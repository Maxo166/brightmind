$(function(){
    $("#nav_burger").click(function(){
        $("#nvbar_menu").slideToggle('fast');
    })
    $('.navbar-item.has-dropdown a.navbar-link').on('click', function(){
        $('.navbar-dropdown').slideToggle('fast')
    });
    $('.comment-dropdown-trigger button').on('click', function(){
        $(this).parent()
            .next('.comment-dropdown-menu')
            .slideToggle('fast')
    });
    
    $( ".login-form>form").find("div>label.label").each(function(){
        $(this).addClass("has-text-link is-small")
    })
    $("div#div_id_password1").focusin(function(){
        $("div#div_id_password1 ul").fadeIn()
    })
    $( "div#div_id_password1" ).focusout( function () {
        $( "div#div_id_password1 ul" ).fadeOut()
    } );
    $( "#id_username" ).focusin( function () {
        $( " p#hint_id_username" ).fadeIn()
    } );
    
    $( "div#div_id_first_name, div#div_id_last_name" ).wrapAll( "<div class='first_last_name is-flex'></div>" )
    
    $( "#id_username" ).focusout( function () {
        $( " p#hint_id_username" ).fadeOut()
    } );
    $(".notification>.delete").click(function(e){
        e.preventDefault()
        $(this).parent(".notification").hide()
    })
})