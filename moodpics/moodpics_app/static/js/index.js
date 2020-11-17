alert("Success");

$(".likebutton").click(function(){
    
    var post_id = $(this).attr("postid");
    var post = this;
    $.ajax({
        url: `/feed/posts/${post_id}/like`,
        method: "GET",
        success: function(response){

            
            $(post).attr("src","https://moodpics.s3-us-west-1.amazonaws.com/static/img/sharp_favorite_red_48dp.png")
        }
    })
})


