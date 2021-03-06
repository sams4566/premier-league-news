/*!
* Start Bootstrap - Blog Home v5.0.7 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

/*jshint esversion: 6 */

/**
 * Reveals and hides the 'More Comments' button when there
 * are more comments available to view.
*/
$(function () {
    $(".comment-list").slice(0, 4).show();
    $("#load-comments").on('click', function () {
        $(".comment-list:hidden").slice(0, 4).slideDown();
        if ($(".comment-list:hidden").length == 0) {
            $("#load-comments").hide();
        }
    });
});

/**
 * Reveals and hides the 'More Categories' button when there
 * are more categories available to view.
*/
$(function () {
    $(".category-list").slice(0, 6).show();
    $("#load-categories").on('click', function () {
        $(".category-list:hidden").slice(0, 6).slideDown();
        if ($(".category-list:hidden").length == 0) {
            $("#load-categories").hide();
        }
    });
});

/**
 * Sets up the Summernote textarea box
*/
$(document).ready(function(){
    $('#summernote').summernote({
        placeholder: 'Hello stand alone ui',
        tabsize: 2,
        height: 300,
        toolbar: [
        ['style', ['style']],
        ['font', ['bold', 'underline', 'clear']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['table', ['table']],
        ['insert', ['link', 'picture', 'video']],
        ['view', ['fullscreen', 'codeview', 'help']]
        ]
    });
});

/**
 * Sets a timer for the notifications that appear below the 
 * navbar to disappear
*/
setTimeout(function() {
    let info = document.getElementById("msg");
    let alert = new bootstrap.Alert(info);
    alert.close();
}, 2500);

