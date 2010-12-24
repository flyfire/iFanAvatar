$(document).ready(function() { 

    String.prototype.s= function (o) {
        return this.replace(/{([^{}]*)}/g,
            function (a, b) {
                var r = o[b];
                return typeof r === 'string' || typeof r === 'number' ? r : a;
            }
        );
    };
        
    
    function getCheckedStatus(checkboxID) {
        //return 1 if checked, or 0 
        if ($(checkboxID).attr('checked')) {
            return 'True';
        }
        else {
            return 'False';
        }
    } 

      
    $('#btn_gen').click(function() { 
        $("#pic_output").html("<img id='loading-icon' src='/site_media/images/loading.gif' />");

        $.get('/gen', getArgs(), function(data) {
            $("#pic_output").html(data);

        }); //request ends

        //click to download
               
    });//submitbutton ends

   
    /******* code from index.html **********/

    function getHatArgs()
    {
        //get current image result, 
        //HAT: rotation angle, size, offset of the
        
        //site_media/result/bc98ff0348403f8098a3f7207c29f94f.png
                
        var hat=$("#xmas-hat").attr("src");//   site_media/images/hat.png
        var angle=parseInt($("#xmas-slider").slider( "option", "value"));
        angle=360-angle;
        
        var base=$("#avatar-img").offset(); //left, top
        var hatoffset=$("#xmas-hat-holder").offset();
        var offsetLeft=hatoffset.left-base.left;
        var offsetTop=hatoffset.top-base.top;
        var hatWidth=$("#xmas-hat-holder>img").width();
        var hatHeight=$("#xmas-hat-holder>img").height();
        
        return {
            bg:bg,
            hat:hat,
            angle:angle,
            offsetTop:offsetTop,
            offsetLeft:offsetLeft,
            hatHeight:hatHeight,
            hatWidth:hatWidth
        }
    }
        
    function int2css(deg) {
            return "-webkit-transform: rotate("+deg+"deg); -moz-transform: rotate("+deg+"deg);";
        } 


    //uploading img
    $('#uploading_form').ajaxForm({ 
        // dataType identifies the expected content type of the server response 
        dataType:'json', 
 
        // success identifies the function to invoke when the server response 
        // has been received 
        success:  function(data){
            var image=data.fn;
//            image="<image scr=\"{image}\">".s({image:image});
            $("#preview").attr("style", "background-image:url({image}); background-size: 200px 200px;".s({image:image}));
            $("#hat-holder").fadeIn();
            $("#hat-holder").resizable({
                    aspectRatio: 1/1,
                    maxHeight: 200,
                    maxWidth: 200,
                    minHeight: 10,
                    minWidth: 10,
                }).draggable({
                    zIndex: 9999999,
                    containment:"#content",
                    stop: function() {
                        $(this).removeClass('ui-draggable-dragging');
                    },
            });//xmas-hat-holder end

            $("#hats img").click(function(){
                var img=$(this).attr('src');
                $("#hat").attr('src', img);
                return false;
                    });//hat image select end

            $("#xmas-slider").slider({
                max: 359,
                min: 0,
                range: "min",
                slide: function(event, ui) {
                    var angle = ui.value;//turn angle to counter clockwise// original 360- ui.value
                    $("#hat").attr("style", int2css(angle));
                }
            });//slider end
            function getArgs()
            {
                var bg=$("#preview").attr("style");
                bg=bg.replace(/^.*\(['"]?/,''); 
                bg=bg.replace(/['"]?\).*$/,'');

                var hat=$("#hat").attr("src");//   site_media/images/hat.png
                var angle=parseInt($("#xmas-slider").slider( "option", "value"));
                
                var base=$("#preview").offset(); //left, top
                var hatoffset=$("#hat-holder").offset();
                var offsetLeft=hatoffset.left-base.left;
                var offsetTop=hatoffset.top-base.top;
                var hatWidth=$("#hat-holder>img").width();
                var hatHeight=$("#hat-holder>img").height();
                
                return {
                    bg:bg,
                    hat:hat,
                    angle:angle,
                    offsetTop:offsetTop,
                    offsetLeft:offsetLeft,
                    hatHeight:hatHeight,
                    hatWidth:hatWidth
                } 
            }
            
            $("#generate").click(function(){
                var args=getArgs();
                $.get("/gen", args, function(data){
                    $("#result").html(data);
                    });
                return false;
            });


            return false;
        } 

    }); 
    
    
    
});//document ready ends

