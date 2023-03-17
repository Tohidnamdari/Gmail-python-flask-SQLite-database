    email=document.getElementById('re_email')
    pass=document.getElementById('re_password')
    info=document.getElementById('info')

    pass.addEventListener('change',(event)=>{
        console.log(pass.value.length)
        if (pass.value.length<8)
    {
        info.innerHTML="پسورد باید دارای حداقل 8 رقم باشد"
        info.style.display='block';
        info.style.color="#ff0000";
        info.style.fontSize='12px';
        info.style.margin='auto';

    }
    else{


        info.style.display='none';
    }
    })
