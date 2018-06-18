$(function () {

  // function draw() {
  //   var canvas = $('#myCanvas')[0];
  //   if (canvas.getContext) {
  //     var ctx = canvas.getContext('2d');
  //   }
  // }
  var canvas = $('#myCanvas')[0];
  var context = $('#myCanvas')[0].getContext("2d");

  $('#blink').click(function() {
    blink();
  });

  $('#clear').click(function() {
    canvas.width = canvas.width;
  });

  var images = {};
  loadImage("body");
  loadImage("head");
  loadImage("arm");
  loadImage("feet");

  function loadImage(name) {
    images[name] = new Image();
    images[name].onload = function() {
        resourceLoaded();
    }
    images[name].src = "static/images/" + name + ".gif";
  }

  var totalResources = 4;
  var numResourcesLoaded = 0;
  var fps = 30;

  function resourceLoaded() {

    numResourcesLoaded += 1;
    if(numResourcesLoaded === totalResources) {
      setInterval(redraw, 1000 / fps);
    }
  }

  var charX = 245;
  var charY = 185;

  function redraw() {

    var x = charX;
    var y = charY;

    canvas.width = canvas.width; // clears the canvas

    drawEllipse(x , y + 285, 300 - breathAmt, 10);
    context.drawImage(images["body"], x - 130, y + 50 - breathAmt);
    context.drawImage(images["head"], x - 130, y - 165 - breathAmt);
    context.drawImage(images["arm"], x - 32, y - 125 - breathAmt);
    context.drawImage(images["feet"], x - 80, y + 200);

    drawEllipse(x + 112, y - 98 - breathAmt, 20, curEyeHeight); // Left Eye

  }


  function drawEllipse(centerX, centerY, width, height) {

    context.beginPath();

    context.moveTo(centerX, centerY - height/2);

    context.bezierCurveTo(
      centerX + width/2, centerY - height/2,
      centerX + width/2, centerY + height/2,
      centerX, centerY + height/2);

    context.bezierCurveTo(
      centerX - width/2, centerY + height/2,
      centerX - width/2, centerY - height/2,
      centerX, centerY - height/2);

    context.fillStyle = "black";
    context.fill();
    context.closePath();
  }

  var breathInc = 0.1;
  var breathDir = 1;
  var breathAmt = 0;
  var breathMax = 2;
  var breathInterval = setInterval(updateBreath, 1000 / fps);

  function updateBreath() {

    if (breathDir === 1) {  // breath in
      breathAmt -= breathInc;
      if (breathAmt < -breathMax) {
        breathDir = -1;
      }
    } else {  // breath out
      breathAmt += breathInc;
      if(breathAmt > breathMax) {
        breathDir = 1;
      }
    }
  }

  var maxEyeHeight = 20;
  var curEyeHeight = maxEyeHeight;
  var eyeOpenTime = 0;
  var timeBtwBlinks = 4000;
  var blinkUpdateTime = 200;
  // var blinkTimer = setInterval(updateBlink, blinkUpdateTime);
  //
  // function updateBlink() {
  //
  //   eyeOpenTime += blinkUpdateTime;
  //
  //   if(eyeOpenTime >= timeBtwBlinks){
  //     blink();
  //   }
  // }

  function blink() {

    curEyeHeight -= 1;
    if (curEyeHeight <= 0) {
      eyeOpenTime = 0;
      curEyeHeight = maxEyeHeight;
    } else {
      setTimeout(blink, 10);
    }
  }

});
