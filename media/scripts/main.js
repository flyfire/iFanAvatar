$(document).ready(function() { 

    String.prototype.s= function (o) {
        return this.replace(/{([^{}]*)}/g,
            function (a, b) {
                var r = o[b];
                return typeof r === 'string' || typeof r === 'number' ? r : a;
            }
        );
    };
        
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
        var bg = $("#bg").val() + getImageArgs($(this)) + ".png";

        //important code for fixing pic name; 
        //pls don't delete
        bg=bg.replace(/\.png[_bh]{0,3}\.png$/, '.png'); 

        var bg_h = $("#highlight").attr("checked");
        var bg_b = $("#border").attr("checked");

        var text=$("#text_input").val();
        var textColor=$("#textColor").val();
        var shadowColor=$("#shadowColor").val();
        var font=$("#font_select").val();
        var border=getCheckedStatus("#border");
        var shadow=$("input[name='shadow']:checked").val();
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

    $('#btn_gen').click(function() { 
        $("#pic_output").html("<img id='loading-icon' src='/site_media/images/loading.gif' />");
        $.get('/gen', getArgs(),function(data) {
            $("#pic_output").html(data);
            //add img url to history:
            var history=$("#history").html();
            var match=data.match(/\w+\.png/i);
            if (!match)
            {
                return false;
            } 
            var img=match[0];
            if (history.search(img) == -1 && data.search("loading.gif") == -1) {
                if ($("#history>a>img").length >= 10) {
                    $("#history>a>img:first").remove();
                }
                $("#history").append(data);
                $("#history > a >img").click(function() {
                    
                    var src=$(this).attr('src');
                    function img2html(img)
                    {
                        return "<a href=\"result?url={url}\"><img src=\"{url}\"></a>".s({url:src});
                    }
                    $("#pic_output").html(img2html(src));
                    //return false is very import to avoid downloading 
                    //from the history zone
                    return false;
                });
            }
        }); //request ends

    });//submitbutton ends

    /*
    $("#font_select").change(function() {
        var font=$(this).val();
        $("#text_input").css("font-family","'"+font+"'");

    });
    */

    $('.bgcolors').click(function() {
        var bgColor = $(this).css('background-color');
        $("#bg").val($(this).attr('id'));
        $('#text_input').css('background-color', bgColor);
    });

    $('#highlight').click(function() {
        $('#text_input').toggleClass('sprite');
    });

    $("#preset").change(function() {
        set=$(this).val();
        if (set=='ifan') { 
            $("#font_select").val("iYaHei.ttf"); 
            $("#textColor").val("#FFFFFF");
            $("#bg").val("c206_hb.png");
            $('#border').attr('checked','checked');
            $('#highlight').attr('checked','checked'); 
            $("#c206").click();
            $("input[name='shadow'][value=1]").attr('checked', 'checked'); 
            $("#shadowColor").val("#000000"); 
        }
        else if (set == 'fanfou') {
            //TODO: add shadow control 
            $("#font_select").val("msjhbd.ttf");
            $("#textColor").val("#FFFFFF");
            $("#bg").val("c192.png");
            $('#border').removeAttr('checked');
            $('#highlight').removeAttr('checked'); 
            $("#c192").click();
            $("input[name='shadow'][value=0]").attr('checked', 'checked'); 
            $("#shadowColor").val("#000000"); 
        } 
        else {
            $("#textColor").val("#FFFFFF"); 
        }

    });
    $("#preset").click(function(){
         $(this).change(); 
    });
    $("#preset").blur(function(){
         $(this).change(); 
    });
    $("#preset").change();

    //download pic
    $("#pic_output").click(function(){
        //get the url:
        var url=$("#pic_output img").attr('src');
        //TODO:download the pic url.
    }); 
    
    /******* code from index.html **********/

    $('#textColor, #shadowColor').ColorPicker({
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
                      if ($(el).attr("id")=="textColor")
    {
        $("#text_input").css('color', '#' + hex);
    }
                      else if (getCheckedStatus("#shadow")=='True') {
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
   
    /****** end of code from index.html ********/
});//document ready ends

