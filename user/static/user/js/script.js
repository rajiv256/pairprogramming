$(document).ready(function(){
    $("#tag-edit").click(function(){
        $(this).hide() ;
        $("#tag-edit-form").show() ;
    });
    $("#close-tag-edit").click(function(){
        $("#tag-edit-form").hide() ;
        $("#tag-edit").show() ;
    });
    var all_tags = []
    $("#tag-input").hover(function(){
        if (all_tags.length == 0){
            $.ajax({url: "/autocomplete/", success: function(data){
                alert(data.length) ;
                for (i = 0 ; i < data.length ; i++){
                    all_tags[i] = data[i].toString() ;
                }
            }});
        }
    });
    var availableTags = [
      "ActionScript",
      "AppleScript",
      "Asp",
      "BASIC",
      "C",
      "C++",
      "Clojure",
      "COBOL",
      "ColdFusion",
      "Erlang",
      "Fortran",
      "Groovy",
      "Haskell",
      "Java",
      "JavaScript",
      "Lisp",
      "Perl",
      "PHP",
      "Python",
      "Ruby",
      "Scala",
      "Scheme"
    ];

    $("#tag-input").autocomplete({
        source: all_tags
    });
});