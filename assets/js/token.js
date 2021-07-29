function Token(){
    const token = new URLSearchParams(window.location.href.replace("#", "&")).get('access_token');
    document.write(token);
}