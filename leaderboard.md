---
layout: markdown
title: Leaderboard
permalink: /leaderboard/
---


<input 
  style="max-width: 360px;"
  class="form-control" 
  type="text" 
  placeholder="Search" 
  aria-label="Search" 
  onkeyup="search(this)">

{% include partials/leaderboard.html %}


<script>
  // apply filter after search typing delay
  function search(searchInput) {
    delay(function(){
      applyFilter(searchInput);
    }, 400 );
  }

  // filter users to ones that match search term
  function applyFilter(searchInput) {
    // let searchInput = document.getElementById('searchInput');
    let searchText = searchInput.value.toLowerCase();
    // let rows = document.getElementsByTagName("tbody")[0].innerHTML.split("<tr");
    let rows = document.querySelector("#leaderboardTable tbody").innerHTML.split("<tr");
    let show = `style="visibility: visible;"`;
    let hide = `style="visibility: collapse;"`;
    let table = rows[0];

    for (let i = 1; i < rows.length; i++) {
      let splitStart = ".com/u/";
      let splitEnd = "</a>";
      let regex = new RegExp("(?:"+splitStart+")((.[\\s\\S]*))(?:"+splitEnd+")", "ig");
      let user = rows[i];
      let row;
      if (regex.exec(user)[1].includes(searchText)) {
        row = show + user;
        row.replace(hide, "");
      } else {
        row = hide + user;
        row.replace(show, "");
      }
      table += "<tr " + row;
    }
    document.querySelector("#leaderboardTable tbody").innerHTML = table;
  }

  // general delay function
  var delay = (function(){
    var timer = 0;
    return function(callback, ms){
      clearTimeout (timer);
      timer = setTimeout(callback, ms);
    };
  })();
</script>

