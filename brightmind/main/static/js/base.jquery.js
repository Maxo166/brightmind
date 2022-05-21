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
    
})