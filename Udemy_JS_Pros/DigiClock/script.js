function updateClock(){
    const now = new Date();

    const hr = document.getElementById('hour');
    const min = document.getElementById("min");
    const sec = document.getElementById("sec");

    hr.textContent = (now.getHours() <10) ? '0' + now.getHours() : now.getHours() ;
    min.textContent = now.getMinutes() <10 ? '0' + now.getMinutes() : now.getHours();
    sec.textContent = now.getSeconds() <10 ? '0' + now.getSeconds() : now.getSeconds();
}

setInterval(updateClock, 1000);
