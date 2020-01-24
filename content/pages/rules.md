Title: Rules for Pentagame
Date: 2020-1-21 10:20
Modified: 2020-1-21 10:20
Category: General
Tags: general, rules
Slug: rules
Authors: Jan Suchanek
Summary: Rules section for pentagame.org



## [Rules in English](https://pentagame.org/pdf/Illustrated_Rules.pdf) and [Rules in german](http://pentagame.org/pdf/Illustrated_Rules__German_.pdf)

Rules explanation in english [Youtube](https://www.youtube.com/watch?v=pnXDFhH5gMI)

Rules explanation in german [Youtube](https://www.youtube.com/watch?v=H1BSNvzTxko)

[Sources for multilingual rules](/category/rules/sources.html)

<button type="button" class="btn btn-primary btn-shadow" data-toggle="modal" data-target="#modal"><i class="fa fa-play"></i> Launch Trailer</button>

<div class="modal fade" tabindex="-1" data-backdrop="False" role="dialog"id="modal">
  <div class="modal-dialog" role="document">
  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
  <span aria-hidden="true">&times;</span>
</button>
    <div class="modal-body">       
        <!-- 16:9 aspect ratio -->
        <div class="embed-responsive embed-responsive-16by9 text-center">
          <video class="embed-responsive-item" src="https://pentagame.org/video/Pentagame_Teaser_E.mp4" id="video1" allowscriptaccess="always" webkitallowfullscreen mozallowfullscreen allowfullscreen></video>
        </div>
    </div>
  </div>
</div>


<script>
$('#modal').on('shown.bs.modal', function () {
  $('#video1')[0].currentTime = 0;
  $('#video1')[0].play();
})
$('#modal').on('hidden.bs.modal', function () {
  $('#video1')[0].pause();
})
</script>
