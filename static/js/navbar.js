function navbar(){
    var title=document.title;
    // var syntax=`
 
    // `;
    // $("#navbarlogin").append(syntax);
    $('.nav-link').removeClass("nav-active");
    if (title =="Log In"){
        $("#loginPage").addClass("nav-active");
    }else if(title =="Sign Up"){
        $("#signupPage").addClass("nav-active");
    }else if(title =="Home"){
        $("#homePage").addClass("nav-active");
    }else if(title =="Password Change"){
        $("#passwordResetPage").addClass("nav-active");
    }else if(title =="Create Article"){
        $("#addArticlePage").addClass("nav-active");
    }else if(title =="Articles"){
        $("#viewArticlePage").addClass("nav-active");
    }
    
    //articles
    //[x]logout redirect so quickly don't need this case.
}

function init(){
    navbar();
}
window.onload=init;