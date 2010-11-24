$(document).ready(function() { 

    function getCheckedStatus(checkboxID)
    {
        //return 1 if checked, or 0 
        if ($(checkboxID).attr('checked'))
        {
            return 'True';
        }
        else
        {
            return 'False';
        }
    } 

    //get auguments 
    function getArgs()
    {
        var bg=$("#bg").val();     
        var text=$("#text").val();
        var textColor=$("#textColor").val();
        var shadowColor=$("#shadowColor").val();
        var font=$("#font").val();
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

    $('#submitbutton').click(function(){
        $.get('/gen', getArgs(),function(data) {
            $("#pic_output").html(data);
            }); //request ends

    });//submitbutton ends

    $("#preset").blur(function(){
            set=$(this).val();
            if (set=='aifan')
            {
                $("#textColor").val("#00AAFF");
                $("#bg").val("logo192.png");
                $('#border').attr('checked','checked');
                $('#shadow').attr('checked','checked');
                $('#highlight').attr('checked','checked'); 
            }
            else if (set == 'fanfou')
            {
                $("#textColor").val("#00CCFF"); 
                $("#bg").val("logo172.png"); 
                $('#border').removeAttr('checked');
                $('#shadow').removeAttr('checked');
                $('#highlight').removeAttr('checked'); 
            } 
            else
            {
                $("#textColor").val("#FFFFFF"); 
                $("#shadowColor").val("#000000");

            }
            
        });

});//document ready ends

