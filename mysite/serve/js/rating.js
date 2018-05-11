function postRating(videoId,count){
  $.ajax({
    url: '{% url "animeweb:post_rating"  %}',
    data: {
      'username': {{ request.user.id}},
      'videoId':videoId,
      'count':count
    },
    dataType: 'json',
    success: function (data) {

      var obj = JSON.parse(data)
      var average = Number(obj['average']);
      var starId = "star-"+average;
      $("#"+starId).prop('checked', true);
      if (data.is_taken) {
        alert("A user with this username already exists.");
      }
    }



  });
}
