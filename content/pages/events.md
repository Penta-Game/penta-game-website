Title: Events
Date: 2020-1-21 10:20
Modified: 2020-1-21 10:20
Category: General
Tags: general, events
Slug: events
Authors: Cobalt, Jan Suchanek
Summary: Events section for pentagame.org

<br>

# <div class="glow">P-Day </div>
## <div class="glow" id="target"></div>

<br>

P-Day is MARCH 14th 2020.

Location t.b.a. :)

Kickstarter Edition Release

Pentagame Cup Semi-Finals and Final

Dresscode: Cats, Rabbits, Hedgehogs, Geese, Black Blocks, Grey Blocks.


<center>
  <img src="http://pentagame.org/images/Pentagame-Thursday.png" class="img-fluid" />
</center>



<script>
var countDownDate = new Date("Mar 14, 2020 19:00:00").getTime();

var x = setInterval(function() {

  var now = new Date().getTime();

  var distance = countDownDate - now;

  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById("target").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";

  if (distance < 0) {
    clearInterval(x);
    document.getElementById("target").innerHTML = "";
  }
}, 1000);
</script>
