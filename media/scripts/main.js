$(document).ready(function() { 

    function getImageArgs() {
        var border=getCheckedStatus("#border");
        var highlight=getCheckedStatus("#highlight");
        var status="";
        if (highlight=='True') {
            status+="h";
        }
        if (border=='True') {
            status+="b";
        }
        if (status) {
            status="_"+status;
        }
        return status; 
    }

    function getCheckedStatus(checkboxID) {
        //return 1 if checked, or 0 
        if ($(checkboxID).attr('checked')) {
            return 'True';
        }
        else {
            return 'False';
        }
    } 

    //get auguments 
    function getArgs() {
        var bg = $("#bg").val();

        var bg_h = $("#highlight").attr("checked");
        var bg_b = $("#border").attr("checked");

        if (!(bg_h || bg_b)) {
            bg += '.png';
        } else if(!bg_h &&  bg_b) {
            bg += '_b.png';
        } else if(bg_h && !bg_b) {
            bg += '_h.png';
        } else if(bg_h && bg_b) {
            bg += '_hb.png';
        }

        var text=$("#text_input").val();
        var textColor=$("#textColor").val();
        var shadowColor=$("#shadowColor").val();
        var font=$("#font_select").val();
        var border=getCheckedStatus("#border");
        var shadow=getCheckedStatus("#shadow");
        var highlight=getCheckedStatus("#highlight"); 

        return {
            'bg':bg,
                'text':text,
                'textColor':textColor,
                'shadowColor':shadowColor,
                'font':font, 
                'border':border,
                'shadow':shadow,
                'highlight':highlight,
        };
    }

    $('#btn_gen').click(function(){

        x=getArgs();
        $.get('/gen', getArgs(),function(data) {
            $("#pic_output").html(data);
        }); //request ends

    });//submitbutton ends
    /*
    //waiting for kevin's background pics
    $("#bg").change(function(){
    url=window.location.href+"site_media/colors/"+$(this).val();
    $("#text_input").css("background-image","url("+url+")");

    });
    */

    $("#font_select").change(function() {
        var font=$(this).val();
        $("#text_input").css("font-family","'"+font+"'");

    });

    $("#preset").blur(function() {
        set=$(this).val();
        if (set=='aifan') {
            $("#font_select").val("iYaHei.ttf"); 
            $("#textColor").val("#FFFFFF");
            $("#bg").val("logo192.png");
            $('#border').attr('checked','checked');
            $('#shadow').attr('checked','checked');
            $('#highlight').attr('checked','checked'); 
        }
        else if (set == 'fanfou') {
            $("#font_select").val("msjhbd.ttf");
            $("#textColor").val("#FFFFFF");
            $("#bg").val("logo172.png");
            $('#border').removeAttr('checked');
            $('#shadow').removeAttr('checked');
            $('#highlight').removeAttr('checked');
        } 
        else {
            $("#textColor").val("#FFFFFF"); 
            $("#shadowColor").val("#000000");

        }

    });

    $('.bgcolors').click(function() {
        var bgColor = $(this).css('background-color');
        $("#bg").val($(this).attr('id'));
        $('#text_input').css('background-color', bgColor);
    });

    $('#highlight').click(function() {
        $('#text_input').toggleClass('sprite');
    });
    //$("#border, #highlight").click(function(){
    //    var status=getImageArgs();
    //    var img=$("#text_input").css('background-image');
    //    img=img.replace(/c(\d+).*?\.png/, "c$1"+status+".png"); 
    //    $("#text_input").css('background-image', img);
    //});

    /******** code for index.html **********/
    $('#textColor, #shadowColor').ColorPicker( {
        onChange: function(hsb, hex, rgb, el) {
                      function getCheckedStatus(checkboxID) {
                          //return 1 if checked, or 0 
                          if ($(checkboxID).attr('checked')) {
                              return 'True';
                          }
                          else {
                              return 'False';
                          }
                      }
                      $(el).val("#"+hex);
                      if ($(el).attr("id")=="textColor") {
                          $("#text_input").css('color', '#' + hex);
                      }
                      else if (getCheckedStatus("#shadow")=='True') {
                          //text-shadow: 0.1em 0.1em #333
                          $("#text_input").css('text-shadow', '#' + hex+" 0 0 3px");
                      }

                  },
            onSubmit: function(hsb, hex, rgb, el) {
                          hex=hex.toUpperCase();
                          $(el).val("#"+hex);
                          $(el).ColorPickerHide();
                      },
            onBeforeShow: function () {
                              $(this).ColorPickerSetColor(this.value);
                          }

    })
    .bind('keyup', function() {
        $(this).ColorPickerSetColor(this.value.replace("#",''));
    });
    $("#textColor").val("#FFFFFF");
    $("#shadowColor").val("#000000");

    /*********** code from index.html end ********/
});//document ready ends

