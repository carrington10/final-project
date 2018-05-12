function postRating(videoId,count){
  $.ajax({
    url: '/video/'+videoId+'/rate/',
    data: {
      'videoId':videoId,
      'count':count
    },
    dataType: 'json',
    success: function (obj) {


      var average = Number(obj['average']);
      var starId = "star-"+average;
      $("#"+starId).prop('checked', true);
      if (data.is_taken) {
        alert("A user with this username already exists.");
      }
    }



  });
}
